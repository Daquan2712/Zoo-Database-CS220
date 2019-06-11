
from projectzoodb import projectzooDB

# Create a database object that will handle all the DB stuff.
dbobj = projectzooDB()


def updateEmployeeInfo(FirstName,LastName,Gender,Address,City,State,Zipcode,DepartmentId,Email,Phone,SupervisorId,Salary):
    print("<h1>Update Employee Info</h1><p>")
    print("""
    <table border=1>
    <tr><td>FirstName</td><td>LastName</td><td>Gender</td><td>Address</td><td>City<td><td>State</td><td>Zipcode</td><td>DepartmentId</td><td>Email</td><td>Phone</td><td>SupervisorId</td><td>Salary</td></th>
    """)
    result = dbobj.updateEmployeeInfo(FirstName,LastName,Gender,Address,City,State,Zipcode,DepartmentId,Email,Phone,SupervisorId,Salary)
    
    print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%d</td><td>%d</td><td>%s</td><td>%d</td><td>%d</td><td>%d</td></th>"  % (FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary))


def updateVisitorInfo(Firstname,Lastname,Address,City,State,Zipcode,Birthday,Email):
    print("<h1>Update Visitor Info</h1><p>")
    print("""
    <table border=1>
    <tr><th>Firstname</th><td>Lastname</td><td>Address</td><td>City<td><td>State</td><td>Zipcode</td><td>Birthday</td><td>Email</td><th>
    """)
    cur = dbobj.updateVisitorInfo(Firstname,Lastname,Address,City,State,Zipcode,Birthday,Email)
    result = cur.fetchall()
    print("<tr><td>%s</td></tr><tr><td>%s</td></tr><tr><td>%s</td></tr><tr><td>%s</td></tr><tr><td>%s</td></tr><tr><td>%s</td></tr><tr><td>%s</td></tr><tr><td>%s</td></tr>" % (result))


def listAnimalInfo(name):
    cur = dbobj.listAnimalInfo(name)
    
    # Fetch some the results
    result = cur.fetchall()
    
    
    print("""
    <table border=1>
    <tr><th>AnimalID</th><td>Sex</td><td>Name</td><td>Species</td><td>Birthdate</td><td>Age</td><td>ExtinctionStatus</td><td>Origin</td><td>LocationName</td></tr>
    """)
    for row in result:
        AnimalID,Sex,Name,Species,BirthDate,Age,ExtinctionStatus,Origin,LocationName = row
        #print("%d %s %s %s %d %s %s %s %s" % (AnimalId,Sex,Name,Species,Birthdate,Age,ExtinctionStatus,Origin,LocationName))
        print("<tr><td>%d</td><td>%s</td><td>%s</td><td>%s</td><td>%d</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>" % (AnimalId,Sex,Name,Species,Birthdate,Age,ExtinctionStatus,Origin,LocationName))
        print()
        
    print("""
    
    </table>
    
    <br>
    <a href="?">URL</a>
    
    """)
    
    
    
def listNearbyAnimal(zonename):
      cur = dbobj.listNearbyAnimal(zonename)
    
     # Fetch some the results  <td></td>
    result = cur.fetchall()
    
    print("""
    <table border=1>
    <tr><th>AnimalID</th><td>Species</td><td>LocationName</td>></th>
    """)
    for row in result:
        AnimalID, Species, LocationName = row
    print("<tr><th>%d</th><td>%s</td><td>%s</td>"  % (AnimalID,Species,LocationName))
    print()
    
    print("""
    
    </table>
    
    <br>
    <a href="?">URL</a>
    
    """)
    
    
def listVisitorBasedOnTier(tier):
      cur=dbobj.listVisitorBasedOnTier(tier)
      result=cur.fetchall()
      
      print("""
    <table border=1>
    <tr><th>VistorID</th><td>FirstName</td><td>LastName</td>></th>
    """)
    for row in result:
        VisitorID, FirstName, LastName = row
    print("<tr><th>%d</th><td>%s</td><td>%s</td>"  % (VisitorID,FirstName,LastName))
    print()
    
    print("""
    
    </table>
    
    <br>
    <a href="?">URL</a>
    
    """)
    
    
def showOldestAnimal():
      cur=dbobj.showOldestAnimal()
      result=cur.fetchall()
         print("""
    <table border=1>
    <tr><th>AnimalID</th><td>Name</td><td>Species</td><td>Age</td>
    """)
        
      for row in result:
        AnimalID, Name, Species, Age = row
    print("<tr><th>%d</th><td>%s</td><td>%s</td><td>%d</td>"  % (AnimalID,Name,Species,Age))
    print()
    
    print("""
    
    </table>
    
    <br>
    <a href="?">URL</a>
    
    """)
    
    
def showForeignAnimal():
      cur=dbobj.showForeignAnimal()
      result=cur.fetchall()
         print("""
    <table border=1>
    <tr><th>AnimalID</th><td>Name</td><td>LocationName</td>
    """)
        
        for row in result:
        AnimalID, Name, LocationName = row
    print("<tr><th>%d</th><td>%s</td><td>%s</td>"  % (AnimalID,Name,LocationName))
    print()
    
    print("""
    
    </table>
    
    <br>
    <a href="?">URL</a>
    
    """)
    
    
def showNearbyFeeding(zonename):
      cur=dbobj.showNearbyFeeding(zonename)
      result=cur.fetchall()
        print("""
    <table border=1>
    <tr><th>FeedingTime</th><td>FeedingLocation</td><td>AnimalID</td><td>Species</td>
    """)
        for row in result:
        FeedingTime, FeedingLocation, AnimalID, Species = row
    print("<tr><th>%s</th><td>%s</td><td>%d</td><td>%s</td>"  % (FeedingTime,FeedingLocation,AnimalID,Species))
    print()
    
    print("""
    
    </table>
    
    <br>
    <a href="?">URL</a>
    
    """)
    
    
    
def insertNewEmployee(SSN, FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary):
    cur = dbobj.insertNewEmployee(SSN, FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary)
    
     # Fetch some the results  <td></td>
    result = cur.fetchall()
    
    print("""
    <table border=1>
    <tr><th>SSN</th><td>FirstName</td><td>LastName</td><td>Gender</td><td>Address</td><td>City<td><td>State</td><td>Zipcode</td><td>DepartmentId</td><td>Email</td><td>Phone</td><td>SupervisorId</td><td>Salary</td></th>
    """)
    for row in result:
        SSN, FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary = row
    print("<tr><th>%d</th><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%d</td><td>%d</td><td>%s</td><td>%s</td><td>%d</td><td>%d</td></th>"  % (SSN, FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary))
    print()
    
    print("""
    
    </table>
    
    <br>
    <a href="?">URL</a>
    
    """)
    
    
def deleteVisitorById(ID):
    dbobj.deleteVisitorById(ID)
    print("<p>Visior deleted</p>")
    
    
def deleteEmpById(ID):
      dbobj.deleteEmployeeById(ID)
      print("<p>Employee deleted</p>")


    
    
      
def showDefaultEmployeePage():    
    print("""
    <h1>Welcome to Employee Page</h1>
    <br>
    You can:<br><ul>
    
    <!-- Adding attributes to the end of a URL puts them into the CGI form -->
    <li><a href="?UpdateEmployeeInfo=1">Update Employee Info</a>
    <li><a href="?UpdateVisitorInfo=1">Update Visitor Info</a>
    <li><a href="?listAnimalInfo=1">List Animal Info</a>
    <li><a href="?listNearbyAnimal=1">List Nearby Animal Info</a>
    <li><a href="?listVisitorBasedOnTier=1">List Visitor by Tier</a>
    </ul>
    
    <p>    
    """)  

def showDefaultAdminPage():    
    print("""
    <h1>Welcome to Admin Page</h1>
    <br>
    You can:<br><ul>
    
    <!-- Adding attributes to the end of a URL puts them into the CGI form -->
    <li><a href="?InsertnewEmployee=1">Insert New Employee</a>
    <li><a href="?UpdateEmployeeInfo=1">Update Employee Info</a>
    <li><a href="?UpdateVisitorInfo=1">Update Visitor Info</a>
    <li><a href="?deleteEmpById=1">Delete Employee</a>
    <li><a href="?deleteVisitorById=1">Delete Visitor</a>
    <li><a href="?listAnimalInfo=1">List Animal Info</a>
    <li><a href="?listNearbyAnimal=1">List Nearby Animal Info</a>
    <li><a href="?listVisitorBasedOnTier=1">List Visitor by Tier</a>
    </ul>
    
    <p>    
    """)
    
def showDefaultVisitorPage():    
    print("""
    <h1>Welcome to Visitor Page</h1>
    <br>
    You can:<br><ul>
    
    <!-- Adding attributes to the end of a URL puts them into the CGI form -->
    <li><a href="?UpdateVisitorInfo=1">Update Visitor Info</a>
    <li><a href="?listAnimalInfo=1">List Animal Info</a>
    <li><a href="?listNearbyAnimal=1">List Nearby Animal Info</a>
    </ul>
    
    <p>    
    """)
    
def showInsertNewEmployeeForm():

    print("""
    <h2>Input to Update Employee Info</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="InsertnewEmployee" value="1">
        SSN: <input type="text" name="SSN" required><br><br>
        First Name: <input type="text" name="FirstName" required><br><br>
        Last Name: <input type="text" name="LastName" required><br><br>
        Gender: <input type="text" name="Gender" required><br><br>
        Address: <input type="text" name="Address" required><br><br>
        City: <input type="text" name="City" required><br><br>
        State: <input type="text" name="State" required><br><br>
        Zipcode: <input type="text" name="Zipcode" required><br><br>
        DepartmentID: <input type="text" name="DepartmentID" required><br><br>
        Email: <input type="email" name="email" required><br><br>
        Phone: <input type="text" name="Phone" required><br><br>
        SupervisorId: <input type="text" name="SupervisorId" required><br><br>
        Salary: <input type="email" name="Salary" required><br><br>
        <input type="submit" value="submit">
    </FORM>
    """)
    
def showUpdateEmployeeInfoForm():

    print("""
    <h2>Input to Update Employee Info</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="UpdateEmployeeInfo" value="1">
        First Name: <input type="text" name="FirstName" required><br><br>
        Last Name: <input type="text" name="LastName" required><br><br>
        Gender: <input type="text" name="Gender" required><br><br>
        Address: <input type="text" name="Address" required><br><br>
        City: <input type="text" name="City" required><br><br>
        State: <input type="text" name="State" required><br><br>
        Zipcode: <input type="text" name="Zipcode" required><br><br>
        DepartmentID: <input type="text" name="DepartmentID" required><br><br>
        Email: <input type="email" name="email" required><br><br>
        Phone: <input type="text" name="Phone" required><br><br>
        SupervisorId: <input type="text" name="SupervisorId" required><br><br>
        Salary: <input type="email" name="Salary" required><br><br>
        <input type="submit" value="submit">
    </FORM>
    """)

def showUpdateVisitorInfoForm():

    print("""
    <h2>Input to Update Visitor Info</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="UpdateVisitorInfo" value="1">
        Last Name: <input type="text" name="LastName" required><br><br>
        First Name: <input type="text" name="FirstName" required><br><br>
        Address: <input type="text" name="Address" required><br><br>
        City: <input type="text" name="City" required><br><br>
        State: <input type="text" name="State" required><br><br>
        Zipcode: <input type="text" name="Zipcode" required><br><br>
        Birthday: <input type="text" name="Birthday" required><br><br>
        Email: <input type="email" name="email" required><br><br>
        <input type="submit" value="submit">
    </FORM>
    """)

def showDeleteEmployeeForm():

    print("""
    <h2>Input to Delete Employee</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="deleteEmpById" value="1">
        Employee ID: <input type="text" name="Id" required><br><br>
    </FORM>
    """)
    
def showDeleteVisitorForm():

    print("""
    <h2>Input to Delete Visitor</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="deleteVisitorById" value="1">
        Visitor ID: <input type="text" name="Id" required><br><br>
    </FORM>
    """)

def showListAnimalInfoForm():

    print("""
    <h2>Input to Show Animal Info</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="listAnimalInfo" value="1">
        Animal ID: <input type="text" name="animalid" required><br><br>
    </FORM>
    """)

def showListNearbyAnimalForm():

    print("""
    <h2>Input to Show Nearby Animal Info</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="listNearbyAnimal" value="1">
        Zone Name: <input type="text" name="zonename" required><br><br>
    </FORM>
    """)
    
def showListVisitorForm():

    print("""
    <h2>Input to Show Animal Info</h2>
    <p>
    <!-- without action="someurl", the form will run the script that generated the page -->    
    <FORM METHOD="POST">
    
    <!-- Hidden form field used to keep track of state (what we are doing) -->
    <input type="hidden" name="listVisitorBasedOnTier" value="1">
        Tier: <input type="text" name="tier" required><br><br>
    </FORM>
    """)
