# 📄 Smart Legal Document Manager

A lightweight **document version control system for legal teams** built using **FastAPI and SQLite**.
The system allows lawyers to **create, update, track versions, and compare document changes** in a clear and structured way.

---

## 🚀 Features

### 1️⃣ Document Creation

Users can create a new legal document with a title, content, and author.

### 2️⃣ Document Versioning

Every update creates a **new version** instead of overwriting the previous one.

Example:

Version 1

```
The company agrees to provide salary and benefits.
```

Version 2

```
The company agrees to provide salary, health benefits and insurance.
```

---

### 3️⃣ Duplicate Version Detection

If a user tries to upload **identical content**, the system detects it and prevents creating a duplicate version.

Example response:

```
No changes detected. Version remains 2
```

---

### 4️⃣ Version Comparison

Two versions of a document can be compared to highlight changes.

Output example:

```
+ The company agrees to provide salary, health benefits and insurance.
- The company agrees to provide salary and benefits.
```

Green lines indicate **added content**, while red lines indicate **removed content**.

---

### 5️⃣ Crash-Safe Database Transactions

The system uses **SQLAlchemy transactions** to ensure that partial data is not saved if a failure occurs during updates.

---

### 6️⃣ Clean Project Architecture

The project follows a modular backend structure to keep the code easy to maintain and understand.

---

## 🧱 Tech Stack

Backend

* FastAPI
* Python
* SQLAlchemy
* SQLite

Frontend

* HTML
* CSS
* Vanilla JavaScript

Utilities

* difflib (Python library for text comparison)

---

## 📁 Project Structure

```
smart-legal-document-manager

app
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── notification.py
│
├── routes
│   └── document_routes.py
│
└── static
    └── index.html

requirements.txt
README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/smart-legal-document-manager.git
cd smart-legal-document-manager
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the server

```
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 🧪 How to Use

### Create Document

Enter:

* Title
* Content
* User

Click **Create Document**.

---

### Update Document

Enter:

* Document ID
* Updated content
* User

Click **Update Version**.

---

### Compare Versions

Enter:

* Document ID
* Version 1
* Version 2

Click **Compare**.

---

## 📊 Example Workflow

1️⃣ Create a document
2️⃣ Update the document (new version created)
3️⃣ Compare two versions
4️⃣ View added and removed content

---

## 🎯 Design Decisions

* **Version based storage** instead of overwriting documents
* **Line-by-line comparison** for legal readability
* **Duplicate version prevention**
* **Transaction-safe updates**

---

## 📌 Future Improvements

* Document history panel
* Authentication for users
* Rich text document editor
* Role-based access control
* Cloud database support

---

## 👨‍💻 Author

Built as part of an **SDE-1 technical task** demonstrating backend design, API development, and document version control systems.

---
