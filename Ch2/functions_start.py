#
# Example file for working with functions
#

def main(): 
    x,y = 2,2 
    func(x,y)
    func1(x,y)

def func(x,y): 
    print('heelo im func1')  
    if(x<y): 
        print('x is greater than y') 
    elif (x>y) : 
        print("y is greater than x") 
    else : 
        print("maybe they are equals")



def func1(x,y):
    
    st="hello" if (x<y) else  "idont know" ; 
    print(st)






if __name__ == "__main__":
    main()




       




