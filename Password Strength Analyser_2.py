#Library 
import string as str
#For repetation
i = "y"
while i == "y" or i == "Y" :
    print("Enter a Password and check its Strength.")
    #Tacking Input
    password = input("Enter a Password =")
    # For checking if Password Entered is empty or not
    val = password if password else None
    if val is not None :
        rating = 0
        # For 8 char
        no_of_char = len(password)
        print("Minimum 8 Characters Pass" if no_of_char >= 8 else "Minimum 8 Characters Fail")
        if no_of_char >= 8 :
            rating +=1
        # For Uppercase
        has_upper = any(char.isupper() for char in password)
        print("Upper case is present" if has_upper == True else "Upper case is not present")
        if has_upper == True :
            rating +=1
        # For Lowercase    
        has_lower = any(char.islower() for char in password)
        print("Lower case is present" if has_lower == True else "Lower case is not present")
        if has_lower == True :
            rating +=1
        # For Digit   
        has_decimal = any(char.isdecimal() for char in password)
        print("Digit is present" if has_decimal == True else "Digit is not present")
        if has_decimal == True :
            rating +=1
        # For Special Character
        has_special = any(char in str.punctuation for char in password)
        print("Special Character is present" if has_special == True else "Special Character is not present")
        if has_special == True :
            rating +=1
        # For Space 
        has_space = any(char.isspace() for char in password)
        print("Space is present" if has_space == True else "Space is not present") 
        if has_space == True :
            rating -=1
            
        print("The Password is "rating "Out of 5.")        

    else :
        print("The Password has not been Entered.")

    i = input("Enter y if you want to repeat and n if not :")




        
        
