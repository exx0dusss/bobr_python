class System:
    os1 = "windows"
    ver1 = "1909"
    os2 = "mac os"
    ver2 = "10.15"
    os3 = "linux"
    ver3 = "5.5.9"
    date = "2019"
    def changeos(self,newos):
        self.os1 = newos
        self.os2 = newos
    def changesys(self,newsys):
        self.ver2 = newsys
        self.ver1 = newsys
        self.ver3 = newsys
    def changedate(self,newdate):
        self.date = newdate
        self.date = newdate
        self.date = newdate
obj1 = System()
obj2 = System()
obj3 = System()
print (obj1.os1, obj1.ver1)
print (obj2.os2, obj2.ver2) 
print (obj3.os3, obj3.ver3)
print (obj1.os1, obj1.date)
print (obj2.os2, obj2.date) 
print (obj3.os3, obj3.date)
obj1.changeos("windows")
obj2.changeos("mac os")
obj1.changesys("10") 
obj2.changesys("Catalina")
obj3.changesys("kernel")
print ("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print (obj1.os1, obj1.ver1)
print (obj2.os2, obj2.ver2)
print (obj3.os3, obj3.ver3)
print ("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
obj1.changedate("2020")
obj2.changedate("2020")
obj3.changedate("2020")
print (obj1.os1, obj1.date)
print (obj2.os2, obj2.date)
print (obj3.os3, obj3.date)