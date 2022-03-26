# class Test:
#     def __init__(self,x,y,z):
#         print("constructors.......")
#         self.name= x
#         self.rollname = y
#         self.dob = z

#     def display(self):
#         print("display method......")
#         print("Studen_name:{}\nStuden_rollname:{}\nStudent_dob:{}".format(self.name,self.rollname,self.dob))


# obj = Test("vivek",100,15)
# obj.display()


class Test2:
    def __init__(self):
        self.name = "vivek"
        self.rollname  = 120



obj = Test2()
print(obj.__dict__)