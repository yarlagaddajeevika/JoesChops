---------------------------------------------------------------
--------------CPSC-531-RDB15-PROJECT-JOESCHOPS--------------
---------------------------------------------------------------
-----------------INITIAL DATABASE CREATION--------------------

---------------CREATE DATABASE - JOESCHOPS------------
IF NOT EXISTS(SELECT name FROM sys.databases WHERE name='JOESCHOPS')
     BEGIN
	   CREATE DATABASE JOESCHOPS
	 END
GO
  USE JOESCHOPS
GO

---------------------------------------------------------------
------------------ CREATE TABLES ---------------------------
---------------------------------------------------------------
----------------------- 1. Customer -------------------------------------------
----------------Customer ID Start: 80000000 ---------------------------
IF OBJECT_ID('Customer', 'U') IS NOT NULL
   BEGIN
		PRINT 'Customer TABLE ALREADY EXISTS'
   END
ELSE
   BEGIN
		CREATE TABLE Customer(
		  Cust_ID Integer IDENTITY(80000000,1) NOT NULL PRIMARY KEY,
		  Cust_firstame varchar(50) NOT NULL, 
		  Cust_lastname varchar(50) NOT NULL, 
		  Cust_Phone Integer NOT NULL UNIQUE,
		  Cust_Email varchar(100) NOT NULL UNIQUE, 
          username varchar(40) NOT NULL UNIQUE,
		  upassword varchar(10) NOT NULL CHECK(len(upassword)<=10),
		  Address varchar(40) NOT NULL UNIQUE, 
		  City varchar(20) NOT NULL,
		  State varchar(20) NOT NULL,
		  zip Integer NOT NULL
		  )
   END

INSERT into Customer values ('Jeevika','Yarlagadda',999999999,'abc@gmail.com','jeevika','abcd','600 langsdorf','Fullerton','CA',92831)

select * from Customer

SELECT Customer.Cust_ID FROM Customer WHERE username='jeevika' AND upassword='abcd'