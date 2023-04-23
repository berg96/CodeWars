#Consider a sequence u where u is defined as follows:
#The number u(0) = 1 is the first one in u.
#For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
#There are no other numbers in u.
#Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
#Task: Given parameter n the function dbl_linear (or dblLinear...) 
#returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).

def dbl_linear(n):
    u = {1}
    for i in range(int(n/2) + 1):
        u.add(i*2 + 1)
        u.add(i*3 + 1)
    new_u = list(u)
    new_u.sort
    print (new_u)
    return new_u[n]

print(dbl_linear(10))