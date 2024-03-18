#This reads all the the user inputs
#Importing all the required modules

from requirement_chain.file_operations import *
import pandas as pd
import numpy as np

def print_options():
    print("\n***Please select from the following***")
    print("1 : Add genesis artifact")
    print("2 : Add requirement artifact")
    #print("2 : Mine the requirement block")
    print("3 : Print the requirement chain")
    print("4 : Verify the requirement chain")
    print("5 : Create wallet")
    print("6 : Load wallet")
    print("7 : Save wallet")
    print("q : Quit")

def get_user_input(path):
    """ 
    Explanation:
    Arguments:
    Return values: 
    """
    #creators = input("Who are the creators of the artifact? ")
    #artifact_name = input("Enter the name of the artifact: ")
    name, depends_on, authors, requirement_data = read_file_pd(path)
    return name[:], depends_on[:], authors[:], requirement_data.copy()

#Get user choice
def get_user_choice():
    """ 
    Explanation:
    Arguments:
    Return values: 
    """
    return input("enter your choice: ")