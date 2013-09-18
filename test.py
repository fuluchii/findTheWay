from statemachine import StateMachine
from state import State
from path import Path

class TestObject:
	def __init__(self, state):
		self.state = state


# construct a StateMachine
statemachine = StateMachine()

state0 = State('state0','str')

state1 = State('state1','func')

state2 = State('state2','func')

state3 = State('state3','str')

def testfunc1(a):
	if int(a)>3:
		return True
	else:
		return False

def testfunc2(a):
	if int(a)<3:
		return True
	else:
		return False

_0to1 = Path()
_0to1.from_(state0).to_(state1).when('go to 1')

_0to2 = Path()
_0to2.from_(state0).to_(state2).when('go to 2')

_1to2 = Path()
_1to2.from_(state1).to_(state2).when(testfunc1)

_2to3 = Path()
_2to3.from_(state2).to_(state3).when(testfunc2)

test = TestObject(state0)


#and start loop
while(True):
	line = raw_input('input>>')
	pre_state = test.state.state_desc
	if not statemachine.run(test,line):
		print 'end.'
		break
	else:
		print 'from %s to %s.' % (pre_state,test.state.state_desc)


