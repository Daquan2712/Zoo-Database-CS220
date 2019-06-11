import sqlite3 as db 
from datetime import date
from datetime import timedelta

class projectzooDB:
    def __init__(self):
    self.conn=db.connect("projectzoo.db")
    
    def __del__(self):
    self.conn.cles()
    
    def UpdateEmployeeInfo(self,FirstName,LastName,Gender,Address,City,State,Zipcode,DepartmentID,Email,Phone,SupervisorId,Salary)
        cur = self.conn.cursor();
        params = (FirstName,LastName,Gender,Address,City,State,Zipcode,DepartmentID,Email,Phone,SupervisorId,Salary)
        cur.execute("UPDATE employee SET FirstName = %s, LastName = %s, Gender = %s, Address = %s, City = %s, State = %s, Zipcode = %s, DepartmentID = %s, Email = %s, Phone = %s, SupervisorId = %s, Salary = %s", params)
        result = cur.fetchall()
        self.conn.commit()
        return(result)
    
    
    def UpdateVisitorInfo(self,LastName,Firstname,Address,City,State,Zipcode,Birthday,Email):
        cur = self.conn.cursor();
        params = (LastName,Firstname,Address,City,State,Zipcode,Birthday,Email)
        cur.execute("UPDATE visitors SET LastName = %s, FirstName = %s, Address = %s, City = %s, State = %s, Zipcode = %s, Birthday = %s, Email = %s", params)
        result = cur.fetchall()
        self.conn.commit()
        return(result)
    
    
    def listAnimalInfo(self, animalid):
        cur = self.conn.cursor()
        params = (animalid,)
        cur.execute("SELECT Sex, Name, Species, Birthdate, Age, ExtinctionStatus, Origin, LocationName FROM Animal WHERE AnimalId like %d", params)
        result = cur.fetchall()
        return(result)
    # result = dbobj.listAnimalInfo(animalid)
    # if len(result) == 0:
    #   print("<h2>%s Animal not found in the database</h2>" % animalid)
    # else:
    #   for row in result:
    #       print(row)
    # print("""
    # 
    #
    # <br>
    # <a href="?">Return Home</a>
    #
    # """)
    
    def listNearbyAnimal(self, zonename):
        cur = self.conn.cursor()
        params = (zonename,)
        cur.execute("SELECT a.AnimalId, a.Species, a.LocationName FROM Animal AS a, Location AS l WHERE a.LocationName = l.LocationName AND l.ZoneName like %s", params)
        result = cur.fetchall()
        return(result)
    # result = dbobj.listNearbyAnimal(zonename)
    # if len(result) == 0:
    #   print("<h2>%s Zone not found in the database</h2>" % zonename)
    # else:
    #   for row in result:
    #       print(row)
    # print("""
    # 
    #
    # <br>
    # <a href="?">Return Home</a>
    #
    # """)
    
    def listVisitorBasedOnTier(self, tier):
        cur = self.conn.cursor()
        params = (tier,)
        cur.execute("SELECT VisitorId FirstName LastName Email FROM Visitors WHERE MembershipTier like %d", params)
        result = cur.fetchall()
        return(result)
    # result = dbobj.listVisitorBasedOnTier(tier)
    # if len(result) == 0:
    #   print("<h2>%d Tier not valid</h2>" % tier)
    # else:
    #   for row in result:
    #       print(row)
    # print("""
    # 
    #
    # <br>
    # <a href="?">Return Home</a>
    #
    # """)
    
    def showOldestAnimal(self):
        cur = self.conn.cursor()
        cur.execute("SELECT AnimalId, Name, Species, Age, LocationName FROM Animal WHERE Age = (SELECT MAX(Age) FROM Animal)")
        result = cur.fetchall()
        return(result)
    # result = dbobj.showOldestAnimal()
    # for row in result:
    #       print(row)
    # print("""
    # 
    #
    # <br>
    # <a href="?">Return Home</a>
    #
    # """)
    
    def showForeignAnimal(self):
        cur = self.conn.cursor()
        cur.execute("SELECT AnimalId, Species, LocationName FROM Animal WHERE Origin != 'Project'")
        result = cur.fetchall()
        return(result)
    # result = dbobj.showForeignAnimal()
    # if len(result) == 0:
    #   print("<h2> No animal from outside</h2>")
    # else:
    #   for row in result:
    #       print(row)
    # print("""
    # 
    #
    # <br>
    # <a href="?">Return Home</a>
    #
    # """)
    
    def showNearbyFeeding(self, zonename):
        cur = self.conn.cursor()
        params = (zonename,)
        cur.execute("SELECT f.Time, f.LocationName, a.AnimalId, a.Species FROM Animal AS a, Location AS l, FeedingCalendar AS f WHERE a.LocationName = f.LocationName AND f.Time < (Select Convert(Time, GetDate())) AND l.ZoneName like %s", params)
        result = cur.fetchall()
        return(result)
    # result = dbobj.showNearbyFeeding(zonename)
    # if len(result) == 0:
    #   print("<h2>%s Zone not found in the database</h2>" % zonename)
    # else:
    #   for row in result:
    #       print(row)
    # print("""
    # 
    #
    # <br>
    # <a href="?">Return Home</a>
    #
    # """)
    
    def CreatenewVisitAccount(self, FirstName, LastName, Address, City, State, Zipcode, Birthday, Email):
        cur = self.conn.cursor();
        tod = date.today();
        Joindate = str(date.today());
        exp = tod + timedelta(days = 1825);
        Expdate = str(exp);
        MembershipTier = '0';
        ZoopBalance = 0;
        params = (FirstName, LastName, Address, City, State, Zipcode, Birthday, MembershipTier, Email, ZoopBalance, JoinDate, Expdate, None, )
        cur.execute("INSERT INTO Visitors"
                   "(FirstName, LastName, Address, City, State, Zipcode, Birthday, MembershipTier, Email, ZoopBalance, JoinDate, Expdate, RepId)"
                    "Values (?,?,?,?,?,?,?,?,?,?,?,?,?)", params)
        self.conn.commit()
        result = cur.fetchall()
        return (result)
        
    
    def InsertnewEmployee(self, SSN, FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary):
        cur = self.conn.cursor();
        params = (SSN, FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary,)
        cur.execute("INSERT INTO Employee"
                   "(SSN, FirstName, LastName, Gender, Address, City, State, Zipcode, DepartmentId, Email, Phone, SupervisorId, Salary,)"
                   "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", params)
        self.conn.commit()
        result = cur.fetchall()
        return (result)
    
    
    def visitorIdExist(self, iD):
        cur = self.conn.cursor()
        param = (iD, )
        cur.execute("SELECT * FROM Visitors WHERE VisitorId = ?", param)
        if len(cur.fetchall()) == 0:
            return False
        else:
            return True
    
    def deleteVisitorById(self, iD):
        if (self.visitorIdExist(iD)):
            cur = self.conn.cursor()
            param = (iD, )
            cur.execute("DELETE * FROM Visitor WHERE VisitorId = ?", param)
            self.conn.commit()
            print("<p>Visitor deleted</p>")
        else:
            print("<p>Visitor doesn't exist!</p>")
            return
    
    def employeeIdExist(self, iD):
        cur = self.conn.cursor()
        param = (iD, )
        cur.execute("SELECT * FROM ES WHERE EmployeeId = ?", param)
        if len(cur.fetchall()) == 0:
            return False
        else:
            return True
          
    def HasEmployee(self,firstname,lastname):
        cur=self.conn.cursor();
        params=(firstname,lastname,)
        cur.execute("SELECT FirstName,LastName FROM Employee WHERE FirstName =? and LastName=?",params)
        result=cur.fetchall()
        return (result)
    
    def deleteEmpById(self, iD):
        if (self.employeeIdExist(iD)):
            cur = self.conn.cursor()
            param = (iD, )
            cur.execute("DELETE * FROM ES WHERE EmployeeId = ?", param)
            self.conn.commit()
            print("<p>Employee deleted</p>")
        else:
            print("Employee doesn't exist")
            return

    def checkAccountType(self, username, password):
        cur = self.conn.cursor()
        param = (username,)
        cur.execute("SELECT * FROM Logins WHERE username = ?", param)
        if len(cur.fetchall()) == 0:
            print("Username or password mismatched!")
            return None
        else:
            param = (username, password)
            cur.execute("SELECT * FROM Logins WHERE username = ? AND password = ?", param)
            if len(cur.fatchall()) == 0:
                print("Username or password mismatched!")
                return None
            else:
                cur.execute("SELECT Acc_Type FROM Logins WHERE username = ? AND password = ?", param)
                result = cur.fetchall()
                return result
    
    
    