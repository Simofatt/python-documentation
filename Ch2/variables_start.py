# 
# Example file for variables
#

# Declare a variable and initialize it

f=0 


# re-declaring the variable works



# ERROR: variables of different types cannot be combined



# Global vs. local variables in functions

def vari():
    f="def" 
    print(f)


vari()             #if you call the method f variable will change to def the global one as well 
print(f)