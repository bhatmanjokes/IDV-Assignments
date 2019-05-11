from mpl_toolkits.mplot3d import axes3d
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import math
#read the file into a list
x1,y1,z1,u1,v1,w1 = [],[],[],[],[],[]
x2,y2,z2,u2,v2,w2 = [],[],[],[],[],[]
x3,y3,z3,u3,v3,w3 = [],[],[],[],[],[]
x4,y4,z4,u4,v4,w4 = [],[],[],[],[],[]

with open('field2.irreg') as f:
    # removing the initial six values to get rid of them
    for i in range (0,6):
        a = f.readline()
    line = f.readline()
    
    while(line):
        temp = line.split(" ")
        tempx1 = float(temp[0])
        tempy1 = float(temp[1])
        tempu1 = float(temp[3])
        tempv1 = float(temp[4])
        length = math.sqrt(((tempu1)**2)+((tempv1)**2))
        if(length <0.25):
            x1.append(float(temp[0]))
            y1.append(float(temp[1]))
            z1.append(float(temp[2]))
            u1.append(float(temp[3]))
            v1.append(float(temp[4]))
            w1.append(float(temp[5]))
        elif(length >=0.25 and length < 0.50):
            x2.append(float(temp[0]))
            y2.append(float(temp[1]))
            z2.append(float(temp[2]))
            u2.append(float(temp[3]))
            v2.append(float(temp[4]))
            w2.append(float(temp[5]))
        else:
            x3.append(float(temp[0]))
            y3.append(float(temp[1]))
            z3.append(float(temp[2]))
            u3.append(float(temp[3]))
            v3.append(float(temp[4]))
            w3.append(float(temp[5]))
 
        line = f.readline()


fig, ax = plt.subplots(figsize=(7,7))

ax.quiver(x1,y1,u1,v1,scale = 3,pivot='mid',color='blue')
ax.quiver(x2,y2,u2,v2,scale = 3,pivot='mid',color='black')
ax.quiver(x3,y3,u3,v3,scale = 3,pivot='mid',color='gray')
ax.quiver(x4,y4,u4,v4,scale = 3,pivot='mid',color='orange')
ax.set_title('Direction_of_Water_Plot')
ax.set_aspect('equal')
ax.use_sticky_edges = False

cmap = mpl.colors.ListedColormap(['blue','black','gray'])
cax = fig.add_axes([0.75,0.075,0.07,0.85])
color_base = mpl.colorbar.ColorbarBase(cax,cmap = cmap,orientation = 'vertical')
color_base.set_ticks([0.2,0.6,0.9])
color_base.set_ticklabels(['Low', 'Medium', 'High']) 
color_base.set_label('Velocity')

plt.tight_layout()
plt.show()