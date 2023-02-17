''' Iteration 0
class myperson:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
    def GetName(self):
        self.AskedForName = True
        return self.name

print(myperson("Mike", 32, "m").GetName())
'''
''' Iteration 1 
class MyPerson:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.asked_for_name = False

    def get_name(self):
        self.asked_for_name = True
        return self.name
    
print(MyPerson("Mike", 32, "m").get_name())

'''
''' Iteration 2 '''
class MyPerson:
    def __init__(self, name, Age, gender):
        self.name = name
        self.Age = Age # pylint: disable=invalid-name
        self.gender = gender
        self.asked_for_name = False

    def get_name(self):
        self.asked_for_name = True
        return self.name
    
    def get_age(self):
        return self.Age

print(MyPerson("Mike", 32, "m").get_name())
