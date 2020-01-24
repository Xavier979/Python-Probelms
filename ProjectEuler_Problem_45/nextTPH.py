
# for various polygons.
def getPenta(n):
    return (n*(3*n-1))/2
def getHex(n):
    return n * (2*n - 1)

# The quadratic formula is useful for computing a least polygonal number greater than n.
# For example, to find the least Hexagonal number greater than 30, solve the equation 
# 30 = x(2x-1), which in general form is 0 = 2x^2 - x - 30. If we write the function below 
# to compute the larger of the two solutions to 0=ax^2 + bx + c, then solve_quad(2, -1, -30) 
# will return 4.1310435... so the next Hexagonal number is getHex(5) = 45.

def solve_quad(a, b, c):
    x= (-b+(b**2-4*a*c)**0.5)/(2*a)
    return int(x)

# Now write a function that returns the least TPH number greater than n. 
def nextTPH(n):
    least_index_penta=solve_quad(3,-1,-2*n)+1
    
    index_penta=least_index_penta
    while True:
        value_penta=getPenta(index_penta)
        largest_index_hex=solve_quad(2,-1,-value_penta)+1
        least_index_hex=solve_quad(2,-1,-(value_penta-1))
        for index_hex in range(least_index_hex,largest_index_hex):
            if value_penta==getHex(index_hex):
                return int(value_penta)
        index_penta+=1
    return 0

# Print the output of your function for n=1 and again for n=40754.
print(nextTPH(1))
print(nextTPH(40754))

# Print the output of your function for n=40755.
print(nextTPH(40755))