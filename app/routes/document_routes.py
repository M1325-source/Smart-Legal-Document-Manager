from fastapi import APIRouter, Depends, BackgroundTasks, Query
from sqlalchemy.orm import Session
import difflib

from app.database import SessionLocal
from app import crud, schemas
from app.notification import check_significant_change, send_notification

router = APIRouter(prefix="/documents", tags=["Documents"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE DOCUMENT
@router.post("/")
def create_document(
    data: schemas.DocumentCreate,
    db: Session = Depends(get_db)
):

    new_doc = crud.create_document(
        db,
        title=data.title,
        content=data.content,
        user=data.user
    )

    return {
        "document_id": new_doc.id,
        "message": "Document created successfully"
    }


# UPDATE DOCUMENT (CREATE NEW VERSION)
@router.put("/{doc_id}")
def update_document(
    doc_id: int,
    data: schemas.DocumentUpdate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):

    try:

        versions = crud.get_versions(db, doc_id)

        if not versions:
            return {
                "status": "error",
                "message": "Document not found"
            }

        last_version = versions[-1]
        last_content = last_version.content

        # IDENTICAL TEXT CHECK
        if last_content.strip() == data.content.strip():
            return {
                "status": "ignored",
                "message": "No changes detected",
                "current_version": last_version.version_number
            }

        # CREATE NEW VERSION
        new_version = crud.update_document(
            db,
            doc_id,
            data.content,
            data.user
        )

        db.commit()

        # CHECK SIGNIFICANT CHANGE
        if check_significant_change(last_content, data.content):
            background_tasks.add_task(send_notification, doc_id)

        return {
            "status": "success",
            "message": "Document updated",
            "document_id": doc_id,
            "previous_version": last_version.version_number,
            "new_version": new_version.version_number,
            "updated_by": data.user
        }

    except Exception as e:

        db.rollback()

        return {
            "status": "error",
            "message": "Update failed",
            "details": str(e)
        }


# COMPARE TWO DOCUMENT VERSIONS
@router.get("/{doc_id}/compare")
def compare_versions(
    doc_id: int,
    v1: int = Query(...),
    v2: int = Query(...),
    db: Session = Depends(get_db)
):

    versions = crud.get_versions(db, doc_id)

    version1 = None
    version2 = None

    for v in versions:
        if v.version_number == v1:
            version1 = v.content
        if v.version_number == v2:
            version2 = v.content

    if not version1 or not version2:
        return {"error": "Versions not found"}

    diff = list(
        difflib.ndiff(
            version1.splitlines(),
            version2.splitlines()
        )
    )

    added = []
    removed = []

    for line in diff:
        if line.startswith("+ "):
            added.append(line[2:])
        elif line.startswith("- "):
            removed.append(line[2:])

    return {
        "added": added,
        "removed": removed
    }