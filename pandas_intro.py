import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Here, we create a dataframe using a python list.
Essentially, we call the constructor of the DataFrame class to
instantiate our object.
'''
simpleList = [
               ['Katerina', 'Constantinos'],
               ['Gae', 'Dimitra'],
               ['Sandy','Mitsos'],
               ['Panagiotis', 'Tim'],
               ['George'],
             ]

frameObject1 = pd.DataFrame(simpleList)

print(frameObject1)
print('\n')
print(frameObject1[0][1])
print('\n')

'''
Here, we create a dataframe using a python dictionary.
'''
simpleDict = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
              'Age' : ['27', '24', '22', '32'],
              'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannuj'],
              'Qualification': ['MsC', 'MA', 'MBA', 'PhD']
             }

frameObject2 = pd.DataFrame(simpleDict)
print(frameObject2)
print('\n')

# We can isolate and work on specific columns of our data frame
print(frameObject2[['Name', 'Address']])
print('\n')

# We can easily check the dimensions and size of our data frame using the 'size' and 'shape' attributes.
print("frameObject2 has " + str(frameObject2.size) + " elements")
print("frameObject2 has shape: ")
print(frameObject2.shape)
print('\n')

'''
Here, we create a dataframe importing data from csv file.
'''
frameObject3 = pd.read_csv("files/nba.csv")
print(frameObject3)
print('\n')
frameObject3.plot(x = 'Name', y = 'Salary', color = 'purple', marker = '.', linestyle = 'dotted')
plt.show()
'''
Another example.
'''
myList = [ [2, 'Catherine', 22], [1, 'Constantinos', 25], [3, 'Panos', 24] ]

# When creating the frame, we can specify the title of each column.
frameObject4 = pd.DataFrame(myList, columns = ['id', 'name', 'age'])
print(frameObject4)
print('\n')
