#Trying to build a simple perceptron described in https://www.youtube.com/watch?v=ntKn5TPHHAk in python3

import random

def sign(n):   #Acts an activation function
	if(n >= 0):
		return 1
	else:
		return -1

class Perceptron:
	  def __init__(self, weights,inputs):
	  	self.weights = weights
	  	self.inputs = inputs
	  	for i in range( 3 ):
	  		weights.append( random.uniform(-1,1) )
	  	#print(weights)
	  def think(self):
	  	total = 0
	  	for i in range( 3 ):
	  		#print(weights,inputs)
	  		total += self.inputs[i] + self.weights[i]
	  	#print(total)
	  	return( sign(total) )

if __name__ == '__main__':
	inp = [ -8, 3, 5]
	p = Perceptron([],inp)
	print( p.think() )