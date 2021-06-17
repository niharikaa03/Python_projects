#matplotlib is used for plotting purpose
#arrange is used for DEFINING (start,end,difference)
#numpy is used for access trigno fuctions
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,x,z)
plt.show()