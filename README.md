# bitpy
Better Bool Type for Python

add Falling edge and Rising edge Detection function for Bool-like Type.

#to use the module 

*********************************************************************************************

  from bit import Bit

  x=Bit() #Create new bit with false value

  y=Bit(1) #Create new bit with True value

  x.value() #return int value of the bit

  y(0)  #update the value of the bit

  z=x() #create new bit with the state of x

  x(1) #update the value of the bit

  x.rising_edge()#return True

  y.falling_edge()#return True

  x.rising_edge()#return False because the bit need to get a rising edge condion again 

*********************************************************************************************
