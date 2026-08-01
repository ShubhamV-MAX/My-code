
#Armstrong Number
import sys 
ex = True
while ex == True :
    no=int(input("Enter an Armstrong Number ="))                #storing the number in the variable "no"
    temp=no                                                     #using the "temp" variable as areferance
    l=len(str(no))                                              #using the length module
    iteration = range(l)                                        #using range datatype for iteration
    arm = 0                                                     #for initial sum 
    for i in iteration:                                         #condition for loop
        r=no%10                                                 #for calculation purpose r=ls,r=2ndls,...,r=2ndms,r=ms
        arm = arm + r**l                                        #main calculation
        no=no//10                                               #for selecting single digits from given number
        continue                                                #for re-checking the condition
    if temp == arm :                                            #main reason of code
        print("The Number",temp,"is an Armstrong Number")
    else :                                                      #if we are not good at assumptions
        print("The Number",temp,"is not an Armstrong Number")

    ex=input("If you want to try again press 'y' if not then press 'n' = ")
    if "y" == ex :
        ex = True
    else :
        exit
    
