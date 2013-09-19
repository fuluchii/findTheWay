# -*- coding: utf-8 -*-

class State:
	def __init__(self,state_desc,exp_type):
		self.exp_type = exp_type
		self.state_desc = state_desc
		self.paths = []

	def add_path(self,path):
		self.paths.append(path)

	def find_way(self,*input):
		for path in self.paths:
			if path.is_next(*input):
				return path.next_state,path.output
		return None