try:
    prompt= "please type a number as a numerator"
    number1 = input(prompt)
    num2= input("please type a second number as a denominator")
    division = number1/num2
    print("The division result is: ",division)
except:
    ValueError:
        print("Please type a correct number")
except:
    ZeroDivisionError:
    print("You cannot divide by 0")