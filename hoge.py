import numpy as np
import pylab
import matplotlib.pyplot as plt

def onclick(event):
    print('event.button=%d,  event.x=%d, event.y=%d, event.xdata=%f, \
    event.ydata=%f'%(event.button, event.x, event.y, event.xdata, event.ydata))

fig=plt.figure()
ax=fig.add_subplot(111)
cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
