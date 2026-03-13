from datetime import datetime
from app import models


# CREATE DOCUMENT
def create_document(db, title, content, user):

    new_doc = models.Document(
        title=title
    )

    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)

    first_version = models.DocumentVersion(
        document_id=new_doc.id,
        content=content,
        version_number=1,
        updated_by=user,
        created_at=datetime.utcnow()
    )

    db.add(first_version)
    db.commit()

    return new_doc


# GET ALL VERSIONS
def get_versions(db, doc_id):

    return db.query(models.DocumentVersion)\
        .filter(models.DocumentVersion.document_id == doc_id)\
        .order_by(models.DocumentVersion.version_number)\
        .all()


# UPDATE DOCUMENT (CREATE NEW VERSION)
def update_document(db, doc_id, content, user):

    versions = db.query(models.DocumentVersion)\
        .filter(models.DocumentVersion.document_id == doc_id)\
        .order_by(models.DocumentVersion.version_number)\
        .all()

    new_version_number = 1

    if versions:
        new_version_number = versions[-1].version_number + 1

    new_version = models.DocumentVersion(
        document_id=doc_id,
        content=content,
        version_number=new_version_number,
        updated_by=user,
        created_at=datetime.utcnow()
    )

    db.add(new_version)

    return new_version