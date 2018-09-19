prompt= " Welcome to the calculator please type your first number: "
x = float(input(prompt))
prompt = "Type your second number: "
y = float (input(prompt))

addition = eval("x+y")
subtraction = eval("x-y")
multiplication = eval("x*y")
division = eval("x/y")

print(addition)
print(subtraction)
print(multiplication)
print(division)