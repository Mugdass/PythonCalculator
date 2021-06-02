#This is the flower box#
#Program name: Wk8_matas_backevicius.py#
#Student Name: Matas Backevicius#
#Course: ENTD220#
#Instructor: Georgia Brown#
#Date: May 25, 2021#
#Description:  added  menu items "to file to write" and file to read". Also two methods used write() and read() to call upon the attributes in that file.
#The results will be displayed and called upon in the file with these two methods to write to file and to read from file.


import mylib








class ValueError(Exception):                    # this will be the first implemented exception
    pass


while True:                                         #first few input questions asking for a range value
    try:
        lrange = int(input('enter your lower range, -100 the lowest: '))
        hrange = int(input('enter your higher range, 100 the highest: '))
        
        if lrange < -100 or lrange > 100:               #given the start and end of our range, with low and high, given these condition
                                                        #if the range is outside the given range perfor this exception and print this statement.
            raise ValueError 
        elif hrange < -100 or hrange > 100:
            raise ValueError                            # I have implemented another case for a VaueError is the numbers are out of range it will print this exception#
        break
    except ValueError:
        print("The input values are out side the input ranges Please check the numbers and try again Thanks for using our calculator")
        q2=input("Continue Looping Y/N ?")


                                                # this is an implemented exception statement for the numbers out of the given range






lr = -100
hr = 100
                                                     #here is the def IsInRange function to test the value between the low range and high range,
                                                    # will return true or false based on the condition of the given value by the user.
def IsInRange(n):
   # using comaparision operator
   if lr <= n <= hr:
       print(True)
       print('The number {} is in range ({}, {})'.format(n, lr, hr))
   else:
       print(False)
       print('The number {} is not in range ({}, {})'.format(n, lr, hr))

# Test Input List
n=int(input("Enter a value to test it between two ranges"))
value = [n]

for value in value:
   IsInRange(value)
        



            # we print our function by printing the name of our class which is IsInRange and then the variable 'value' with its only value 'n'






    

fn= input("Please Enter you First number: ")            # these are variables assigned with the input asking for the first and second number
sn= input("Please Enter your Second number: ")



answer= mylib.Sum(int(fn),int(sn))
print("The result of,", int(fn), "+", int(sn), "=",answer)          # using the function in mylib module to call upon the value in order to return the value: answer



answer1= mylib.Diff(int(fn),int(sn))
print("The result of,", int(fn), "-", int(sn), "=",answer1)     # using the function in mylib module to call upon the value in order to return the value: answer1


    


answer3= mylib.Mult(int(fn),int(sn))
print("The result of,", int(fn), "*", int(sn), "=",answer3)    # using the function in mylib module to call upon the value in order to return the value: answer3










t1= mylib.scalc1(int(fn),int(sn))               #apllied the new function scalc and imported from mylif into this main code to print the answer for all operator
print(int(fn),(","),int(sn),("*"))
print("the result will be ",t1)                  # for multiplication imported mylib to return an answer for multiplication


t2= mylib.scalc2(int(fn),int(sn))
print(int(fn),(","),int(sn),("+"))          # for addition imported mylib to return an answer for addition
print("the result will be ",t2)


t3= mylib.scalc3(int(fn),int(sn))           # for subtraction imported mylib to return an answer for subtraction
print(int(fn),(","),int(sn),("-"))
print("the result will be ",t3)


t4= mylib.scalc4(int(fn),int(sn))
print(int(fn),(","),int(sn),("/"))
print("the result will be ",t4)         # for division imported mylib to return an answer for division


t5= t1,t2,t3,t4








                                                        #here we ask the user for the input if to Continue Looping or not Continue Looping with these two conditions only available.
ol="Y"
lo="N"

q=input("Continue Looping Y/N ?")
if q=="Y":
    q1=input("Enter first number: ")

elif q=="N":
    q2=input("Still enter first number ")

else:
    q3=input("Still enter first number")







    

class ZeroDivisionError(Exception):                         #this will be the second implemented exception
    pass


try:
        x=input("Enter first number one more time     ")
        print()
        p=input("Enter second number one more time     ")
        print()
        if int(x) <= 0 or int(p) <=0:    #here we have an exception case,I have implemented an exception because the second number cannot be 0, and will throw an error
            raise ZeroDivisionError
        
           

except ZeroDivisionError:
        print("DO NOT ENTER 0")                 # if the condtion is not met which means if the number is 0 it will print this: #
        print()
        print("Run IDLE again!")

        raise Exception("0 is not allowed")             # this is what the exception will be, it will say 0 is not allowed


else:
    print("no errors found")                            # if the number is not 0 it will not print an exception#












    
    
def input_numbers():                             # we ask for the first and second number to perform divison based if the second number is 0 or not 0.

    a = float(input("Enter first number again:"))
    b = float(input("Enter second number again:"))
    return a, b


x, y = input_numbers()

while True:

    if y != 0:                                       # if the second input number is not 0, we print calculation and the answer for division of that given value.

        print(x, "/", y, "is: ", x / y)
        print("Thanks for using our Calculator!")
        break
        

    else:

        print("You Cannot divide by zero")
        q3=input("Continue Looping? Y/N: ")
        print("Try a different number other than zero")      #here if the value given by the user is 0, then we cannot perform the calculation,
                                                                # and we let the user know to choose a number other than 0
                                                                # alsoa sk the user if Continue or not Continue looping,regardless of the answer we continue forever
        x, y = input_numbers()
       

    if q3=="N":
        print("But still try a different number other than zero!")

          #here with the else statement in the de function we can print ths statment rather than having an error,we set the user know that the number has to be other than 0
        x, y = input_numbers()


                                   

Menu= []                        # identify the name of the list 'menu'

Menu.append("1. Add two numbers")
print()

Menu.append("2.Subtract two numbers")
print()                                             # append all the options in the list names 'menu'

Menu.append("3.Multiply two numbers")
print()
Menu.append("4. Divide")
print()
Menu.append("5.all ine one")
print()

Menu.append("6. Write to a File")
print()
Menu.append("7. Read from a File")
print()




joined_string = "\n".join(Menu)                 # separate the option in the list by joining the string ' "\n"
print()
    
print("Welcome to the Menu",)
print()
print(joined_string)                        



def res():                                          # create 'res' function representing the result all the answer in the allinone

    print("allInOne(",fn,",",sn,")")
    print()
    print(allInOne)
    print()
    print(int(fn),"+",int(sn),"=",int(fn) + int(sn))
    print()

    print(int(fn),"-",int(sn),"=",int(fn) - int(sn))
    print()

    print(int(fn),"*",int(sn),"=",int(fn) * int(sn))
    print()

    print(int(fn),"/",int(sn),"=",int(float(fn) / int(sn)))









class wrfile():

    
    with open("resultsfile.txt", "w") as tof:
        tof.write("And these were the RESULTS:\n")
        tof.write("From our previous calculations:\n")
        tof.write("Read from a file name: resultsfile.txt\n")
        tof.write('{}'.format(t5))

    #open and read the file after the appending:

    with open("resultsfile.txt", "r") as tof:
        print(tof.read())











    
print()

print("Please Enter a new first number:")               # use n1 and n2 given by the user to calculate and return a result with the fun 'res'
fnr=input()
print()
print("Please Enter a new second number:")
snr= input()
print()

print()



print()


add=int(fnr) + int(snr)
sub=int(fnr) - int(snr)                                 # identify all the operators for the function
mult=int(fnr) * int(snr)
div=int(fnr) / int(snr)

print()

allInOne= {"add":add,"sub":sub, "mult":mult, "div":int(float(div))}                     # here is the dicitonary 'allinone' REPRESENTING the answer in the function

print()

print()
print()



print("make another selection 1,2,3,4,5,6,7")                           #request the user to make a selection which operation to perform : +,-,*,/
print()
choice=input()

print()






if choice == "1":
    print("allInOne(",fnr,",",snr,")")              # if selection 1st to add the numbers, the return result
    print()
    print(allInOne)
    print()
    print(int(fnr),"+",int(snr),"=",int(fnr) + int(snr))
    print()
    
   

    

elif choice == "2":
    print("allInOne(",fnr,",",snr,")")              # if subtration return the result of subtraction
    print()
    print(allInOne)
    print()
    print(int(fnr),"-",int(snr),"=",int(fnr) - int(snr))
    print()

    

elif choice == "3":
    print("allInOne(",fnr,",",snr,")")
    print()                                         # return the result in the dictionary of multiplication
    print(allInOne)
    print()
    print(int(fnr),"*",int(snr),"=",int(fnr) * int(snr))
    print()

    

elif choice =="4":
    print("allInOne(",fnr,",",snr,")")              # and division
    print()
    print(allInOne)
    print()
    print(int(fnr),"/",int(snr),"=",int(fnr) / int(snr))
    print()

    

elif choice == "5":
   res()                        # call upon allInOne for the function, representing all the operators and the resuult that's shown in the dictionary. by res()



elif choice == "6":

    print("The results are alredy written to a file\n")
    print("next enter choice '7' \n")
    print("and you'll see the results read from that file")


elif choice == "7":
    with open("resultsfile.txt", "w") as tof:
        tof.write("And these were the RESULTS:\n")
        tof.write("From our previous calculations:\n")
        tof.write("Read from a file name: resultsfile.txt\n")
        tof.write('{}'.format(t5))

    #open and read the file after the appending:

    with open("resultsfile.txt", "r") as tof:
        print(tof.read())







    
   



print()
print()


    
print("make another selection 1,2,3,4,5,6,7")
print()

choice1=input()

print()


if choice1 == "1":                                          # continue to allow another selection and perform similar aciton
    print("allInOne(",fnr,",",snr,")")
    print()
    print(allInOne)
    print()
    print(int(fnr),"+",int(snr),"=",int(fnr) + int(snr))
    print()
    
   

    

elif choice1 == "2":
    print("allInOne(",fnr,",",snr,")")                          # continue to allow another selection and perform similar aciton
    print()
    print(allInOne)
    print()
    print(int(fnr),"-",int(snr),"=",int(fnr) - int(snr))
    print()

    

elif choice1 == "3":                                        # continue to allow another selection and perform similar aciton
    print("allInOne(",fnr,",",snr,")")
    print()
    print(allInOne)
    print()
    print(int(fnr),"*",int(snr),"=",int(fnr) * int(snr))
    print()

    

elif choice1 =="4":
    print("allInOne(",fnr,",",snr,")")                          # continue to allow another selection and perform similar aciton
    print()
    print(allInOne)
    print()
    print(int(fnr),"/",int(snr),"=",int(fnr) / int(snr))
    print()

    

elif choice1 == "5":
   res()



elif choice1 == "6":
    print("The results are alredy written to a file\n")
    print("next enter choice '7' \n")
    print("and you'll see the results read from that file")



elif choice1 == "7":
    with open("resultsfile.txt", "w") as tof:
        tof.write("And these were the RESULTS:\n")
        tof.write("From our previous calculations:\n")
        tof.write("Read from a file name: resultsfile.txt\n")
        tof.write('{}'.format(t5))

    #open and read the file after the appending:

    with open("resultsfile.txt", "r") as tof:
        print(tof.read())





    
    

print()                                                 # continue to allow return the function all in one calculation
print()

print("make another selection 1,2,3,4,5,6,7")
print()
choice2= input()

print()


if choice2 == "1":
    print("allInOne(",fnr,",",snr,")")
    print()                                             # continue to allow another selection and perform similar aciton
    print(allInOne)
    print()
    print(int(fnr),"+",int(snr),"=",int(fnr) + int(snr))
    print()
    
   

    

elif choice2 == "2":
    print("allInOne(",fnr,",",snr,")")                      # continue to allow another selection and perform similar aciton
    print()
    print(allInOne)
    print()
    print(int(fnr),"-",int(snr),"=",int(fnr) - int(snr))
    print()

    

elif choice2 == "3":
    print("allInOne(",fnr,",",snr,")")
    print()                                             # continue to allow another selection and perform similar aciton
    print(allInOne)
    print()
    print(int(fnr),"*",int(snr),"=",int(fnr) * int(snr))
    print()

    

elif choice2 =="4":
    print("allInOne(",fnr,",",snr,")")
    print()                                             # continue to allow another selection and perform similar aciton
    print(allInOne)
    print()
    print(int(fnr),"/",int(snr),"=",int(fnr) / int(snr))
    print()

    

elif choice2 == "5":
   res()





elif choice2 == "6":
    print("The results are alredy written to a file\n")
    print("next enter choice '7' \n")
    print("and you'll see the results read from that file")




elif choice2 == "7":
    with open("resultsfile.txt", "w") as tof:
        tof.write("And these were the RESULTS:\n")
        tof.write("From our previous calculations:\n")
        tof.write("Read from a file name: resultsfile.txt\n")
        tof.write('{}'.format(t5))

    #open and read the file after the appending:

    with open("resultsfile.txt", "r") as tof:
        print(tof.read())










print()
print()


print("make another selection 1,2,3,4,5,6,7")
print()
choice3= input()                            # choose another seleciton and will preturn the result for the caluclation

print()


if choice3 == "1":
    print("allInOne(",fnr,",",snr,")")
    print()
    print(allInOne)
    print()
    print(int(fnr),"+",int(snr),"=",int(fnr) + int(snr))
    print()
    
   

    

elif choice3 == "2":
    print("allInOne(",fnr,",",snr,")")
    print()
    print(allInOne)
    print()
    print(int(fnr),"-",int(snr),"=",int(fnr) - int(snr))
    print()

    

elif choice3 == "3":
    print("allInOne(",fnr,",",snr,")")
    print()
    print(allInOne)
    print()
    print(int(fnr),"*",int(snr),"=",int(fnr) * int(snr))
    print()

    

elif choice3 =="4":
    print("allInOne(",fnr,",",snr,")")
    print()
    print(allInOne)
    print()
    print(int(fnr),"/",int(snr),"=",int(fnr) / int(snr))
    print()

    

elif choice3 == "5":
   res()                        # all in one selection, then all calculation will be return as in the function ' res() '
    





elif choice3 == "6":
    print("The results are alredy written to a file\n")
    print("next enter choice '7' \n")
    print("and you'll see the results read from that file")




elif choice3 == "7":
    with open("resultsfile.txt", "w") as tof:
        tof.write("And these were the RESULTS:\n")
        tof.write("From our previous calculations:\n")
        tof.write("Read from a file name: resultsfile.txt\n")
        tof.write('{}'.format(t5))

    #open and read the file after the appending:

    with open("resultsfile.txt", "r") as tof:
        print(tof.read())










print()
print()


print("make another selection 1,2,3,4,5,6,7")
print()
choice4= input()

print()


if choice4 == "1":
    print("allInOne(",fnr,",",snr,")")
    print()                                                     # continue to allow another selection and perform similar aciton
    print(allInOne)
    print()
    print(int(fnr),"+",int(snr),"=",int(fnr) + int(snr))
    print()
    
   

    

elif choice4 == "2":
    print("allInOne(",fnr,",",snr,")")
    print()
    print(allInOne)                                             # continue to allow another selection and perform similar aciton
    print()
    print(int(fnr),"-",int(snr),"=",int(fnr) - int(snr))
    print()

    

elif choice4 == "3":
    print("allInOne(",fnr,",",snr,")")
    print()                                                         # Choose to allow another selection and perform similar aciton
    print(allInOne)
    print()
    print(int(fnr),"*",int(snr),"=",int(fnr) * int(snr))
    print()

    

elif choice4 =="4":
    print("allInOne(",fnr,",",snr,")")
    print()
    print(allInOne)
    print()
    print(int(fnr),"/",int(snr),"=",int(float(fnr) / int(snr)))
    print()

    

elif choice4 == "5":
   res()







elif choice4 == "6":
    print("The results are alredy written to a file\n")
    print("next enter choice '7' \n")
    print("and you'll see the results read from that file")




elif choice4 == "7":
   with open("resultsfile.txt", "w") as tof:
        
    tof.write("And these were the RESULTS:\n")
    tof.write("From our previous calculations:\n")
    tof.write("Read from a file name: resultsfile.txt\n")
    tof.write('{}'.format(t5))

    #open and read the file after the appending:

    with open("resultsfile.txt", "r") as tof:
        print(tof.read())





    



    
print()


print()
print()





print()
print()


print("make another selection 1,2,3,4,5,6,7")
print()

choice5= input()

print()


if choice5 == "1":
    print("allInOne(",fnr,",",snr,")")
    print()                                                     # continue to allow another selection and perform similar aciton
    print(allInOne)
    print()
    print(int(fnr),"+",int(snr),"=",int(fnr) + int(snr))
    print()
    
   

    

elif choice5 == "2":
    print("allInOne(",fnr,",",snr,")")
    print()
    print(allInOne)                                             # continue to allow another selection and perform similar aciton
    print()
    print(int(fnr),"-",int(snr),"=",int(fnr) - int(snr))
    print()

    

elif choice5 == "3":
    print("allInOne(",fnr,",",snr,")")
    print()                                                         # Choose to allow another selection and perform similar aciton
    print(allInOne)
    print()
    print(int(fnr),"*",int(snr),"=",int(fnr) * int(snr))
    print()

    

elif choice5 =="4":
    print("allInOne(",fnr,",",snr,")")
    print()
    print(allInOne)
    print()
    print(int(fnr),"/",int(snr),"=",int(float(fnr) / int(snr)))
    print()

    

elif choice5 == "5":
   res()




elif choice5 == "6":
    print("The results are alredy written to a file\n")
    print("next enter choice '7' \n")
    print("and you'll see the results read from that file")




elif choice5 == "7":
    with open("resultsfile.txt", "w") as tof:
        tof.write("And these were the RESULTS:\n")
        tof.write("From our previous calculations:\n")
        tof.write("Read from a file name: resultsfile.txt\n")
        tof.write('{}'.format(t5))

    #open and read the file after the appending:

    with open("resultsfile.txt", "r") as tof:
        print(tof.read())




    

    
    
print()


print()
print()










print()
print()


print("make another selection 1,2,3,4,5,6,7")
print()

choice6= input()

print()


if choice6 == "1":
    print("allInOne(",fnr,",",snr,")")
    print()                                                     # continue to allow another selection and perform similar aciton
    print(allInOne)
    print()
    print(int(fnr),"+",int(snr),"=",int(fnr) + int(snr))
    print()
    
   

    

elif choice6 == "2":
    print("allInOne(",fnr,",",snr,")")
    print()
    print(allInOne)                                             # continue to allow another selection and perform similar aciton
    print()
    print(int(fnr),"-",int(snr),"=",int(fnr) - int(snr))
    print()

    

elif choice6 == "3":
    print("allInOne(",fnr,",",snr,")")
    print()                                                         # Choose to allow another selection and perform similar aciton
    print(allInOne)
    print()
    print(int(fnr),"*",int(snr),"=",int(fnr) * int(snr))
    print()

    

elif choice6 =="4":
    print("allInOne(",fnr,",",snr,")")
    print()
    print(allInOne)
    print()
    print(int(fnr),"/",int(snr),"=",int(float(fnr) / int(snr)))
    print()

    

elif choice6 == "5":
   res()






elif choice6 == "6":
    print("The results are alredy written to a file\n")
    print("next enter choice '7' \n")
    print("and you'll see the results read from that file")




elif choice6 == "7":
    with open("resultsfile.txt", "w") as tof:
        tof.write("And these were the RESULTS:\n")
        tof.write("From our previous calculations:\n")
        tof.write("Read from a file name: resultsfile.txt\n")
        tof.write('{}'.format(t5))

    #open and read the file after the appending:

    with open("resultsfile.txt", "r") as tof:
        print(tof.read())





    
print()


print()
print()















                                                #here we're adding a statement that will print the name of t




print("This is a class named: Priorfunctions ")
print()
print("It contains all prior functions ")
print("Enter OK to see the first function used")
print()                                                 # will ask the suer to enter 'ok' in order to continue to the function in the new class

p=input()





class Priorfunctions:                           # define the name of the class
  def __init__(self1, name1,number1):           #define the function that will be used to call upon the funciton in that class
    self1.name1 = name1
    self1.number1 = number1
    

  def myfunc1(abc):                                 #will have two variables in the def__ init__ function
    print("When I got " + abc.name1)
   
                                                    # then create a funct with a statekemt pertaining to the prior functions used in this program
p1 = Priorfunctions(" the result it was my def res() function: ",1)
p1.myfunc1()
res()                   # once the myfunc() is called the statment in the class named priorfunctions is printed,
                                #so it's two statements but one being the same for every function

print()
print()                 #spacing


print("Enter OK to see the second function used")
print()
                        #continue with user's input to the next function
p1=input()







def __init__(self2, name2,number2):
    self2.name2 = name2
    self2.number2 = number2
    
                                            #list the function again by calling for the same variable but calling
                                                #for a function and a prior function followed after this one
def myfunc1(abc1):
      print("When I got " + abc1.name2)


p1 = Priorfunctions(" the sum of two numbers I used def sum() function: ",2)
p1.myfunc1()                                                        #function is printed with callng the name of the class and the name of the function

answer= mylib.Sum(int(fn),int(sn))
print("The result of,", int(fn), "+", int(sn), "=",answer)
print()
print()



print("Enter OK to see the third function used")
print()

p2=input()


                                



def __init__(self3, name3,number4):                         #similarly assigned statment to the function contained in the same class
    self3.name3 = name3
    self3.number4 = number4
    

def myfunc1(abc2):
      print("When I got" + abc2.name3)


p1 = Priorfunctions("the difference between the two numbers I used my def Diff() function: ",3)
p1.myfunc1()
                                                        # after the statment in the function is printed, the prior function will be printed right after
answer1= mylib.Diff(int(fn),int(sn))
print("The result of,", int(fn), "-", int(sn), "=",answer1)
print()
print()



print("Enter OK to see the fourth function used")
print()
                                                            #again continue wil user's input
p3=input()








def __init__(self4, name4,number5):                                 # assign another def __init__ function with different variables
    self4.name4 = name4
    self4.number5 = number5
                                                #objects pertaining to the function like p1 which is the class and the statement 

def myfunc1(abc3):
      print("When I got " + abc3.name4)


p1 = Priorfunctions(" the answer after I multiplied two numbers I used def Mult() function: ",4)
p1.myfunc1()
                                                        #once the function is printed in the class, one of the other prior function in this program is printed
answer3= mylib.Mult(int(fn),int(sn))
print("The result of,", int(fn), "*", int(sn), "=",answer3)
print()
print()



print("Enter OK to see the fifth function used")
print()
                                    #with user's input we continue
p4=input()









def __init__(self5, name5,number6):
    self5.name5 = name5
    self5.number6 = number6
    
                                            #simiarly use same function, but change the name of the object
def myfunc1(abc4):
      print("When I got " + abc4.name5)
                                                # the function will print the same stemtnet, but contains the naem of the object like name5

p1 = Priorfunctions(" the answer after I multiplied two numbers with my def scalc1() function: ",5)
p1.myfunc1()                                #the statment and the funciton are both printed because the object p1 is called upon with the name of the class

t1= mylib.scalc1(int(fn),int(sn))               
print(int(fn),(","),int(sn),("*"))
print("the result will be ",t1) 
print()
print()



print("Enter OK to see the sixth function used")
print()

p5=input()








def __init__(self6, name6,number7):                 #here another def function but same class printing a different statement but same statment in the same function
    self6.name6 = name6
    self6.number7 = number7
    

def myfunc1(abc5):
      print("When I got " + abc5.name6)


p1 = Priorfunctions(" the answer after I used my def scalc2() function by multipling two numbers: ",6)
p1.myfunc1()                    #once the class "Priorfunctions" is called the statement is returned pertaining to the statment in the function

t2= mylib.scalc2(int(fn),int(sn))           #right after it the prior function is called upon to show its relation to this statement
print(int(fn),(","),int(sn),("+"))         
print("the result will be ",t2)
print()
print()




print("Enter OK to see the seventh function used")
print()

p6=input()








def __init__(self7, name7,number8):                     #here another def__init__ function to assign the different object's name
    self7.name7 = name7
    self7.number8 = number8
    

def myfunc1(abc6):                                  #same function is assigned, but with a different name as shown in the new def__init__ function
      print("When I got " + abc6.name7)


p1 = Priorfunctions(" the answer after using my def scalc3() function by subtracting both numbers: ",7)
p1.myfunc1()                                # to print the statement like in previous functions, the name of the class must be called before the stement is printed

t3= mylib.scalc3(int(fn),int(sn))           
print(int(fn),(","),int(sn),("-"))
print("the result will be ",t3)
print()
print()                         # then the prior function is called upon to show some calculation that was done in previous assignments




print("Enter OK to see the eight function used")
print()

p7=input()









def __init__(self8, name8,number9):
    self8.name8 = name8
    self8.number9 = number9
                                                #and the last def__init__ is created with the same def myfunct byt different name of the object

def myfunc1(abc7):
      print("When I got " + abc7.name8)


p1 = Priorfunctions(" my last answer after using my last def scalc4() function by dividing the two numbers: ",8)
p1.myfunc1()            #because the myfunct is called upon it will print the same statement, but a different statement in the class

t4= mylib.scalc4(int(fn),int(sn))
print(int(fn),(","),int(sn),("/"))
print("the result will be ",t4)                 #adter the statment is pirnted, the prior function is printed showing the division operant
print()
print()

print()




print("That is all!")        # end the application with the end statement closing the class that was used to show all the prior functions listed with this class
print()
print("These were all the functions that were used !")

print()
print()
end=input()
print()
print()


       









        
        





    

    












        






