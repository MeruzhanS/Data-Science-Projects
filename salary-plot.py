import json
import matplotlib.pyplot as plt
import random
import numpy as np
import math

f = open('/Users/meruzhansargsyan/Desktop/Data Science Projects/Salary-Data-2.json')
data = json.load(f)
sampleSize = 200

x = []
xint = []
y = []
randomNums = []

# choose 200
for i in range(sampleSize):
    randomNums.append(random.randint(0, 41967))
    
#populate x
for i in range(len(randomNums)):
    x.append(float(data[str(randomNums[i])]["age"]))
# populate y
for i in range(len(randomNums)):
    y.append(float(data[str(randomNums[i])]["income"]))

for i in x:
    xint.append(int(i))

npX = np.array(x)
npY = np.array(y)

plt.scatter(x,y, label="dot", color=["#D81B60"])
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Income based on age")

#find line of best fit
a, b = np.polyfit(npX, npY, 1)
coeffs =    np.polyfit(npX, npY, 1)
# r calculation
results = {}

p = np.poly1d(coeffs)
yhat = p(npX)
ybar = np.sum(npY)/len(npY)
ssreg = np.sum((yhat-ybar)**2)
sstot = np.sum((y - ybar)**2)
results = ssreg / sstot
print(results)
#add line of best fit to plot
plt.plot(npX, a*npX+b)

plt.show()

