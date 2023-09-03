"""module docstring
You must change this module doc
"""




def fib (n):
    """method docstring"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def fac(n):
    if n==1 or n==0:
        return 1
    else:
        return n *fac(n-1)

num=int(input("put the number here : ")) 

print(fac(num))
print(fib(num))