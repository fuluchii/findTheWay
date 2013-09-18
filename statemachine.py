# -*- coding: utf-8 -*-
class StateMachine:
	def __init__(self):
		self.state_tree = []

	def add_state(self,state):
		self.state_tree.append(state)

	def run(self,something,*input):
		if hasattr(something, 'state'):
			next = something.state.find_way(*input)
			if next is not None:
				something.state = next
				return True
			else:
				return False
