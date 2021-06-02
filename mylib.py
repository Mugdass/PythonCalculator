#This is the flower box#
#Program name: mylib.py
#Student Name: Matas Backevicius#
#Course: ENTD220#
#Instructor: Georgia Brown#
#Date: May 4, 2021#
#Description:       This is mylib program imorted to the main code in order to caculate and return a value. All function are on this module.
                   # But the value is returned on the main code.














    
def Sum(fn, sn):                            #first we use def Sum to execute the addition and return the answer by print the string and the calculation assigned to the variable 'answer'
    answer= int (fn) + int (sn)
    return answer






def Diff(fn, sn):                           #similarly to addition, here we use def named Diff to execute subtraction assigned to a variable named answer1,
                                                            # once we xecute 'answer1' we return its value which is the answer we want
    answer1= int (fn) - int (sn)
    return answer1







def Mult(fn, sn):                               #like the other two def functions, to return a value for this multiplication function, we execute the variable 'answer3'
                                                    # by calling the variable and the name of the function Mult
    answer3= int (fn) * int (sn)
    return answer3









def scalc1(fn,sn):          # new functions to calculate the numbers with mylif this will be imported to the main code
    t1= fn * sn
    return t1




def scalc2(fn,sn):
    t2= fn + sn
    return t2


def scalc3(fn,sn):
    t3= fn - sn
    return t3


def scalc4(fn,sn):
    t4= fn / sn
    return t4


                                                  
