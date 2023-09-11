import string # 1 - import the tring module

"""This module will change your normal pass to a Caesar pass code"""

x = input("enter your password : ") # 2 - create a variable
g = ''                              # 3 - make a vacant string
lst = []                            # 3 - make a vacant list >>>>>>>> check ( 8,11 ) 
lw = list(string.ascii_lowercase)   # 4 - create a list for lowercase alphabet
up = list(string.ascii_uppercase)   # 5 - create a list for upercase alphabet

# ------------- we have our lists and strings now ------------- #
for item in x:
    if item in lw :
        index = lw.index(item)      # 6 - the only way to find our variables index 
        r = lw[(index+23)%len(x)]   # 7 - To define the Caesar code, we must add 23 to the index of that strings 
        lst.append(r)               # 8 - we append all lower cases to lst

    if item in up:
        index_2 = up.index(item)    # 9 - the only way to find our variables index
        u = up[(index_2 +23)%len(x)]# 10 - To define the Caesar code, we must add 23 to the index of that strings
        lst.append(u)               # 11 - we append all lower cases to lst

for i in lst:   
    g = g + i                       # 12 - We do this to paste the encrypted letters together
print(g)