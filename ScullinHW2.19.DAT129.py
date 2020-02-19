# -*- coding: utf-8 -*-
"""
Dan Scullin
DAT-129
Icon Programming
Goal is to create an icon of my creation, and manipulate it using functions. Rad!
This is a temporary script file.
"""

lists = [['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
['0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
['0', '0', '0', '1', '1', '1', '0', '0', '0', '0'],
['0', '0', '1', '1', '1', '1', '1', '0', '0', '0'],
['0', '0', '0', '1', '1', '1', '0', '0', '0', '0'],
['0', '0', '1', '1', '1', '1', '1', '0', '0', '0'],
['0', '0', '0', '1', '1', '1', '0', '0', '0', '0']]


def print_lists (the_list):
    """
    The goal of this function is to take in a list of lists, and print it using 
    the @ and . symbols to create a 10 x 10 icon. 
    """
    for list in the_list:
        print("")
        #gives us some space 
        for item in list:
            if item == "0":
                print(".", sep='', end='')
                #prints . for 0 in the list
            elif item == "1":
                print("@", sep='', end='')
                #prints @ for 1 in the list


def print_icon_inverse (the_list):
    """
    the goal of this function is to create an icon that prints from the list above,
    but prints the inverse of the icon instead
    """
    for list in the_list:
        print("")
        for item in list:
            if item == "0":
                print("@", sep='', end ='')
            elif item == "1":
                print (".", sep='', end='')
                

        

if __name__ == '__main__':

    (print_lists(lists))
    print("")
    (print_icon_inverse(lists))
