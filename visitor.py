import time
import cgi
import cgitb; cgitb.enable()
import dbinterface
class visitor:
	

	################################################################################
	def doHTMLHead():

    	print("""
    	<html>
    	<head>
    	<title>visitor</title>
	    </head>
	    <body>
	    """)


	################################################################################
	def doHTMLTail():

	    print("""
	    <p>
	    <hr>
	    This page was generated at %s.
	    </body>
	    </html>

	    """ % time.ctime())


	################################################################################
	if __name__ == "__main__":

	    print("Content-Type: text/html; charset=utf-8")
	    print("Cache-Control: no-cache, must-revalidate") # HTTP/1.1 
	    print("Expires: Sat, 26 Jul 1997 05:00:00 GMT") # Date in the past 
	    print()

	    form = cgi.FieldStorage()
    
	    doHTMLHead()

	    #print("<br><br>")
	    #print("Debugging mode with 'print form':<br>")
	    #print(form)
	    #print("<br><br>")

	    if "UpdateVisitorInfo" in form and "Birthday" in form:
	    	LastName = form["LastName"].value
	    	FirstName = form["FirstName"].value
	    	Address = form["Address"].value
	    	City = form["City"].value
	    	State = form["State"].value
	    	Zipcode = form["Zipcode"].value
	    	Birthday = form["Birthday"].value
	    	Email = form["Email"].value
	    	dbinterface.UpdateVisitorInfo(LastName,Firstname,Address,City,State,Zipcode,Birthday,Email)

	    elif "UpdateVisitorInfo" in form:
	    	dbinterface.showUpdateVisitorInfoForm()
	    	
	    elif "listAnimalInfo" in form and "animalid" in form:
	    	animalid = form["animalid"].value
	    	dbinterface.listAnimalInfo(animalid)

	    elif "listAnimalInfo" in form:
	    	dbinterface.showListAnimalInfoForm()

	    elif "listNearbyAnimal" in form and "zonename" in form:
	    	zonename = form["zonename"].value
	    	dbinterface.listNearbyAnimal(zonename)

	 	elif "listNearbyAnimal" in form:
	    	dbinterface.showListNearbyAnimalForm()

	    else:        
    	    # substitute other functions in here to test from command line
        	# musicinterface.listArtists()
        
        	# show the default page
        	dbinterface.showDefaultVisitorPage()

	    doHTMLTail()   

