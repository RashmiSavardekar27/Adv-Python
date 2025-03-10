""" # Print a statement
print("Welcome to the class.")
for i in range(1,25):
    print(f"print this line {i}") """
def add(x,y):
    '''
    Inputs : take 2 inputs x & y
    outputs : Returns addition of x & y'
    '''
    add=x+y
    return add
op_xy=add(2,5)
print(f"addition of two numbers is {op_xy}")

def simple_interest(p,n,r):
    '''
    input= take inputs for principal amount,number of years,rate of interest
    output=display simple interest
    '''
    if isinstance(p,int|float) and isinstance(n,int|float) and isinstance(r,int|float):
        si=(p*n*r)/100
        return si
    else:
         print("Please provide integer/float data for respective inputs ")

simp_intr = simple_interest(25000,6,5.4)
print(f"output of simple interest function:{simp_intr}")