# -*- coding: utf-8 -*-
class StateMachine:
	def __init__(self):
		self.state_tree = []

	def add_state(self,state):
		self.state_tree.append(state)

	def run(self,something,*input):
		if hasattr(something, 'state'):
			next = something.state.find_way(*input)
			if next is None:
				return False
			else:
				something.state = next[0]
				return next[1]
