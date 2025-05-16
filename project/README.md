
1. clone the current repository locally (`git clone git@github.com:Kate-217/WSAA-coursework.git`)
2. rename db_config.py_template to db_config.py
3. change host, user, password in db_config.py to let the app connect to your local MySQL database server
4. pip install -r requirements.txt 
5. python project/create_db.py - note, that this requires the user to have global privileges (DROP and CREATE on schema level) to be able to drop and create databases.
5. python project/app.py
7. open localhost:5000 in your web browser. You can add/edit/delete swimmers