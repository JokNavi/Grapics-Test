import time

start_time = time.time()

def LowerFrame(lower):
    lowerList = []
    for _ in range(lower):
        lowerList.append(" ")
    print(*  lowerList, sep ="\n")

def LowerFrameTwo(lower):
    lowerList = [" " for Counter in range(lower)]
    print(*  lowerList, sep ="\n")

LowerFrameTwo(30)
print("My program took", time.time() - start_time, "to run")