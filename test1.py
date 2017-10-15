#!usr/bin/python
"""Programmed by BigBadWolf15, github.com/bigbadwolf15"""

from datetime import * #import library

a1 = datetime.now().hour
a1 = str(a1) #convert a1 to string

def main(): #define main
    print "Hello, world !"
    print "Ich heisse Python !"
    print "It is " + a1 + " O'clock"
    print "It is " + str(datetime.now().minute)+ " Minute"
    print "It is " + str(datetime.now().second)+ " Second"

main() #call functions main
#end
