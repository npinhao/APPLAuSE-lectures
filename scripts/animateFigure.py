# Visualization routines:
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def initFigure():
  """Sets the figure for the trajectories"""
  
  line1.set_data([], []); line1b.set_data([], [])
  line2.set_data([], []); line2b.set_data([], [])
  # Legibility
  ax.set_title("Trajectories",fontsize=18)
  ax.set_xlabel("X Axis",fontsize=16); ax.set_ylabel("Y Axis",fontsize=16)
  ax.text(18,8,"$\\odot\\,\\vec{B}$", fontsize=20)
  return line1, line1b, line2, line2b

def animate(i,re,rp):
  """Plots the trajectories in (x,y) for i"""
  
  line1b.set_data(re[:i,0],re[:i,1]); line1.set_data(re[i,0],re[i,1])
  line2b.set_data(rp[:i,0],rp[:i,1]); line2.set_data(rp[i,0],rp[i,1])
  return line1, line1b, line2, line2b

def animateFigure(Qe,Qp,tf):
  
  ani = animation.FuncAnimation(fig, animate, np.linspace(0,tf,5*tf), fargs=(Qe,Qp),
                                blit=False, interval=1,
                                repeat = False, init_func=initFigure)
  #ani.save('uniformB.mp4', fps=20)
  a = plt.show()

plt.style.use('ggplot')

fig = plt.figure(figsize=(9,8))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-5,25), ylim=(-15,15))

line2, = ax.plot([], [], 'ro', markersize=12); line2b, = ax.plot([], [], 'r--')
line1, = ax.plot([], [], 'bo'); line1b, = ax.plot([], [], 'b--')



