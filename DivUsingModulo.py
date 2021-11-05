# Impliment division without using division operator. Function should return a tuple of (dividend, remainder) & should take two numbers, product and divisor. 

#Exampled divide(10,3) returns (3,1). 

def divide(product, divisor):
    remainder = (product % divisor)
    newproduct = product - remainder
    count = 0
    while newproduct != 0:
        newproduct -= divisor 
        count += 1
    return (count, remainder)
    
x = divide (25,3) 
print (x)
