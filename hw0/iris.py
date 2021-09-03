import numpy as np
from matplotlib import pyplot as plt

'''
The iris.names file describes the structure of the dataset. 
How many features/attributes are there per sample?
4
Attribute Information:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm

How many different species are there? 
3
  -- Iris Setosa
  -- Iris Versicolour
  -- Iris Virginica

how many samples of each species did Anderson record?
50 in each of three classes

'''

attribute_array = []
class_array = []
for line in open('iris.data'):
  r = line.split(',')
  if len(r) == 5:
    # N×p array, where N is the number of samples and p is the number of attributes per sample.
    attribute_array.append([float(x) for x in r[:4]])
    # N-dimensional vector containing each sample’s label (species)
    class_array.append(r[4][:-1])
attribute_array = np.array(attribute_array)

print(attribute_array)
print(class_array)

'''
Attribute Information:
   1. sepal length in cm
   2. sepal width in cm
   3. petal length in cm
   4. petal width in cm
   5. class: 
      -- Iris Setosa
      -- Iris Versicolour
      -- Iris Virginica
'''
# Create every possible scatterplot from all pairs of two attributes. 

# Transpose the arr, the same attribute is in the same array
# print(attribute_array.T)
spl_len = attribute_array.T[0]
spl_wdt = attribute_array.T[1]
ptl_len = attribute_array.T[2]
ptl_wdt = attribute_array.T[3]
# setosa-red, versicolor-green, virginica-blue
colors = ["r"] * 50 + ["g"] * 50 + ["b"] * 50

def plot_scatter(pos, x, y):
  plt.subplot(4, 4, pos)
  plt.scatter(x, y, c=colors,s=3)
  plt.tick_params(labelsize=5)

def plot_text(pos, text):
  plt.subplot(4, 4, pos)
  plt.text(0.5, 0.5, text, fontsize=10, verticalalignment='center', horizontalalignment='center')
  plt.tick_params(bottom=False,top=False,left=False,right=False)
  plt.tick_params(labelbottom=False,labeltop=False,labelleft=False,labelright=False) # remove the scale

#-----------------
plot_text(1, 'Sepal.Length')

# sepal width vs sepal length
plot_scatter(2, spl_wdt, spl_len)

# petal length vs sepal length
plot_scatter(3, ptl_len, spl_len)

# petal width vs sepal length
plot_scatter(4, ptl_wdt, spl_len)

#------------------
# sepal length vs sepal width
plot_scatter(5, spl_len, spl_wdt)

plot_text(6, 'Sepal.Width')

# petal length vs sepal width
plot_scatter(7, ptl_len, spl_wdt)

# petal width vs sepal width
plot_scatter(8, ptl_wdt, spl_wdt)

#------------------
# sepal length vs petal length
plot_scatter(9, spl_len, ptl_len)

# sepal width vs petal length
plot_scatter(10, spl_wdt, ptl_len)

plot_text(11, 'Petal.Length')

# petal width vs petal length
plot_scatter(12, ptl_wdt, ptl_len)

#------------------
# sepal length vs petal width
plot_scatter(13, spl_len, ptl_wdt)

# petal length vs petal width
plot_scatter(14, spl_wdt, ptl_wdt)

# petal width vs petal width
plot_scatter(15, ptl_len, ptl_wdt)

plot_text(16, 'Petal.Width')

# add title
plt.suptitle('Iris Data(red=setosa,green=versicolor,blue=virginica)', fontsize=10)
plt.savefig("plot.png")
plt.show()
