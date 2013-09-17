# -*- coding: utf-8 -*-
class StateMachine:
	def __init__(self):
		self.state_tree = []

	def add_state(self,state):
		self.state_tree.append(state)

	def get_start(self):
		return self.start