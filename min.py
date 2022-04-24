# base Class of your App inherits from the App class.
from kivy.app import App
# GridLayout arranges children in a matrix.
from kivy.uix.gridlayout import GridLayout
# Label is used to label something
from kivy.uix.label import Label
# used to take input from users
from kivy.uix.textinput import TextInput
from db import *

class LS(GridLayout):
    def __init__(self,**var_args):
        
        print(authenticateUser('Jeevika','abcd',True))
        print(authenticateUser('Chao123','xyz',False))
        #createCustomer('Hsini','Li',91199399,'wyz@gmail.com','h1ni','ab','Fulerton','Fullerton','CA',92831)
        # StoreVehicleInfo(80000000,'Sonic','1234A',1996,'LPW Naturally Aspirated Engines 2, 3 & 4 Cylinder Configurations ',
		# 					'SEL','Car Wash','Seat Adjustment','Average','New', 'Average', 'Average')
        lisOfAllEmployees()
        # StoreCustomisationDetails(80000000,'WuChao','Paint','Paint the car')
        print(DisplayPlanId(80000000))
        StoreQuestions(80000000,'2022-07-03','Whats the progress')
        #initialPayment(80000000,200,'2022-04-24')
        print(returnTotalPrice(80000000))
        print(getEmployeeCustomisations(5))
        #UpdateDB(5,'https://varcahr','2022-09-10')
        print(Questions(5))
        UpdateQuestionsAns(5,1003,'Created')
        print(DisplayAnswers(80000000))
        #DeleteVehicle(5)
        print(searchData(1104))
        


# the Base Class of our Kivy App
class MyApp(App):
	def build(self):
		# return a LoginScreen() as a root widget
		return LS()


if __name__ == '__main__':
	MyApp().run()
