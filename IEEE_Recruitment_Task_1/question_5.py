#Task: Generate numbers from a normal distribution a plotting a scatter plot using matplotlib.

#Normal Distribution is a type of distribution which takes the form of a bell curve.
#The idea is that most values are closer to top of the bell curve, the mean and fewer values are on the slopes, and least are on the extremas.*/
# One gets this graph considetring the mean and standard deviation of the data.
# Many distributions normally take this form.
#Resources used: Chatgpt and wikipedia to understand normal distribution and "https://www.youtube.com/watch?v=zZZ_RCwp49g" for understanding scatter plots

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("seaborn-v0_8")                     #uses the style of seaborn data visualisation library for the plot

x= np.random.normal(0,1,1000)                     #Generates 1000 random numbers with mean 0 and standard deviation 1.
y= np.random.normal(0,1,1000)

plt.scatter(x,y,s=25,alpha=0.75,c='red',edgecolors='black',linewidth=1) 

#scatters x and y. s sets dot size, alpha sets transparency, c sets dot colour, edgecolors sets border color of dots, linewidth sets thickness of border.

plt.grid(True)                                                                             #activates grid

plt.title("Scatter plot of normally distributed random numbers",fontsize=20,c='teal')      #Title of the plot with size and color
plt.xlabel("Random Variable X Normal Distribution",fontsize=15,c='red')                    #x-axis label with size and color
plt.ylabel("Random Variable Y Normal Distribution",fontsize=15,c='red')                    #y-axis label with size and color

plt.show()

#we are getting a scatter cloud here because both variables are random.


