class History:
    def __init__(self,one = "cs",two=""):
        self.fpart = one
        self.spart = two


name = History("Half life")
name1 = History()
name2 = History("cs","1.6")
name3 = History(two ="go")


print(name.fpart, name.spart)
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print(name1.fpart, name1.spart)
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print(name2.fpart, name2.spart)
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
print(name3.fpart, name3.spart)