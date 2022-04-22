""" This file have all queries to run on database TITANENROLLDB"""
""" All functions will be called and run the query"""

# pyodbc is the module to connect to sql server
import pyodbc as connector
#connection string with needed information
""" The server name will be differ for all partners"""
connection_string=(r"Driver={SQL Server};"
               r"Server=LTCSUF-24KH0B3\SQLEXPRESS;" # please change this to your server--> run 'select @@SERVERNAME' in sql studio to find your server
               r"Database=JOESCHOPS;"
               r"Trusted_Connection=yes;")

#connect to the server and database under that server
conn= connector.connect(connection_string)

#create a cursor to work on the database
cur=conn.cursor()

##Login
# To authenticate user credentials - read from employee, customer data
def authenticateUser(username,password):
      if username=="" or password=="":
         return False
      else:
         cur.execute(f"""SELECT Customer.Cust_ID FROM Customer WHERE username='{username}' AND upassword='{password}'""")
         customer=[]
         for i in cur:
            customer.append(i)
            if not customer:
               cur.execute(f"""SELECT Employee.Emp_ID FROM Employee WHERE username='{username}' AND upassword='{password}'""")
               employee = []
               for k in cur:
                  employee.append(i)
                  if not employee:
                     return False
                  else:
                     return employee[0]
            else:
               return customer[0] # customer ID

# Insert entry into Customer table
def createCustomer(fName, lName, mobile, email,uname, upswd, address, city, state, zip):
   if uname=="" or upswd=="" or fName=="" or lName=="" or mobile=="" or email=="" or address=="" or city=="" or zip=="":
         return False
      else:
         cur.execute(f"""INSERT into Customer values ({fName},{lName},{mobile},{email},{uname},{upswd},{address},{city},{state},{zip})""")
         print("Successfully inserted row into customer table")
         return True

##Customer
#Insert data into vehicle table
def StoreVehicleInfo(custId, producedBy, ModelNo, year, engineDet, Tirm, exterior, interior, bodyC, frameC, interC, engC):
   if custId=="" or year=="":
         return False
      else:
         cur.execute(f"""INSERT into Vehicle values ({custId},{producedBy},{ModelNo},{year},{engineDet},{Tirm},{exterior},{interior},{bodyC},{frameC},{interC},{engC})""")
         print("Successfully inserted data into vehicle table")
         return True

#Dropdown values to show available employees
def lisOfAllEmployees():
   cur.execute(f"""select Employee.Emp_firstName+Employee.Emp_lastName from Employee""")
   employeeData=[]
   for i in cur:
      employeeData.append(i)
   
   return employeeData # array with all employee names

#Store details about Customisation
def StoreCustomisationDetails(custId, empName, itemName, itemdesp):
   if custId==""
      return False
   else:
      cur.execute(f"""select Employee.Emp_ID from Employee where Employee.Emp_firstName+Employee.Emp_lastName={empName}""")
      empID=cur[0]

      cur.execute(f"""select Vehicle.VerificationIN from Vehicle where Vehicle.Cust_ID={custId}""")
      vIn=cur[0]

      #store data in Customization_Detail
      cur.execute(f"""insert into Customization_Detail values({custId},{vIn},{empID})""")

      cur.execute(f"""select Plan_ID from Customization_Detail where Cust_ID={custId}""")
      planId = cur[0]

      cur.execute(f"""insert into Item values({planId},{empID},{itemName},{itemdesp},400.96,150,100,150)""")
      print("Successfully inserted data into customization and item tables")
      return True
  
#Display PlanId
def DisplayPlanId(custId):
   if custId==""
      return False
   else:
      cur.execute(f"""select Plan_ID from Customization_Detail where Cust_ID={custId}""")
      return cur[0]

#Store Questions
def StoreQuestions():
   