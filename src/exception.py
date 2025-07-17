import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys): #This function takes: error: the actual exception (e.g., ZeroDivisionError) & error_detail: the full error context from sys (used to get traceback)
    _,_,exc_tb=error_detail.exc_info() # This gets the traceback object exc_tb from the exception where exc_info() gives: (exception_type, exception_object, traceback)
    file_name =exc_tb.tb_frame.f_code.co_filename #Gets the name of the Python file where the error occurred
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message


class CustomException(Exception):   #customexception classs is inherited from Exception class
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) #Calls base class Exception to store the original message
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    



    

