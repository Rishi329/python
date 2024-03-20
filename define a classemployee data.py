#
class employee:
    eno=0
    enm=""
    salary=0
    
    def getdata(self):
        self.eno=int(input("Enter EMP NO="))
        self.enm=(input("Enter EMP Name="))
        self.salary=int(input("Enter Salary="))
    def putdata(self):
        print("Employee no=",self.eno)
        print("Employee EMP no=",self.enm)
        print("Employee salary=",self.salary)
e1=employee();
e1.getdata()
e1.putdata()