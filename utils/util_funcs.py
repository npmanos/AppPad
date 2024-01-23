class classproperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()
    
    # def __set__(self, cls, owner, value):
    #     classmethod(self.fset).__get__(None, owner)(value)
    
    