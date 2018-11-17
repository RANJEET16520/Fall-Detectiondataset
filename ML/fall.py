# Modules
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt  
data = pd.read_csv('falldeteciton.csv')

# Functions
# --Activitity
a = np.array(data['ACTIVITY'][:])
b = np.array(list(set(a)))

for i in a:
    b[i]+=1
y = b
x = len(y)
x = range(x)
width = 1/1.5
plt.bar(x,y,width,color="blue")
plt.xlabel("Activity")
plt.ylabel("Range")
plt.show()

# --Time
a = np.array(data['TIME'][:])
y = a
x = len(y)
x = range(x)
width = 1/1.5
plt.bar(x,y,width,color="blue")
plt.xlabel("Time")
plt.ylabel("Range")
plt.show()

# --Sugar Level
a = np.array(data['SL'][:])
y = a
x = len(y)
x = range(x)
width = 1/1.5
plt.bar(x,y,width,color="blue")
plt.xlabel("Sugar Level")
plt.ylabel("Range")
plt.show()

# --EEG
a = np.array(data['EEG'][:])
y = a
x = len(y)
x = range(x)
width = 1/1.5
plt.bar(x,y,width,color="blue")
plt.xlabel("EEG Level")
plt.ylabel("Range")
plt.show()

# --BP
a = np.array(data['BP'][:])
y = a
x = len(y)
x = range(x)
width = 1/1.5
plt.bar(x,y,width,color="blue")
plt.xlabel("Blood Pressure Level")
plt.ylabel("Range")
plt.show()

# --HR
a = np.array(data['HR'][:])
y = a
x = len(y)
x = range(x)
width = 1/1.5
plt.bar(x,y,width,color="blue")
plt.xlabel("HR Level")
plt.ylabel("Range")
plt.show()

# --Circulation
a = np.array(data['CIRCULATION'][:])
y = a
x = len(y)
x = range(x)
width = 1/1.5
plt.bar(x,y,width,color="blue")
plt.xlabel("Circulation")
plt.ylabel("Range")
plt.show()