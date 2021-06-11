
# Parent Class
class User:
    Name = "Name"
    Email = "Email"
    Password = "Password"

    def getLoginInfo(self):
        entry_name = input("Enter name here")
        entry_email = input("Enter email here")
        entry_password = input("Enter password here")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome to the forum, {}!".format(entry_name))
        else:
            print("Invalid credentials, please try again or contact support.")

# child class 
class Normal_user(User):
    screen_name = "User selected"
    award_points = 0 #user could earn/buy points to show other users that they especially enjoy their content
    time_online = 0 #This would be calculated by the program as amount of time user has spent on the forum

    #getLoginInfo function polymorphs from parent class
    #Normal_user class has no email and instead has a screen name as a login credential
    def getLoginInfo(self):
        entry_screen_name = input("Enter username here")
        entry_password = input("Enter password here")
        if (entry_screen_name == self.screen_name and entry_password == self.password):
            print("Welcome to the forum, {}!".format(screen_name))
        else:
            print("Invalid credentials, please try again or contact us at help@forum.com.")

    
# another child class
class Admin(User):
    admin_name = "User selected"
    admin_seniority = 1 #This could be increased with length of time as an admin, granting additional privileges
    admin_pin = "User selected"

    #getLoginInfo function polymorphs from parent class
    #Admin has a pin number in addition to email and password for added security
    def getLoginInfo(self):
        entry_name = input("Enter name here")
        entry_email = input("Enter email here")
        entry_pin = input("Enter PIN here")
        entry_password = input("Enter password here")
        if (entry_email == self.email and entry_password == self.password and entry_pin == self.admin_pin):
            print("Welcome back, admin {}!".format(admin_name))
        else:
            print("Invalid credentials, please try again or contact support.")
    
                  
