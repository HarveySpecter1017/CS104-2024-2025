import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[5,6,7,8]
##For basic plots:
plt.plot(x,y,color='red',marker='o',label='hello')
plt.title('hey')
plt.xlabel("wow")
plt.ylabel("huh")
plt.xlim(0,5)
plt.grid(True)
plt.legend(loc='upper right')
##use plt.savefig("hey.png") to save as file
plt.show()
##for a scatter plot:
##matplotlib.pyplot.scatter(x, y, s=None, c=None, *, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=None, colorizer=None, plotnonfinite=False, data=None, **kwargs)
plt.scatter(x,y,alpha=0.7) ##alpha is opacity value
plt.show()
###for a bar plot:
###matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)[source]
plt.bar(x,height=y,width=0.8) ##width is fraction of separation
plt.show()
###for a pie plot:
###matplotlib.pyplot.pie(x, *, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False, rotatelabels=False, normalize=True, hatch=None, data=None)[source]
plt.pie(x,labels=['a','b','c','d'],colors=['r','b','g','y']) ##all values of explode are less than 1
plt.show()
####for a histogram:
##matplotlib.pyplot.hist(x, bins=None, *, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, data=None, **kwargs)[source]
plt.hist([1,2,2,2,2,3,4,4,4,4,4,5],bins=5)
plt.show()