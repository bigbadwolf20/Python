#!usr/bin/python

from datetime import *

a1 = datetime.now().hour
a1 = str(a1)
def main(): #define main
    print "Hello, world !"
    print "Ich heisse Python !"
    print "It is " + a1 + " O'clock"
    print "It is " + str(datetime.now().minute)+ " Minute"
    print "It is " + str(datetime.now().second)+ " Second"

main()
