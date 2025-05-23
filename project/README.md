

# Swimmers’ Gala Performance Records

This project is a simple web application built with Flask and MySQL to manage swimmers' competition results.
You can add, edit, delete, and filter swimmers using a user-friendly interface or RESTful API.

### Live demo:

Visit the deployed version at:
 **[https://katespb.pythonanywhere.com/](https://katespb.pythonanywhere.com/)**

---

## Getting Started (Local Setup)

1. **Clone the current repository locally**

   ```bash
   git clone git@github.com:Kate-217/WSAA-coursework.git
   ```

2. **Rename configuration file**

   ```bash
   mv db_config.py_template db_config.py
   ```

3. **Edit `db_config.py`**
   Add your MySQL credentials to connect to your local MySQL server:

   ```python
   db_config = {
       "host": "localhost",
       "user": "your_mysql_user",
       "password": "your_mysql_password",
       "database": "your_database"
   }
   ```

4. **Install required Python packages**

   ```bash
   pip install -r requirements.txt
   ```

5. **Create and initialize the database**

   > You must have privileges to **DROP and CREATE** databases.

   ```bash
   python project/create_db.py
   ```

6. **Run the Flask app**

   ```bash
   python project/app.py
   ```

7. **Open in your browser**
   Go to:
   [http://localhost:5000](http://localhost:5000)
   You can now add, update, or delete swimmers via the web interface.

---

## API Endpoints (Test with `curl`)

### Get all swimmers

```bash
curl http://127.0.0.1:5000/results
```

### Add new swimmer

```bash
curl -X POST http://127.0.0.1:5000/results \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Anna","last_name":"Smith","sex":"F","age_group":12,"event":"100m Freestyle","date":"2025-05-20","time":"00:01:23"}'
```

### Get swimmer by ID

```bash
curl http://127.0.0.1:5000/results/1
```

### Get swimmers by age group

```bash
curl http://127.0.0.1:5000/results/age/12
```

### Get all girls

```bash
curl http://127.0.0.1:5000/results/girls
```

### Get all boys

```bash
curl http://127.0.0.1:5000/results/boys
```

### Update swimmer by ID

```bash
curl -X PUT http://127.0.0.1:5000/results/1 \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Sofia","last_name":"Potter","sex":"F","age_group":13,"event":"200m IM","date":"2025-05-25","time":"00:02:05"}'
```

### Delete swimmer by ID

```bash
curl -X DELETE http://127.0.0.1:5000/results/1
```
## References

1. Course materials and lectures created by Andrew Beatty
   [https://github.com/andrewbeattycourseware/wsaa-courseware](https://github.com/andrewbeattycourseware/wsaa-courseware)

3. W3school HTML tutorial
    [https://www.w3schools.com/html/](https://www.w3schools.com/html/)   

4. HTML Tables
    [https://www.geeksforgeeks.org/html-tables/](https://www.geeksforgeeks.org/html-tables/)


2. MySQL 8.4 Documentation – DROP DATABASE
   [https://dev.mysql.com/doc/refman/8.4/en/drop-database.html](https://dev.mysql.com/doc/refman/8.4/en/drop-database.html)

3. Stack Overflow – Make a dictionary from separate lists of keys and values
   [https://stackoverflow.com/questions/209840/make-a-dictionary-dict-from-separate-lists-of-keys-and-values](https://stackoverflow.com/questions/209840/make-a-dictionary-dict-from-separate-lists-of-keys-and-values)

4. Stack Overflow – How can I set max length in an HTML5 input type="number" element?
   [https://stackoverflow.com/questions/8354975/how-can-i-set-max-length-in-an-html5-input-type-number-element](https://stackoverflow.com/questions/8354975/how-can-i-set-max-length-in-an-html5-input-type-number-element)

5. Stack Overflow – How to clear radio button in JavaScript
   [https://stackoverflow.com/questions/2554116/how-to-clear-radio-button-in-javascript](https://stackoverflow.com/questions/2554116/how-to-clear-radio-button-in-javascript)




