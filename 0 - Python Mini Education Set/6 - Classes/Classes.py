## The logic of the classes was transferred with the code.
from __future__ import print_function
class MyClass:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.__privateValue = "private value"
    
    def printing(self):
        print(""" 
            printing function
              name: {}
              number: {}
              {}
        """.format(self.name, self.number, self.__privateValue))
    
    def makePrivateAcessible(self, publicValue):
        self.__privateValue = publicValue

    def OutSideFunc(self):
        print("Outside Function")
        nesne = MyClass(name="my name", number=12)
        nesne.printing()
        nesne.makePrivateAcessible("publi value")
        nesne.printing()
        nesne.OutSideFunc()