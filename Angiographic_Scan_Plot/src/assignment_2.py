from matplotlib import pyplot as plt
import numpy as np
import math 
import statistics
#Reading data from the file and reshaping it into 512 * 512 matrix
angioScan = np.fromfile("slice150.raw",dtype='int16',sep="")
angioScan = angioScan.reshape([512,512])
# plt.imshow(Angio_Scan)
# plt.show()

######################################################################
#a: Profile line
######################################################################
for i in range(len(angioScan)):
	if i == 254:
		profileList = angioScan[i]
		break
plt.title('Profile Line')
plt.plot(profileList)
plt.show()

######################################################################
#b: Calculating the mean and variance of the matrix
######################################################################
print("Variance: ", np.var(angioScan))

print("Mean: ", np.mean(angioScan))
######################################################################
#c: Histogram 
######################################################################
u,c = np.unique(angioScan,return_counts=True)
plt.title('Line Graph')
plt.plot(u,c)
plt.show()

######################################################################
#d: Rescaling using Linear Transformation
######################################################################
def linearTransform(angioScan):
	#T(r)=((r - rmin))/(rmax-rmin)*Smax
	Smax = 255
	rmin,rmax = 99999999,0
	for row in angioScan:
		for col in row:
			if col > rmax:
				rmax = col
			elif col < rmin:
				rmin = col 
	n = len(angioScan)
	linMatrix = np.zeros((n,n))
	def lt(r):
		return int(((r - rmin))/(rmax - rmin)*Smax)
	for i in range(0,n):
		for j in range(0,len(angioScan[i])):
			linMatrix[i][j] = lt(angioScan[i][j])
	return linMatrix

linMatrix = linearTransform(angioScan)
plt.title('Linear Transformation')
plt.imshow(linMatrix)
plt.show()


######################################################################
#e: Rescaling using Non-Linear Transformation
######################################################################
def nonlinear(angioScan):
	n = len(angioScan)
	nonLinMatrix = np.zeros((n,n))
	def nlt(r):
		return (r+1)**2
	for i in range(0,n):
		for j in range(0,len(angioScan[i])):
			nonLinMatrix[i][j] = nlt(angioScan[i][j])
	return nonLinMatrix

nonLinMatrix = nonlinear(angioScan)
plt.title('Non-Linear Transformation')
plt.imshow(nonLinMatrix)
plt.show()

#####################################################################
#f: 11*11 Box Car Smoothing
#####################################################################
def boxCarMatrix(angioScan, i, j, boxCarFilter):
	sum = 0
	for row in range(i,i+11):
		for col in range(j, j+11):
			sum = sum + angioScan[row][col]
	retVal = len(boxCarFilter) * len(boxCarFilter)
	return (sum/retVal)

def visualiseBoxCarFilteredData(angioScan, boxCarFilter, outMatrix):
	
	for i in range(0,len(angioScan)):
		#checking for row limit
		if((len(angioScan)-i)>(len(boxCarFilter)-1)):
			for j in range(0,len(angioScan[i])):
				if((len(angioScan[i])-j)>(len(boxCarFilter)-1)):
					midVal = boxCarMatrix(angioScan, i , j, boxCarFilter)
					outMatrix[i][j] = midVal
				
boxCarFilter = np.zeros((11,11))
outMatrix = np.zeros((512,512)) 
visualiseBoxCarFilteredData(angioScan,boxCarFilter,outMatrix)
plt.title('Box Car Smoothing Filter')
plt.imshow(outMatrix)
plt.show()

#####################################################################
#g: 11*11 Median Filter
#####################################################################
def medianFilterMatrix(angioScan, i, j):
	#sort the matrix to replace it with the median value 
	medianList = []
	for row in range(i, i+11):
		for col in range(j, j+11):
			medianList.append(angioScan[row][col])
	return statistics.median(medianList)

def visualiseMedianFilteredData(angioScan, medianFilter, medMatrix):
	
	for i in range(0,len(angioScan)):
		#checking for row limit
		if((len(angioScan)-i)>(len(medianFilter)-1)):
			for j in range(0,len(angioScan[i])):
				if((len(angioScan[i])-j)>(len(medianFilter)-1)):
					midVal = medianFilterMatrix(angioScan, i , j)
					medMatrix[i][j] = midVal
				
medianFilter = np.zeros((11,11))
medMatrix = np.zeros((512,512)) 
visualiseMedianFilteredData(angioScan,medianFilter,medMatrix)
plt.title('Median Filter')
plt.imshow(medMatrix)
plt.show()

######################################################################

