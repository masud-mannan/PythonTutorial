class user:
    name = ''
    email = ''
    password = ''
    login = False

    def login(self):
        name = input("Enter your name ")
        password = input("Enter your password ")

        if(name == self.name and password == self.password):
            self.login = True
            print("Login Successfully")
        else:
            print("Login Failed")

    def logout(self):
        self.login = False
        print("Logged out")

    def isLogin(self):
        if(self.login):
            return True
        else:
            return False

    def profile(self):
        if(self.isLogin()):
            print(self.name, "\n", self.email)
        else:
            print("User Not Looed in")

user1 = user()

user1.name = "Masud"
user1.password = "hello"
user1.email = "mannan@gmail.com"

user1.login()
user1.profile()




