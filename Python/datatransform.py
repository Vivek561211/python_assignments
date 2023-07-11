#converting rupees into dollar
def dollar(salary):
    a=salary/81.80
    return a

salary=int(input("Enter your salary:"))
print(dollar(salary))