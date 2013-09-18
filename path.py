# -*- coding: utf-8 -*-
from state import State

class Path:

	def from_(self,state):
		self.from_state = state
		self.from_state.add_path(self)
		return self

	def to_(self,state):
		self.next_state = state
		return self

	def when(self,expression):
		self.expression = expression


	def is_next(self,*input):
		if self.from_state.exp_type is 'str':
			if input[0] == self.expression:
				return True
			else:
				return False
		if self.from_state.exp_type is 'func':
			try:
				return self.expression(*input)
			except TypeError:
				print 'TypeError'
				return False

# def test_func(a,b):
# 	if a > b:
# 		return True
# 	else:
# 		return False
# next = State('next')
# froms = State('from')
# path = Path('func', test_func, next,froms)
# if path.is_next(5,4) is True:
# 	print path.is_next(5 ,4).state_desc
