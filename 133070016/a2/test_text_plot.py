from text_plot import plot
def test_text_plot():
	x = [1,2,3,6]
	y = [1,2,3,6]
	plot(x,y)
	
	plot(x,y,6,6)
	try:
		plot(x,y,5,5)
	except IndexError:
		pass
	plot(x,y,10,10)
	
	x = [1,3,5,10]
	y = [10,11,12,13]
	plot(x,y)
	
	try:
		plot(x,y,5,10)
	except IndexError:
		pass
	
	
test_text_plot()
