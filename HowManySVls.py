# This program, once called will load the first argument of the call as the image to analyze, 
# and will esteem in function of the required precision how many singular values are necessary for the decomposition

import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

plt.style.use('grayscale')
img = Image.open(sys.argv[1])

# Convert image to grayscale in order to have only one dimension per pixel

imggray = img.convert('LA')

# Convert the image to a numpy array, in order to create a matrix containing the pixels information

imgarr = np.array(list(imggray.getdata(band=0)),float)

imgarr.shape = (imggray.size[1],imggray.size[0])

#Decomposing the image

U,D,V = np.linalg.svd(imgarr)

# Asking for the decomposition quality

opt = 0
while(opt == 0):

	inputstring = "Choose the output quality between low[l],medium[m] or high[h] :"
	Qual = raw_input(inputstring)

	if((Qual == 'l') or (Qual =='L')):

		prec = 0.05
		opt = 1

	if((Qual == 'm') or (Qual =='M')):

		prec = 0.01
		opt = 1	

	if((Qual == 'h') or (Qual =='H')):

		prec = 0.001
		opt = 1

# Finding the best number of singular value according to the selected precision

i = 0
MaxVal = D[i]

while((D[i]/MaxVal)>prec):

		i += 1

inputstring = "According to the selected precision, the program needed  {0} singular values among {1} total values to reconstruct the image.".format(i,len(D))
print(inputstring)

#Image reconstruction with i singular values

reconstrctimg = np.matrix(U[:, :i])*np.diag(D[:i])*np.matrix(V[:i, :])

# Plotting the obtained figures

print("Here is a comparation between the starting image and the decomposed image :")

plt.figure(figsize = (9,6))

plt.subplot(1,2,1)
plt.imshow(imgarr, cmap='gray')
title = "original image"
plt.title(title)

plt.subplot(1,2,2)
plt.imshow(reconstrctimg, cmap ='gray')
title = "reconstructed image"
plt.title(title)
plt.show()