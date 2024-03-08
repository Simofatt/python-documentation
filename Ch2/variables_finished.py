# Declare a variable and initialize it
f = 0
print (f)

# re-declaring the variable works
f = "abc"
print (f)



# GLOBAL VS LOCAL 
def someFunction():
 
  global d    #to make the variable global
  d=4
  f = "def"
  print (f)





someFunction()
print (f) 
print(d)

del f

