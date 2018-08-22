import numpy as np

# Warm Up 1
# Repeat and practice the same exercise that are given in the PowerPoint.
# Write a python program to covert the values of Centigrade into Fahrenheit degree. Print the result after converting.

degree_Cel = [15, 20, 33, 50]
# Create a numpy array from degree_Cel
np_degree_Cel = np.array(degree_Cel)

np_degree_Fah = np_degree_Cel*1.8 +32

print(np_degree_Fah)

# Warm Up 2
# Write a Python Program Using NumPy to interchange the rows of the Matrix into the columns. Print the result for both matrixes.
'''mat1 = np.array([[1, 2, 3],[4, 5, 6]])
print(mat1)

mat2 = np.swapaxes(mat1, 0, 1)
print(mat2)

# shape is different from swapaxes!
# mat1.shape = (3,2)
# print(mat1)

print(type(mat2))
print(mat1.shape)
print(mat2.dtype)'''

# Warm up 3
# Write a Python Program to show if there's an element from the first matrix is existed in the second matrix.
# Print out:
# The location of the common element(s) between the two matrices.
# The Value(s) of the common element(s).
# The Minimum value of the Mat1.
# The Maximum Value of the Mat1 in each columns and rows.
# The mean value of the Mat2 in each row.

'''arr1 = np.array([[10, 20, 30], [40, 50, 60]])
arr2 = np.array([[10, 25, 30], [40, 52, 62]])

# Find the Location of the common elements
print(np.in1d(arr1, arr2))


# The Values of the common elements
print(np.intersect1d(arr1, arr2))

# Mini value of the Mat1
print(np.amin(arr1))

# Maxi value of the Mat1 for each column
print(np.amax(arr1, axis=0))

# Maxi value of the Mat1 for each row
print(np.amax(arr1, axis=1))

# The mean value of the Mat2 in each row.
print(np.mean(arr2, axis=1))'''

# Ex 6
#  Write a Python Program using NumPy and Matplotlib to show the result as the figure below!
'''import matplotlib.pyplot as plt


x = np.arange(0 ,3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(1)
# Plotting the sine curve
plt.subplot(2, 1, 1)
plt.plot(x, y_sin, 'o', color = "green")
plt.title("Sine")

# Plotting the cosine curve
plt.subplot(2, 1, 2)
plt.plot(x, y_cos, '*')
plt.title("Cosine")

# Show the figure
plt.show()'''

# Ex 7
from scipy.misc.pilutil import imsave, imresize, imread, imfilter, imrotate
'''from PIL import Image, ImageFilter

# To read and show an image from the disk
img = Image.open('MindRoad.jpg')
img.show()

#Image Rotate
img.rotate(90).show()

# Image Resize
size = 128, 128
img.resize(size, Image.ANTIALIAS).show()


# To get an image Format, Size and Mode
print(f"Image Format: {img.format}, Image Size: {img.size}, Image Mode: {img.mode}")

# There are many option how to filter an image.
img.filter(ImageFilter.FIND_EDGES).show()


# Save an Image
img_gray = Image.open('MindRoad.jpg').convert('L')

try:
    img_gray.save('MindRoad_Gray.jpg')
    print("Image is saved")
except AttributeError:
    print(f"Couldn't save the image {img_gray}")'''

