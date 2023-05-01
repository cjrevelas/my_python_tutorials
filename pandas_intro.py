import pandas as pd
import matplotlib.pyplot as plt

# Here, we create a simple dataframe importing a python list
simpleList = [
               ['Katerina', 'Constantinos'],
               ['Gae', 'Dimitra'],
               ['Sandy','Mitsos'],
               ['Panagiotis', 'Tim'],
               ['George'],
               ]


# We call here the constructor of the class DataFrame to create a new object
# for our data

frameObject1 = pd.DataFrame(simpleList)

print(frameObject1)

print('\n')
print('\n')

print(frameObject1[0][1])


# Here, we create a simple dataframe importing a python dictionary/hash
simpleDict = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
              'Age' : ['27', '24', '22', '32'],
              'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannuj'],
              'Qualification': ['MsC', 'MA', 'MBA', 'PhD']
           }

print('\n')
print('\n')

frameObject2 = pd.DataFrame(simpleDict)
print(frameObject2)

print('\n')
print('\n')

#print(frameObject2[['Name', 'Address']])

print("frameObject2 has " + str(frameObject2.size) + " elements")
print("frameObject2 has shape: ")
print(frameObject2.shape)

frameObject3 = pd.read_csv("nba.csv")
frameObject3.plot(x = 'Name', y = 'Salary', color = 'purple', marker = '.', linestyle = 'dotted')
print(frameObject2)
#frameObject2.plot(x = 'Name', y = 'Age')
plt.show()



















