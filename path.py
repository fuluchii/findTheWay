# -*- coding: utf-8 -*-
from state import State

class Path:
	def __init__(self,exp_type,expression,next_state,from_state):
		self.exp_type = exp_type
		self.expression = expression
		self.next_state = next_state
		self.from_state = from_state

	def get_next(self,*input):
		if self.exp_type is 'str':
			print input
			if input[0] == self.expression:
				return self.next_state
			else:
				return None
		if self.exp_type is 'func':
			try:
				if self.expression(*input):
					return self.next_state
				else:
					return None
			except TypeError:
				print 'TypeError'
				return None

def test_func(a,b):
	if a > b:
		return True
	else:
		return False
next = State('next')
froms = State('from')
path = Path('func', test_func, next,froms)
if path.get_next(5,4) is not None:
	print path.get_next(5 ,4).state_desc
