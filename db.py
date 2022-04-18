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

### To authenticate user credentials
def authenticateUser(username,password):
      if username=="" or password=="":
         return False
      else:
         cur.execute(f"""SELECT Customer.Cust_ID FROM Customer WHERE username='{username}' AND upassword='{password}'""")
         customer=[]
         for i in cur:
            customer.append(i)
            if not customer:
               return False
            else:
               return customer[0]
