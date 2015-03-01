""" This is test file of 'oop_text_plot.py' using unittest framework
"""
import unittest
from oop_text_plot import *

class Test(unittest.TestCase):
	def test_basic_working(self):
		size = (6,5)
		# Creating a object of canvas class
		t = canvas()
		
		# Creating a figure using its method
		new_figure = t.create_canvas(size)
		#~ print new_figure
		self.assertEqual(len(new_figure),size[0])
		#~ print 'Kanda'
		self.assertEqual(len(new_figure[0]),size[1])
		#~ print 'Mula'
	def test_writing_to_file(self):
		#~ print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
		size = (4,5)
		f1 = open('graph1.txt','w')
		x = [1,2,3,4]
		y = [1,2,3,4]
		plot(x,y,size,f1)
		f1.close()
		
		op = ['    *\n', '   * \n', ' *   \n', '*    \n']
		f2 = open('graph1.txt','r')
		#~ for mk in f2.readlines():
			#~ print mk
		#~ for lines in f2.readlines():
			#~ print lines
			#~ self.assertEqual(lines,op)
			#~ print 'Yo hunny singh'
		lines = f2.readlines()
		#~ print lines
		self.assertEqual(lines,op)
		f2.close()
		#~ print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
		
		size = (14,25)
		f1 = open('graph1.txt','w')
		x = [51,22,18,5,16,34]
		y =  [36, 18, 1, 6, 9]
		plot(x,y,size,f1)
		f1.close()
		
		op = ['                        *\n', \
		'                         \n', \
		'                         \n', \
		'                         \n', \
		'                         \n', \
		'                         \n', \
		'                         \n', \
		'                         \n', \
		'            *            \n', \
		'*                        \n', \
		'     *                   \n', \
		'                         \n', \
		'                         \n', \
		'   *                     \n']

		f2 = open('graph1.txt','r')
		#~ for mk in f2.readlines():
			#~ print mk
		#~ for lines in f2.readlines():
			#~ print lines
			#~ self.assertEqual(lines,op)
			#~ print 'Yo hunny singh'
		lines = f2.readlines()
		#~ print lines
		self.assertEqual(lines,op)
		f2.close()
		#~ print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
	
	def test_match_my_stars(self):
		size = (6,5)
		x = [1,2]
		y = [1,2]

		f1 = open('graph1.txt','w')

		plot(x,y,size,f1)
		f1.close()
		
		
		f2 = open('graph1.txt','r')
		lines = f2.readlines()
		#~ print lines
		self.assertEqual(lines[0][size[1]-1],'*')
		self.assertEqual(lines[size[0]-1][0],'*')
		
		f2.close()
		
if __name__ == 'main':
	unittest.main()
