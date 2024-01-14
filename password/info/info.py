from password import passwords
class Info:
    def __init__(self):
        self.authenticate()
    def authenticate(self):
        while True:
            x = int(input("Enter your password: "))
            if x in passwords.list:
                print("Welcome Aboard")
                break
            else:
                passwords.entering_numbers -= 1
                print(f"Remaining login attempts: {passwords.entering_numbers}")

                if passwords.entering_numbers == 0:
                    print("You have made 3 incorrect login attempts, the program is closing")
                    break