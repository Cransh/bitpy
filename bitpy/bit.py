# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:24:37 2020

bit object to save all the state of the bit
@author: Cransh
"""
#import logging for error messages
import logging

#isbool helper Function
#return True if the value is 1 ,0 True ,False

def isbool(value):
    """
    check if the value is bool

    Parameters
    ----------
    value : any
        can accept any value to be checked.

    Returns
    -------
    bool
        True if the value is 1 ,0 , True or False.
        Flase for anything else.

    """
    temp=str(value).lower()
    if temp == 'true' or temp == 'false' or temp == '1' or temp =='0':
        return True
    else:
        return False

class Bit():
    """
        new Bit Class for all the operation of the class

        Parameters
        ----------
        status :bool, optional
            the initial value of the Bit . The default is False.

        Returns
        -------
        None.

    """
        
    __bit_status=False
    __old_bit_status=False
    def __init__(self, status=False):
        
        if isbool(status):
            self.__bit_status=bool(status)
            self.__old_bit_status=bool(status)
            logging.debug('Object created with Value %s' %self.__bit_status)
        else:
            self.__bit_status=False
            self.__old_bit_status=False
            logging.error('Wrong assiment set False as defualt')
            
                
        
    def  __call__(self, status=None):
        """
        if a new value assaind, update the bit value
        or return the bit as it
        
        Parameters
        ----------
        status : bool, optional
            the new value of the bit. The default is None.

        Returns
        -------
        bit with the new or the old value
            
        """
        if status == None:
            return self
        else:
            if isbool(status):
                self.__old_bit_status=bool(self.__bit_status)
                self.__bit_status=bool(status)
                return self
            else:
                return self
            
    
    def update(self,status):
        """
        update the value of bit according to status.

        Parameters
        ----------
        status : Bool
            The new value of the bit.

        Returns
        -------
        bool
            Return the bool value after update the bit

        """
        if isbool(status):
            self.__old_bit_status=bool(self.__bit_status)
            self.__bit_status=bool(status)
            return self.__bit_status
        else:
            logging.error('Wrong assiment, only True or False')
        
    def __repr__(self):
        """
        return True or False accordng to the bit Status
    
        Returns
        -------
        String
            True if the bit is On
            False if the bit is Off

        """
        return str(bool(self.__bit_status))
    
    def rising_edge(self):
        """
        return True if rising edge of the bit
        has been detected and clear it

        Returns
        -------
        bool
            True if the rising edge has been detected.
            False if the rising edge not detected.

        """
        if self.__old_bit_status==False and self.__bit_status==True:
            self.__old_bit_status=self.__bit_status
            return True
        else:
            return False
        
    def falling_edge(self):
        """
        return True if faling edge of the bit
        has been detected and clear it

        Returns
        -------
        bool
            True if the falling edge has been detected.
            False if the falling edge not detected.

        """
        if self.__old_bit_status==True and self.__bit_status==False:
            self.__old_bit_status=self.__bit_status
            return True
        else:
            return False
        
    def value(self):
        """
        return the integer value of the bit

        Returns
        -------
        TYPE
            1 if bit is Ture
            0 if bit is False

        """
        return int(self.__bit_status)
    
    def toggle(self):
        """
        Toggle the value of the Bit

        Returns
        -------
        Bit
            Return the Bit if needed to be assined again

        """
        self.__old_bit_status=bool(self.__bit_status)
        self.__bit_status= not self.__bit_status
        return self
    
    def set_bit(self):
        """
        Set the Bit (Make it True)

        Returns
        -------
        Bit
            Return the Bit if needed to be assined again

        """
        self.__old_bit_status=bool(self.__bit_status)
        self.__bit_status= True
        return self
        
    def reset_bit(self):
        """
        Reset the Bit (Make it False)

        Returns
        -------
        Bit
            Return the Bit if needed to be assined again

        """
        self.__old_bit_status=bool(self.__bit_status)
        self.__bit_status= False
        return self
        
