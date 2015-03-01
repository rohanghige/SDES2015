import sys
import itertools
import numpy as np
from math import *

class canvas:
	def __init__(self,size = (30,80)):
		self.size = size;
		pass
	def create_canvas(self, size):
		# NOTE: not passing the size, accesing from self
		rows, cols = size
		new_canvas = []
		# Creating a blank canvas here :D
		for ind in xrange(rows):
			new_canvas.append(list(' '*cols))
		
		return new_canvas
	
	def plot_canvas(self, canvas, destination = sys.stdout):
		for line in canvas:
			destination.write(''.join(line))
			destination.write('\n')
class plot(canvas):
	def __init__(self,x,y,size = (30,80),destination = sys.stdout):
		
		self.size = size
		self.x = x
		self.y = y
		# Creating a figure using its father class :D
		my_figure = canvas.create_canvas(self, size)
		
		# what is xmin, and all other stuff
		xmin, xmax = min(x), max(x)
		ymin, ymax = min(y), max(y)
		
		x_range = float(xmax - xmin)
		y_range = float(ymax - ymin)
		
		for x_a, y_a in self.mapping(size, x, y, xmin, ymin, x_range, y_range):
			# assigning a '*' for that pixel :D
			my_figure[self.size[0] - x_a - 1][y_a] = '*'
		
		plot.plot_canvas(self,my_figure,destination)
		
	def mapping(self,dim,x,y, xmin,ymin,x_range, y_range):
		for x_i, y_i in itertools.izip(x,y):
			x_a = int(round((x_i-xmin)/x_range*(dim[0]-1)))
			y_a = int(round((y_i-ymin)/y_range*(dim[1]-1)))
			#~ if x_range < dim[0]:
				#~ x_a = int(x_i)
			#~ else:
				#~ x_a = int(round((x_a-x_min)/x_range*(dim[0]-1)))
			#~ if y_range < dim[1]:
				#~ y_a = int(y_i)
			#~ else:
				#~ y_a = int(round((y_a-y_min)/y_range*(dim[1]-1)))
			
			yield x_a, y_a
def main():
	#~ # Creating a object of canvas class
	#~ t = canvas()
	#~ 
	#~ # Creating a figure using its method
	#~ new_figure = t.create_canvas()
	#~ 
	#~ # Plotting the new_figure on terminal output window :D
	#~ t.plot_canvas(new_figure,sys.stdout)
	
	x = []
	y = np.linspace(-2*pi,2*pi,100)
	for k in y:
		x.append(sin(k))
	plot(x,y)
	
if __name__=='__main__':
		main()
		
		

