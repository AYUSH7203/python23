import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor()

mycursor.execute('create database if not exists banking_system')

mydb = pymysql.connect(host='localhost',user='root',password='',database='banking_system')
mycursor = mydb.cursor()

mycursor.execute('create table if not exists bank(emp_id int , emp_name varchar(20) , email_id varchar(20) , mobile varchar(11) , password varchar(12))')
mydb.commit()

mycursor.execute('create table if not exists customer(acno int primary key , first_name varchar(20) , last_name varchar(20) , mobile varchar(12) , email varchar(30) , password varchar(20), balance int)')
mydb.commit()

mycursor.execute('create table if not exists customer_balance(acno int , balance int ,password varchar(20))')    
mydb.commit()