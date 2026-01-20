
# RESTful API for Swimmers’ Gala Performance Records

This repository contains coursework for the **Web Services and Applications (WSAA)** module.  
The core project is a **Flask-based RESTful web application and API** for managing swimmers’ competition results, including full CRUD functionality and database integration.

---

## What This Repository Is For

This repository demonstrates:
- RESTful web services using Python and Flask
- CRUD operations via HTTP methods
- Backend–database interaction using MySQL
- Separation of concerns (application logic, database configuration, templates)
- Practical coursework for the WSAA module

The repository includes labs, assignments, and a fully implemented core project.

---

## Core Project Overview

The main project, located in the `project/` directory, implements a **RESTful API and web application** for managing swimmers’ gala performance records.

Users can:
- Add, edit, delete swimmer results
- Filter swimmers by age group and sex
- Access data via a web interface or REST API endpoints

The project uses **Flask** for the backend and **MySQL** for persistent storage.


---

## Key Features

- Flask-based RESTful API
- CRUD operations (Create, Read, Update, Delete)
- MySQL database integration
- JSON-based API communication
- HTML templates for a simple user interface
- Modular and well-organised project structure

---

## Required Technologies

- **Python 3.x**
- **Flask**
- **MySQL**
- **pip**
- HTML / JavaScript (for templates)

---

## How to Run the Project (Local Setup)

### 1) Clone the repository

```bash
git clone https://github.com/Kate-217/WSAA-coursework.git
cd WSAA-coursework/project
````

---

### 2) Create and activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
# venv\Scripts\activate       # Windows
```

---

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4) Configure the database

Copy the configuration template:

```bash
cp db_config.py_template db_config.py
```

Edit `db_config.py` and add your local MySQL credentials.

---

### 5) Create and initialise the database

```bash
python create_db.py
```

> Note: You must have permissions to create and drop databases.

---

### 6) Run the Flask application

```bash
python app.py
```

The server will run at:

```text
http://127.0.0.1:5000/
```

---

## User Manual / Usage

### REST API

The API supports standard CRUD operations on swimmer records.

HTTP methods used:

* **GET** – retrieve swimmer data
* **POST** – add new swimmer results
* **PUT** – update existing records
* **DELETE** – remove records

Requests and responses are JSON-formatted.
Example API requests are documented in the project-level README.

---

### Web Interface

If templates are enabled:

1. Start the Flask server.
2. Open `http://127.0.0.1:5000/` in a browser.
3. Manage swimmer results through the user interface.

---

## Notes

* This project is intended for **educational purposes**.
* This project was developed using materials and lectures provided as part of the
  **Web Services and Applications** module at **Atlantic Technological University (ATU)**.

---

## Author

Katerina Lisovenko

