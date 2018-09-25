try:
    gross = int(input("Gross: "))
    kids = int(input("Kids: "))
except:
    print("Invalid input")

if gross < 1000:
    tax = 0.1 - (0.01*kids)
elif gross < 2000:
    tax = 0.12 - (0.005*kids)
elif gross < 4000:
    tax = 0.14 - (0.005*kids)
else:
    tax = 0.18 - (0.005*kids)

net = gross * (1-tax)
print("The net is: ", net)