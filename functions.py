# function with no arguments and no return


A =10

def sayhello():
    print("hello")


# interest loans

def emi(principal, rate, time=10):
    global rate1, time1
    rate1 = rate/100
    time1 = time*12
    emi = principal*(1+rate1*time1)
    return emi


# person 1 , 10000 at 3% 12 months

person_1 = emi(1000, 0.3, 1)
print(rate1)
print(person_1)

# scope of variables

