# Healthbot_EPICS
EPICS project 
For accessing the healthbase ie the database of users please do extract all the files from healthbase.zip and then be sure to install postgresql in your pc.After that please do create a database named user_info and in the tables section run the following query-
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    age INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Then simply put your login credentials on the html page and the user data will be saved in the database.
