import logging
import numpy as np
print(np.__version__)
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

print('')
arrZero = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('Last element from 2nd dim: ', arrZero[1, -1, 2])

#new array specified type
arrThree = np.array([1, 2, 3, 4], dtype='i4')
print(arrThree.dtype)

#Converting Data Type on Existing Arrays
arrThree = np.array([1, 0, 3])
arrThreeCopy = arrThree.copy()
arrThreeView = arrThree.view()
arrThreeView[2] = 31
newarrThree = arrThree.astype(bool)
print(f'\n{arrThree}')
print(newarrThree)
print(newarrThree.dtype)
print(arrThreeCopy)
print(newarrThree.base)
print(arrThreeView)
print(arrThreeView.base)


arrFour = np.array([1, 2, 3, 6, 8], ndmin=5)
print(f'\n{arrFour}')
print('shape of array :', arrFour.shape)

arrFive = np.array([[1, 2, 3], [4, 5, 6]])
newArrFive = arrFive.reshape(-1)
print(newArrFive)

arrSix = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arrSix[:, ::2], flags=['buffered'], op_dtypes=['S']):
  print(x)

for idx, x in np.ndenumerate(arrSix):
  print(idx, x)


arrSeven = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newArrSeven = np.where(arrSeven == 4)
print(newArrSeven)