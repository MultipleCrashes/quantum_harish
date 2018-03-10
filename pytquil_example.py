from pyquil.quil import Program 
from pyquil.gates import H, CNOT
from pyquil.api import SyncConnection 
from pyquil.api import QVMConnection
from pyquil.gates import *

p = Program()
p.inst(H(0))
p.inst(CNOT(0, 1))
qvm = SyncConnection()
result = qvm.wavefunction(p)
print('result', result)

qvm = QVMConnection()
p = Program()
p.inst(H(0),
	CNOT(0,1),
	MEASURE(0,0),
	MEASURE(1,1))
print(p)
x = qvm.run(p, [0,1], 10)
print(x)

import numpy as np 
from pyquil.quil import Program 
from pyquil.api import QVMConnection
quantum_simulator = QVMConnection()
# pyQuil is based around operations (or gates) so we will start with the most
# basic one: the identity operation, called I. I takes one argument, the index
# of the qubit that it should be applied to.
from pyquil.gates import I
p = Program(I(0))

# Quantum states are called wavefunctions for historical reasons.
# We can run this basic program on our connection to the simulator.
# This call will return the state of our qubits after we run program p.
# This api call returns a tuple, but we'll ignore the second value for now.
wavefunction = quantum_simulator.wavefunction(p)

# wavefunction is a Wavefunction object that stores a quantum state as a list of amplitudes
alpha, beta = wavefunction

print("Our qubit is in the state alpha = {} and beta = {}".format(alpha, beta))
print("The probability of measuring the qubit in outcome 0 is {}".format(abs(alpha)**2))
print("The probabbility of measuring the qubit in outcome 1 is {}".format(abs(beta)**2))


# Applying an operation to our qubit affects the probability of each outcome. 
# We can import the qubit "flip" operation, called X, and see what it does.
# We will learn more about this operation in the next section.
from pyquil.gates import X
p = Program(X(0))
wavefunc = quantum_simulator.wavefunction(p)
alpha, beta = wavefunc

print("Our qubit is in the state alpha={} and beta={}".format(alpha, beta)) 
print("The probability of measuring the qubit in outcome 0 is {}".format(abs(alpha)**2))
print("The probability of measuring the qubit in outcome 1 is {}".format(abs(beta)**2))

p = Program(I(0), I(1))
wavefunction = quantum_simulator.wavefunction(p)
print("The quantum state is of dimension", len(wavefunction.amplitudes))
p = Program(I(0), I(1), I(2), I(3))
wavefunction = quantum_simulator.wavefunction(p)
print("The quantum state is of dimenstion:", len(wavefunction.amplitudes))
p = Program()
for x in range(10):
	p.inst(I(x))
wavefunction = quantum_simulator.wavefunction(p)
print("The quantum state is of dimenstion", len(wavefunction.amplitudes))

# wavefunction(Program) returns a coefficient array that corresponds to outcomes in the following order
wavefunction = quantum_simulator.wavefunction(Program(I(0), I(1)))
print(wavefunction.get_outcome_probs())


# Gates 
from pyquil.gates import X, Y, Z
p = Program(X(0))
wavefunction = quantum_simulator.wavefunction(p)
print("X|0 =", wavefunction)
print("The outcome probabilities are ", wavefunction.get_outcome_probs())
print("This looks like a bit flip. \n")
p = Program(Y(0))
wavefunction = quantum_simulator.wavefunction(p)
print("Y|0> =", wavefunction)
print("The outcome probabilities are ", wavefunction.get_outcome_probs())
print("This also looks like a bit flip .\n")
p = Program(Z(0))
wavefunction = quantum_simulator.wavefunction(p)
print("Z|0> = ", wavefunction)
print("The outcome probabilities are ", wavefunction.get_outcome_probs())
print("This state looks unchanged.\n")
