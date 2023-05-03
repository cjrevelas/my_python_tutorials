import matplotlib.pyplot as plt
import numpy as np

x_axis = np.linspace(0, 10, 1000)

y_axis1 = np.linspace(0, 20, 1000)
y_axis2 = np.linspace(0, 40, 1000)
y_axis3 = np.sin(x_axis)
y_axis4 = np.cos(x_axis)

myFigure = plt.figure()

plt.plot(x_axis, y_axis1, color = 'purple', label = 'line 1')
plt.plot(x_axis, y_axis2, color = 'red',    label = 'line 2')
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.title('Just two lines')
plt.legend()
plt.show()

myFigure2 = plt.figure()

plt.plot(x_axis, y_axis3, color = 'purple', label = 'sin')
plt.plot(x_axis, y_axis4, color = 'red',    label = 'cos')
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.title('Trigonometric functions')
plt.legend()
plt.show()

myFigure3, axes = plt.subplots(2)
axes[0].plot(x_axis, y_axis3, color = 'red')
axes[1].plot(x_axis, y_axis4, color = 'orange')
plt.show()
