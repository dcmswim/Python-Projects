

#Parent class
class Employee:
    name = "Unknown" #input when employee is hired
    email = "Unknown" #created at time of hire
    Pay_scale = 0 #This would be adjusted accordingly in child classes
    Weekly_hours = 40 #This could also be adjusted accordingly for child classes
    bonus_eligible = False
    

#child class
class Manager(Employee):
    Pay_scale = 5
    Weekly_hours = 50
    bonus_eligible = True
    unlock_ID = 12345
    expense_allowance = 250.00


#another child class
class Driver(Employee):
    Pay_scale = 3
    Truck_ID = 9876
    CDL_license = "ABC"
    fuel_allocation = 100.00
