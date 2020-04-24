"""

This is a test module to explaine how to use the Bit Class

"""

import time

from bit import Bit   

i=0

x=Bit() #Create a new Object

print('Start')

print(time.gmtime())

while not x.falling_edge(): #Loop unitle we get a Falling Edge

    i=(int(time.time())%2) #return 1 if seconds count is Odd , 0 if Even
    
    x(i)    #Update the Value of x bit
    
print('Catch Falling Edge')

print(time.gmtime())
