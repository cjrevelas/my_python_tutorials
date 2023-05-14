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

# Some more options on formatting the plot area
plotTitleFormat = {'fontname': 'Times New Roman', 'fontsize': '24'}
axisLabelFormat = {'fontname': 'Helvetica', 'fontsize': '18'}

x  = range(0,8,1)
y1 = range(0,24,3)
y2 = np.power(x,3)

plt.title("y = f(x)", fontdict = plotTitleFormat)
plt.xlabel("X axis",  fontdict = axisLabelFormat)
plt.ylabel("Y axis",  fontdict = axisLabelFormat)

plt.plot(x, y1, color = 'purple', label = 'y = 3x',  marker = '.', linewidth = 1.5, markersize = 10, linestyle = '--')
plt.plot(x, y2, color = 'red',    label = 'y = x^3', marker = '.', linewidth = 1.5, markersize = 10, linestyle = 'None')

plt.xticks(range(0,8,2))
plt.yticks(range(0,400,100))

plt.tick_params(axis = 'x', direction = 'in', length = 5.0, width = 2.0)
plt.tick_params(axis = 'y', direction = 'in', length = 5.0, width = 2.0)

plt.legend()
plt.show()

exit()
