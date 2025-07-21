import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [2,4,6,8,10,2]
plt.plot(x,y)
plt.title('Line plot')
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.show()

# Bar chart
a = ['A', 'B', 'C']
b = [5,7,9]
plt.bar(a,b)
plt.title('Bar plot')
plt.show()