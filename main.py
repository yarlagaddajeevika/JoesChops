from distutils.log import error
from email import message
from http.client import FOUND
import db
from flask import Flask, render_template, url_for, request, redirect, Response, session, escape

app = Flask(__name__)
app.secret_key = '(G+KbPeShVmYq3t6w9z$C&E)H@McQfTjWnZr4u7x!A%D*G-JaNdRgUkXp2s5v8y/'

# Web Views


@app.route('/')
def index():
    print(session)
    return render_template('home.html')


@app.route('/cuslogin', methods=['POST', 'GET'])
def cuslogin():
    if request.method == "POST":
        session.pop('username', None)
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        rt = db.authenticateCus(username, password)
        if rt is None:
            return render_template('home.html', message="Login failed.")

        customer_id = rt
        print(username)
        print(password)
        print(customer_id)

    else:
        return render_template('home.html', message="Login failed.")
    return render_template('home.html', message=customer_id)


@app.route('/emplogin', methods=['POST', 'GET'])
def emplogin():
    if request.method == "POST":
        session.pop('username', None)
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        rt = db.authenticateEmp(username, password)
        if rt is None:
            return render_template('home.html', message="Login failed.")

        print(username)
        print(password)
    else:
        return render_template('home.html', message="Login failed.")
    return render_template('home.html', message="Login Successfuly.")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        firstname = request.form.get('new_firstname', None)
        lastname = request.form.get('new_lasttname', None)
        phone = request.form.get('new_phone', None)
        email = request.form.get('new_email', None)
        address = request.form.get('new_address', None)
        city = request.form.get('new_city', None)
        state = request.form.get('new_state', None)
        zip = request.form.get('new_zip', None)
        username = request.form.get('new_username', None)
        password = request.form.get('new_password', None)
        db.createCustomer(firstname, lastname, phone, email,
                          username, password, address, city, state, zip)
        return render_template('home.html', message="Register Successfully.")
    return render_template('home.html', message="Register Fail.")


@app.route('/vehicleInput', methods=['POST', 'GET'])
def vehicleInput():
    if request.method == "POST":
        id = request.form.get('new_id', None)
        brand = request.form.get('new_brand', None)
        model = request.form.get('new_model', None)
        year = request.form.get('new_year', None)
        engine = request.form.get('new_engine', None)
        trim = request.form.get('new_trim', None)
        interior = request.form.get('new_interior', None)
        exterior = request.form.get('new_exterior', None)
        condition = request.form.get('new_condition', None)
        frame = request.form.get('new_frame', None)
        interiorCon = request.form.get('new_interiorCon', None)
        engineCon = request.form.get('new_engineCon', None)
        db.StoreVehicleInfo(id, brand, model, year, engine, trim,
                            interior, exterior, condition, frame, interiorCon, engineCon)
        return render_template('vehicle.html', message="Register Successfully.")
    return render_template('vehicle.html', message="Fail.")


@app.route('/searchEmp')
def searchEmp():
    str = db.lisOfAllEmployees()
    print(str)
    return render_template('customization.html', message=str)


@app.route('/customize', methods=['POST', 'GET'])
def customize():
    if request.method == "POST":
        id = request.form.get('custID', None)
        empName = request.form.get('empName', None)
        itemName = request.form.get('itemName', None)
        itemDescri = request.form.get('itemDescri', None)
        print(id)
        print(empName)
        print(itemName)
        print(itemDescri)
        db.StoreCustomisationDetails(id, empName, itemName, itemDescri)
        return render_template('customization.html', message="Submit Successfully.")
    return render_template('customization.html', message="Fail.")


@app.route('/getPlanid', methods=['POST', 'GET'])
def getPlanid():
    if request.method == "POST":
        planID = request.form.get('planID', None)
        str = db.searchData(planID)
        return render_template('cusReport.html', message=str)
    return render_template('cusReport.html', message="Fail.")


@app.route('/inputQuestions', methods=['POST', 'GET'])
def inputQuestions():
    if request.method == "POST":
        cusID = request.form.get('custID', None)
        date = request.form.get('date', None)
        questions = request.form.get('questions', None)
        print(cusID)
        print(date)
        print(questions)

        db.StoreQuestions(cusID, date, questions)
        return render_template('cusReport.html', message="Submit Successfully.")
    return render_template('cusReport.html', message="Fail.")


@app.route('/getTotal', methods=['POST', 'GET'])
def getTotal():
    if request.method == "POST":
        custID = request.form.get('custID', None)
        print(custID)
        print("call")
        price = db.returnTotalPrice(custID)

        return render_template('billing.html', message=price)
    return render_template('billing.html', message="Fail.")


@app.route('/getEmpid', methods=['POST', 'GET'])
def getEmpid():
    if request.method == "POST":
        empID = request.form.get('empID', None)
        result = db.getEmployeeCustomisations(empID)
        return render_template('showPlan.html', message=result)
    return render_template('showPlan.html', message="Fail.")


@app.route('/update', methods=['POST', 'GET'])
def updateDB():
    if request.method == "POST":
        empID = request.form.get('empID', None)
        link = request.form.get('link', None)
        date = request.form.get('date', None)
        db.UpdateDB(empID, link, date)
        return render_template('updateProgress.html', message="Update Successfully")
    return render_template('updateProgress.html', message="Fail.")


@app.route('/getQuestion', methods=['POST', 'GET'])
def getQuestion():
    if request.method == "POST":
        empID = request.form.get('empID', None)
        questions = db.Questions(empID)
        return render_template('ansQuestions.html', message=questions)
    return render_template('ansQuestions.html', message="Fail.")


@app.route('/ansQuestion', methods=['POST', 'GET'])
def ansQuestion():
    if request.method == "POST":
        empID = request.form.get('empID', None)
        quesNo = request.form.get('quesNo', None)
        quesAns = request.form.get('quesAns', None)
        db.UpdateQuestionsAns(empID, quesNo, quesAns)
        return render_template('ansQuestions.html', message="Update Successfully")
    return render_template('ansQuestions.html', message="Fail.")


@app.route('/getAns', methods=['POST', 'GET'])
def getAns():
    if request.method == "POST":
        custID = request.form.get('custID', None)
        ans = db.DisplayAnswers(custID)
        return render_template('cusReport.html', message=ans)
    return render_template('cusReport.html', message="Fail.")


@app.route('/deleteV', methods=['POST', 'GET'])
def deleteV():
    if request.method == "POST":
        empID = request.form.get('empID', None)
        db.DeleteVehicle(empID)
        return render_template('delete.html', message="Delete Successfully")
    return render_template('delete.html', message="Fail.")


@app.route('/customer')
def customer():
    return render_template('customer.html')


@app.route('/vehicle')
def vehicle():
    return render_template('vehicle.html')


@app.route('/customization')
def customization():
    return render_template('customization.html')


@app.route('/payment')
def payment():
    return render_template('payment.html')


@app.route('/cusReport')
def cusReport():
    return render_template('cusReport.html')


@app.route('/billing')
def billing():
    return render_template('billing.html')


@app.route('/employee')
def employee():
    return render_template('employee.html')


@app.route('/showPlan')
def showPlan():
    return render_template('showPlan.html')


@app.route('/updateProgress')
def updateProgress():
    return render_template('updateProgress.html')


@app.route('/ansQuestions')
def ansQuestions():
    return render_template('ansQuestions.html')


@app.route('/delete')
def delete():
    return render_template('delete.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
