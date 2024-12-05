# Healthbot_EPICS
EPICS project 
<br>
For accessing the healthbase ie the database of users please do extract all the files from healthbase.zip and then be sure to install postgresql in your pc.After that please do create a database named user_info and in the tables section run the following query-
<br>
CREATE TABLE users (
<br>
    id SERIAL PRIMARY KEY,
    <br>
    name VARCHAR(100) NOT NULL,
    <br>
    email VARCHAR(100) UNIQUE NOT NULL,
    <br>
    password VARCHAR(255) NOT NULL,
    <br>
    gender VARCHAR(10) NOT NULL,
    <br>
    age INT NOT NULL,
    <br>
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
<br>
Then simply put your login credentials on the html page and the user data will be saved in the database.
