import matplotlib.pyplot as plt

x_values = list(range(1,1001))

y_values= [x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Greens,edgecolor='none',s=40)

#Set the chart title and label axes.
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#Set the tange of each axis.
plt.axis([0,1100,0,1100000])
#Set size of tick labels
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()