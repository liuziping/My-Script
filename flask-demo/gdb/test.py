#!/usr/bin/env python 
try:
    raise MyException ("this is my exception")
except MyException,data:
    print data
