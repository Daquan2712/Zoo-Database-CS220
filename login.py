#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:06:00 2018

@author: bradley
"""

import cgi
import cgitb; cgitb.enable()
import dbinterface


def checkAccountType():
    form = cgi.FieldStorage()
    user = form["username"].value
    password = form["password"].value
    #check the account type using function from dbinterface
	return dbinterface.checkingAccount()

def main():
    
    result = checkAccountType()
	if 0 in result:
		visitor.main()
	elif 1 in result:
		employee.main()
	elif 2 in result:
		admin.main()
		
# Only run the main method if this was the script that was run
if __name__ == "__main__":
    main()
    