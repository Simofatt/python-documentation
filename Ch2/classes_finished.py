#
#                                                                            Example file for working with classes
#



#SELF is similar to this in java its a container of the current object

class myClass():
    def method1(self):
        print("myClass method1")

    def method3():
        print("without self")

    def method2(self, someString):
        print("myClass method2: " + someString)




class anotherClass(myClass):


    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")






def main():

    c = myClass()
    c.method1()
    c.method2("This is a string")
    c.method3() 

    c2 = anotherClass()
    c2.method1()








if __name__ == "__main__":
    main()
