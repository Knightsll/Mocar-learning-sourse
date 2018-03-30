from mayavi import mlab
import numpy as np

x, y = np.ogrid[-2:2:20j, -2:2:20j]
z = x * np.exp(-x**2-y**2)

face = mlab.surf(x,y,z,warp_scale =2)
axes = mlab.axes(xlabel = 'x',ylabel = 'y',zlabel = 'z', color = (0,0,0))

outline = mlab.outline(face,color = (0,0,0))
