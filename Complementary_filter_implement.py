# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:20:10 2020

@author: kanno
"""
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# input file path
file_path_i = "input/腕振り　スロー　右手系.csv"
# output file path
file_path_o = "output/腕振り　右手系_euler_test1.csv"
# save image path
img_path_o = "image com/腕振り　スロー　右手系.png"

csv_input1 = pd.read_csv(filepath_or_buffer= file_path_i, encoding="ms932", sep=",")
array = csv_input1.values

time = array[:,0]
acc = array[:,1:4]
gyro_deg = array[:,4:7]
gyro = gyro_deg * (np.pi/180)
dt = 1/20

euler_z = []
euler_z.append(180)
for i in range(1,len(gyro)):
    angleAcc = math.degrees(math.atan(-acc[i,0]/math.sqrt(acc[i,1]**2+acc[i,2]**2)))
    new_euler_z = (euler_z[i-1] + gyro_deg[i,2] * dt)*0.95 + angleAcc*0.05
    euler_z.append(new_euler_z)

# plot
plt.plot(euler_z)
#plt.show()
plt.savefig(img_path_o)

