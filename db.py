""" This file have all queries to run on database TITANENROLLDB"""
""" All functions will be called and run the query"""

# pyodbc is the module to connect to sql server
# connection string with needed information
""" The server name will be differ for all partners"""
from locale import currency
import pyodbc as connector
connection_string = (r"Driver={ODBC Driver 17 for SQL Server};"
                     r"Server=localhost;"
                     r"PORT=1443;"
                     r"Database=JOESCHOPS;"
                     r"UID=sa;"
                     r"PWD=Strong.Pwd-123;")

# connection_string=(r"Driver={SQLite3 ODBC Driver;"
#                r"Server=SQLite3 ODBC Driver;" # please change this to your server--> run 'select @@SERVERNAME' in sql studio to find your server
#                r"Database=database.db;"
#                r"Trusted_Connection=yes;")

# connect to the server and database under that server
conn = connector.connect(connection_string)

# create a cursor to work on the database
cur = conn.cursor()

# To authenticate user credentials


# Login
# To authenticate user credentials - read from employee, customer data
def authenticateUser(username, password):
    if username == "" or password == "":
        return None
    else:
        cur.execute(
            f"""SELECT Customer.Cust_ID FROM Customer WHERE username='{username}' AND upassword='{password}'""")
        customer = []
        for i in cur:
            customer.append(i)
            if not customer:
                cur.execute(
                    f"""SELECT Employee.Emp_ID FROM Employee WHERE username='{username}' AND upassword='{password}'""")
                employee = []
                for k in cur:
                    employee.append(i)
                    if not employee:
                        return None
                    else:
                        return employee[0]
            else:
                return customer[0]  # customer ID

# Insert entry into Customer table


def createCustomer(fName, lName, mobile, email, uname, upswd, address, city, state, zip):
    if uname == "" or upswd == "" or fName == "" or lName == "" or mobile == "" or email == "" or address == "" or city == "" or zip == "":
        return False
    else:
        cur.execute(
            f"""INSERT into Customer values ('{fName}','{lName}',{mobile},'{email}','{uname}','{upswd}','{address}','{city}','{state}',{zip})""")
        cur.commit()
        print("Successfully inserted row into customer table")
        return True

# Customer
# Insert data into vehicle table


def StoreVehicleInfo(custId, producedBy, ModelNo, year, engineDet, Tirm, exterior, interior, bodyC, frameC, interC, engC):
    if custId == "" or year == "":
        return False
    else:
        str = f"""INSERT into Vehicle values ({custId},'{producedBy}','{ModelNo}',{year},'{engineDet}','{Tirm}','{exterior}','{interior}','{bodyC}','{frameC}','{interC}','{engC}')"""
        print(str)
        cur.execute(
            f"""INSERT into Vehicle values ({custId},'{producedBy}','{ModelNo}',{year},'{engineDet}','{Tirm}','{exterior}','{interior}','{bodyC}','{frameC}','{interC}','{engC}')""")
        print("Successfully inserted data into vehicle table")
        return True

# Dropdown values to show available employees


def lisOfAllEmployees():
    cur.execute(
        f"""select Employee.Emp_firstName+Employee.Emp_lastName from Employee""")
    employeeData = []
    for i in cur:
        employeeData.append(i)

    return employeeData  # array with all employee names

# Store details about Customisation


def StoreCustomisationDetails(custId, empName, itemName, itemdesp):
    if custId == "":
        return False
    else:
        cur.execute(
            f"""select Employee.Emp_ID from Employee where Employee.Emp_firstName+Employee.Emp_lastName={empName}""")
        empID = cur[0]

        cur.execute(
            f"""select Vehicle.VerificationIN from Vehicle where Vehicle.Cust_ID={custId}""")
        vIn = cur[0]

        # store data in Customization_Detail
        cur.execute(
            f"""insert into Customization_Detail values({custId},{vIn},{empID})""")

        cur.execute(
            f"""select Plan_ID from Customization_Detail where Cust_ID={custId}""")
        planId = cur[0]

        cur.execute(
            f"""insert into Item values({planId},{empID},'{itemName}','{itemdesp},400.96,150,100,150)""")
        print("Successfully inserted data into customization and item tables")
        return True

# Display PlanId


def DisplayPlanId(custId):
    if custId == "":
        return False
    else:
        query = f"""select Plan_ID from Customization_Detail where Cust_ID={custId}"""
        print(query)
        cur.execute(query)
        for i in cur:
            return i

# Search with PlanID - customer


def searchData(planId):
    cur.execute(f"""select Status,Estimated_DeliveryDate,Amount_due,Photo_links,Item.Item_name,Item.Item_Desp from Customization_Plan
     inner JOIN Item on Customization_Plan.Plan_ID={planId} and Item.Plan_ID={planId}""")

    searchData = []

    for i in cur:
        searchData.append(i)

    return searchData  # returns array

# Store Questions


def StoreQuestions(custId, date, question):  # date should be a string
    if custId == "":
        return False
    else:
        planId = DisplayPlanId(custId)
        cur.execute(
            f"""insert into Questionnaire values({custId},{date},{question},null)""")
        print("Successfully inserted data into Questionarrie")
        return True

# # Store the initial deposit


# def initialPayment(custId, depositAmt, date):

#     if custId == "":
#         return False
#     else:
#         planId = DisplayPlanId(custId)
#         cur.execute(
#             f"""insert into Customization_Plan values({planId},600.29,{depositAmt},{date},'2022-08-02',440.16,20.16,600.29-{depositAmt},'Card','Created',{date},null)""")
#         print("inserted data into plan")
#         return True

# Return total price


def returnTotalPrice(custId):
    if custId == "":
        return False
    else:
        planId = DisplayPlanId(custId)
        print(planId)
        cur.execute(
            f"""select TE_price from Customization_Plan where Plan_ID={planId[0]}""")
        price = []
        for i in cur:
            price.append(i)

        return price[0]

# Display customizations for employee


def getEmployeeCustomisations(empId):
    if empId == "":
        return False
    else:
        cur.execute(
            f"""select Plan_ID from Customization_Detail where Emp_ID={empId}""")
        empPland = []
        for i in cur:
            empPland.append(i)
        print(empPland[0])
        print(empId)
        query = f"""select Item.Plan_ID,Item.Item_ID,Item.Item_name,Item.Item_Desp,Customization_Plan.TE_price,Customization_Plan.Amount_Deposited,Customization_Plan.Estimated_DeliveryDate,Customization_Plan.Amount_due,Customization_Plan.Status from Customization_Plan,Item where Customization_Plan.Plan_ID={empPland[0][0]} and Item.Emp_ID={empId}"""
        print(query)
        cur.execute(query)
        return cur  # returns the complete data in array format might be in ()

# Update photo link, delivery date


def UpdateDB(empId, photoLink, DeliveryDate):
    cur.execute(
        f"""select Plan_ID from Customization_Detail where Emp_ID={empId}""")
    empPland = []
    for i in cur:
        empPland.append(i)
    if photoLink == "" and DeliveryDate != "":
        cur.execute(
            f"""update Customization_Plan set Estimated_DeliveryDate={DeliveryDate} where Plan_ID={empPland[0]}""")
        print("Successfully updated delivery date")
    elif photoLink != "" and DeliveryDate == "":
        cur.execute(
            f"""update Customization_Plan set Photo_links={photoLink} where Plan_ID={empPland[0]}""")
        print("Successfully updated photo link")
    elif photoLink != "" and DeliveryDate != "":
        cur.execute(
            f"""update Customization_Plan set Estimated_DeliveryDate={DeliveryDate},Photo_links={photoLink} where Plan_ID={empPland[0]}""")
        print("Successfully updated both")

    return True

# display questions to employee


def Questions(empId):
    cur.execute(
        f"""select Plan_ID from Customization_Detail where Emp_ID={empId}""")
    empPland = []
    for i in cur:
        empPland.append(i)

    cur.execute(
        f"""select Question_No,Question_Desp from Questionnaire where Plan_ID={empPland[0]}""")
    return cur  # returns an array of questions

# Update question answers


def UpdateQuestionsAns(empId, quesNo, quesAns):
    cur.execute(
        f"""select Plan_ID from Customization_Detail where Emp_ID={empId}""")
    empPland = []
    for i in cur:
        empPland.append(i)

    cur.execute(
        f"""update Questionnaire set Question_Ans={quesAns} where Question_No={quesNo} and Plan_ID={empPland[0]}""")
    print("Updated question answers")

# display answers to customers


def DisplayAnswers(custId):
    planId = DisplayPlanId(custId)
    cur.execute(
        f"""select Question_No, Question_Desp, Question_Ans from Questionnaire where Plan_ID={planId}""")
    ans = []
    for i in cur:
        ans.append(i)

    return ans  # array

# delete vehicle details


def DeleteVehicle(empId):
    cur.execute(
        f"""select Plan_ID from Customization_Detail where Emp_ID={empId}""")
    empPland = []
    for i in cur:
        empPland.append(i)

    cur.execute(
        f"""delete from Customization_Plan where Plan_ID={empPland[0]}""")
    cur.execute(f"""delete from Questionnaire where Plan_ID={empPland[0]}""")
    cur.execute(f"""delete from Item where Plan_ID={empPland[0]}""")

    cur.execute(
        f"""select VerificationIN from Customization_Detail where Emp_ID={empId}""")
    for i in cur:
        vIn.append(i)

    cur.execute(
        f"""delete from Customization_Detail where VerificationIN={vIn[0]}""")
    cur.execute(f"""delete from Vehicle where VerificationIN={vIn[0]}""")
