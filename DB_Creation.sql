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

--------------------------------------------------------------------------------
----------------- 2. Employee -----------------------------------
IF OBJECT_ID('Employee', 'U') IS NOT NULL
   BEGIN
		PRINT 'Employee TABLE ALREADY EXISTS'
   END
ELSE
   BEGIN
		CREATE TABLE Employee(
		  Emp_ID Integer IDENTITY(1,1) NOT NULL PRIMARY KEY,
		  username varchar(40) NOT NULL UNIQUE,
		  upassword varchar(10) NOT NULL CHECK(len(upassword)<=10),
		  Emp_firstName varchar(200) NOT NULL,
		  Emp_lastName varchar(200) NOT NULL,
		  Emp_Title varchar(200) NOT NULL, 
		  Emp_Phone Integer NOT NULL UNIQUE,
		  Emp_Email varchar(100) NOT NULL
		)
   END
--------------------------------------------------------------------------------
--------------------------- 3. Vehicle ---------------------------------------
IF OBJECT_ID('Vehicle', 'U') IS NOT NULL
   BEGIN
		PRINT 'Vehicle TABLE ALREADY EXISTS'
   END
ELSE
   BEGIN
		CREATE TABLE Vehicle(
            VerificationIN Integer IDENTITY(1000,1) NOT NULL PRIMARY KEY,
            Cust_ID Integer NOT NULL FOREIGN KEY REFERENCES Customer(Cust_ID),
            ProducedBy varchar(20),
            ModelNo varchar(20),
            Year Integer NOT NULL CHECK(len(Year)=4),
            EngineDetails varchar(200),
            Trim varchar(200),
            V_Exterior varchar(200),
            V_Interior varchar(200),
            Body_Condition varchar(200),
            Frame_Condition varchar(200),
            Interior_Condition varchar(200),
            Engine_Condition varchar(200),
		  )
   END
-----------------------------------------------------------------------------------
---------------- Table 4. Customization----------------------------
----------Plan Id: start:100 -------------------------------
IF OBJECT_ID('Customization_Detail', 'U') IS NOT NULL
   BEGIN
		PRINT ' Customization_Detail TABLE ALREADY EXISTS'
   END
ELSE
   BEGIN
		CREATE TABLE Customization_Detail(
		  Plan_ID Integer IDENTITY(100,1) NOT NULL PRIMARY KEY,
        Cust_ID Integer NOT NULL FOREIGN KEY REFERENCES Customer(Cust_ID),      
		  VerificationIN Integer NOT NULL FOREIGN KEY REFERENCES Vehicle(VerificationIN),  
		  Emp_ID Integer NOT NULL FOREIGN KEY REFERENCES Employee(Emp_ID),  
		  )
   END
-----------------------------------------------------------------------------------
---------------- Table 5. Customization Plan ----------------------------
IF OBJECT_ID('Customization_Plan', 'U') IS NOT NULL
   BEGIN
		PRINT ' Customization_Plan TABLE ALREADY EXISTS'
   END
ELSE
   BEGIN
		CREATE TABLE Customization_Plan(
		  Plan_ID Integer NOT NULL FOREIGN KEY REFERENCES Customization_Detail(Plan_ID) PRIMARY KEY, 
          TE_price money,
          Amount_Deposited money,
          startDate date,
          Estimated_DeliveryDate date,
          subtotal_price money,
          tax_amount money,
          Amount_due money,
          Payment_method varchar(100),
          Status varchar(20),
          Payment_date date,
          current_PhotoID Integer IDENTITY(2000,1) NOT NULL,
          Photo_links varchar(50) 
		  )
   END

---------------------------------------------------------------------
-------------------------- 6. Questionnaire  ------------------------------
----------------Questionnaire  ID Start: 1 ---------------------------
IF OBJECT_ID('Questionnaire ', 'U') IS NOT NULL
   BEGIN
		PRINT 'Questionnaire TABLE  ALREADY EXISTS'
   END
ELSE
   BEGIN
		CREATE TABLE Questionnaire(
			Question_No Integer IDENTITY(1,1) NOT NULL,
            Plan_ID Integer NOT NULL FOREIGN KEY REFERENCES Customization_Detail(Plan_ID), 
            PRIMARY KEY(Plan_ID, Question_No),
            Question_Date Date,
            Question_Desp varchar(500) NOT NULL,
            Question_Ans varchar(500)
	  )
   END

--------------------------------------------------------------------------------
------------------------- 7. Item ----------------------------------------
------------------- ItemID start at 57000-----------------------------------
IF OBJECT_ID('Item', 'U') IS NOT NULL
   BEGIN
		PRINT ' Item TABLE ALREADY EXISTS'
   END
ELSE
   BEGIN
		CREATE TABLE Item(
		  Item_ID Integer IDENTITY(57000,1) NOT NULL PRIMARY KEY,
          Plan_ID Integer NOT NULL FOREIGN KEY REFERENCES Customization_Detail(Plan_ID),
          Emp_ID Integer NOT NULL FOREIGN KEY REFERENCES Employee(Emp_ID),
          Item_name varchar(50) NOT NULL,
          Item_Desp varchar(100) NOT NULL,
          Item_EP money,
          Item_CompEstimation Integer,
          Item_actual_parts_cost money,
          Item_actual_labor_cost money,
		  )
   END
------------------------------------------------------------------------------
------------------------- 8. Part   ----------------------------------------
------------------- Part_ID start at 1000-----------------------------------
IF OBJECT_ID('Part ', 'U') IS NOT NULL
   BEGIN
		PRINT ' Part  TABLE ALREADY EXISTS'
   END
ELSE
   BEGIN
		CREATE TABLE Part (
		    Part_ID Integer IDENTITY(1000,1) NOT NULL PRIMARY KEY,
          part_manufacture varchar(30),
          part_price money,
		  )
   END
-----------------------------------------------------------------------------------------
------------------------- 9. Part_Details ----------------------------------------
IF OBJECT_ID('Part_Details', 'U') IS NOT NULL
   BEGIN
		PRINT ' Part_Details TABLE ALREADY EXISTS'
   END
ELSE
   BEGIN
		CREATE TABLE Part_Details(
		    Part_ID Integer NOT NULL FOREIGN KEY REFERENCES Part(Part_ID),
          Item_ID Integer NOT NULL FOREIGN KEY REFERENCES Item(Item_ID),
          PRIMARY KEY(Part_ID,Item_ID),
          part_quantity Integer,
          part_total_cost money,
		  )
   END
-----------------------------------------------------------------------------------------
------------------------- 10. Labor  ----------------------------------------
------------------- Labor start at 62000-----------------------------------
IF OBJECT_ID('Labor ', 'U') IS NOT NULL
   BEGIN
		PRINT ' Labor TABLE ALREADY EXISTS'
   END
ELSE
   BEGIN
		CREATE TABLE Labor (
		    labor_ID Integer IDENTITY(62000,1) NOT NULL PRIMARY KEY,
          labor_Desp varchar(30),
          labor_cost money,
		  )
   END
-----------------------------------------------------------------------------------------
------------------------- 11. Labor_Details  ----------------------------------------
------------------- Labor_Details start at 62000-----------------------------------
IF OBJECT_ID('Labor_Details ', 'U') IS NOT NULL
   BEGIN
		PRINT ' Labor_Details  TABLE ALREADY EXISTS'
   END
ELSE
   BEGIN
		CREATE TABLE Labor_Details (
		    labor_ID Integer NOT NULL FOREIGN KEY REFERENCES Labor(labor_ID),
          Item_ID Integer NOT NULL FOREIGN KEY REFERENCES Item(Item_ID),
          PRIMARY KEY(labor_ID,Item_ID),
          labor_time time,
          labor_employee varchar(30),
          labor_total_cost money,
		  )
   END
-----------------------------------------------------------------------------------------
