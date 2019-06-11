import dbinterface

welcomeMenu = """
Please log in or create new account:
1.	Log In
2.	Create new account
0.	Exit
"""

def checkAccountType():
	return

def createNewAccount():
	return

def main():
	while(True):
		print(welcomeMenu)
		sel = int(input("Menu Option >> "))
		if sel == 1:
			result = checkAccountType()
			if 0 in result:
				visitor.main()
			elif 1 in result:
				employee.main()
			elif 2 in result:
				admin.main()
		elif sel == 2:
			createNewAccount()
		elif sel == 0:
			break
        else:
            print("Unrecognized Command")

# Only run the main method if this was the script that was run
if __name__ == "__main__":
    main()