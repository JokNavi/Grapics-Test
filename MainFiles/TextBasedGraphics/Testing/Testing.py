import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()

def PrintScreen():
    Line = ["a","a","a","a","a","a","a","a","a","a","a","a"]
    gameVisuals = {1:Line, 2:Line, 3:Line, 4:Line, 5:Line}
    for key, value in gameVisuals.items():
        print(*value, sep="")

def LowerFrame():
    lower = 10
    lowerList = [" " for _ in range(lower)]
    print(*lowerList, sep="\n")
    