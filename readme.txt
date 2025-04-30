===============================
Flask REST API – Product Manager
===============================

This project is a REST API using Flask and MySQL to manage products (name, price, stock).
It includes CRUD operations and bulk actions.

-------------------------------
 Tech Stack:
-------------------------------
- Python 3
- Flask
- MySQL
- Postman (for testing)

-------------------------------
Installation Steps:
-------------------------------

1. Clone the repository (or download the files):

   git clone https://github.com/MichalisN-cmd/Rest-api-project
   cd flask-product-api

2. Install required Python packages:

   pip install flask mysql-connector-python

-------------------------------
MySQL Setup:
-------------------------------

1. Open MySQL Workbench (or any client)
2. Run the following SQL to create the database & table:

   CREATE DATABASE IF NOT EXISTS productdb;
   USE productdb;

   CREATE TABLE IF NOT EXISTS products (
     id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(100),
     price FLOAT,
     stock INT
   );

3. Edit your db.py file to match your MySQL credentials:

   db = mysql.connector.connect(
       host="localhost",
       user="your_username",
       password="your_password",
       database="productdb"
   )

-------------------------------
Running the API:
-------------------------------

In your terminal:

   python app.py

It will start at:

   http://127.0.0.1:5000

-------------------------------
API Endpoints:
-------------------------------

GET     /products              → List all products
GET     /products/<id>         → Get a product by ID
POST    /products              → Add a new product
POST    /products/bulk         → Add multiple products
PUT     /products/<id>         → Update a product
PUT     /products/<id>/stock   → Update only stock
DELETE  /products/<id>         → Delete a product by ID
DELETE  /products/all          → Delete all products


-------------------------------
GitHub Push Instructions:
-------------------------------

Run these commands from inside your project folder:

   git init
   git remote add origin https://github.com/yourusername/flask-product-api.git
   git add .
   git commit -m "Initial commit: Flask REST API"
   git branch -M main
   git push -u origin main

-------------------------------
Notes:
-------------------------------
- MySQL service must be running for the app to work
- Runs in development mode (not for production)
- For production use, consider deploying via gunicorn or Docker

-------------------------------
👨‍💻 Author:Michalis Nikolaou
-------------------------------
NikolaouM99@hotmail.com
