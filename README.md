# How-Many-Singular-Values
In this repository, will be shown a program made with python which receive an image once called and defines how many singular values are necessary to decompose the image in function of the selected quality.
The image, once read by the program, will be converted into grayscale in order to only have one dimension per pixel, and will then be converted into a numpy array which will be used for SVD. 
The idea on which the program is based, is that the eigenvalues of the SVD are ordered in function of their variance where the first one represent the highest variance of the decomposed image.
According to that, the amount of singular values needed to represent correctly the decomposed image may be found in function of a rateo between the first eigenvalue and the other ones, cutting all the ones for which sv[i]/sv[0] < prec.
In the directory, has been loaded the output in function of the selected quality both for a kitten image and for a modern art image.
It may be observed from the output how the number of singular values needed suddenly increase while dealing with the modern art image respect to the kitten one, de facto, the second one has obviously a greater variance and quantity of information implicitly contained in that.
