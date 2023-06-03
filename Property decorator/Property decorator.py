import random

class AWS_school:
    no_lst=[]
    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.__trans_ID=""

    @property
    def ID_num(self):
        alpha=self.first[:4]
        rand_num=int()
        i=0
        while i<=2:
            rand_num=rand_num+random.randint(0,10)
            if i==3:
                if rand_num not in self.no_lst:
                    self.no_lst.append(rand_num)
                else:
                    i-=1
                    continue
            i+=1
        return f"AWS{alpha.upper()}{rand_num}"

    @property
    def school_email(self):
        return f"{self.first}{self.last}@AWS.com"

    @school_email.setter
    def school_email(self,name):
        self.first,self.last=name.split(",")

    @property
    def trans_ID(self):
        for i in range(8):
            self.__trans_ID=self.__trans_ID+str(random.randint(0,9))
        return self.__trans_ID





student_1=AWS_school("Ali","shah")
print(student_1.ID_num)
print(student_1.school_email)
student_1.school_email="Mustafa,kazmi"
print(student_1.school_email)
print(student_1.trans_ID)

