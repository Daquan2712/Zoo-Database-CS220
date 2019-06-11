#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 14:50:27 2018

@author: RVFBM
"""

#!/usr/bin/python
# -*- coding: utf-8 -*-
# "she-bang" line is a directive to the web server: where to find python
#
# filename: createAcc.py
# cTunes = Clark Tunes = mini iTunes?

import time
import cgi
import cgitb; cgitb.enable()
from db import projectzooDB
#import createAccountInterface

# Create a database object that will handle all the DB stuff.
dbobj = projectzooDB()

################################################################################
def doHTMLHead():

    print("""
    <html>
    <head>
    <title>createAccount</title>
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

         
    #createAccountInterface.showCreateAccountPage()
    fname = form["First Name"].value 
    lname = form["Last Name"].value
    address = form["Address"].value
    city = form["City"].value
    state = form["State"].value
    zipc = form["Zipcode"].value
    bday = form["Birthday"].value
    email = form["Email"].value
    dbobj.CreatenewVisitAccount(fname,lname, address, city, state, zipc, bday, email)


    doHTMLTail()    





