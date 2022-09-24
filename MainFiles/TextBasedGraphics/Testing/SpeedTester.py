import time
import math

start_time = time.perf_counter()

#y in circle
y = 2
#radius
r  = 5

#formula
#x**2 = r**2 - y**2

print(int((r**2 - y**2)**(1/2)))

print("My program took", time.perf_counter() - start_time, "to run")