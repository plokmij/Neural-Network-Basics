#A simple perceptron
import random

def sign(n):
	if(n >= 0):
		return 1
	else:
		return 0

class Perceptron:
	  weights = []
	  hell = 5
	  def __init__(self):
	  	for i in range( 3 ):
	  		weights[i] = random.uniform(-1,1)
	  

	  def think(inputs):
	  	total = 0
	  	for i in range( 3 ):
	  		total += inputs[i] + hell
	  	return sign(total)


p = Perceptron
inp = [ 2, 3, 5]
p.think(inp)