
def calculate():

    operations= input('''
Please Type the math operation you want to perform
+ for addition
- for substraction
* for multiplication
/ for division 
''')



    num_1=float(input("Enter first number:"))
    num_2=float(input("Enter second number"))

    if operations=='+' :
        print('{} +{} = '.format(num_1,num_2))
        print(num_1+num_2)
    elif operations=='-' :
        print('{} -{} = '.format(num_1,num_2))
        print(num_1-num_2)
    elif operations=='*' :
        print('{} *{} = '.format(num_1,num_2))
        print(num_1*num_2)
    elif operations=='/' :
        print('{} /{} = '.format(num_1,num_2))
        print(num_1/num_2)

    else:
        print("You have entered a wrong operator")
    again()
def again():
    calculation_again= input('''
    Do you want to calculate again?
    Please type Y for yes and N for no
    ''')

    if calculation_again== 'Y' or calculation_again=='y':
        calculate()
    elif calculation_again =='N' or calculation_again =='n':
        print("Bye ...Thankyou for visiting...")
    else :
        again()

calculate()