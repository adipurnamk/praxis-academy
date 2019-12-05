class employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        
    def tampil(self):
        return "{} {}".format(self.first , self.last)


emp1=employee("abdul","anwar")
print(emp1.tampil())