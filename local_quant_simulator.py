from qiskit import QuantumProgram, QISKitError, RegisterSizeError

q_program = QuantumProgram()
backend = 'local_qasm_simulator'
try:
    # Create a Quantum Register called qr with 2 qubits.
    quantum_reg = q_program.create_quantum_register("qr", 2)
    # Create a Classical Register called "cr" with 2 bits.
    classical_reg = q_program.create_classical_register("cr", 2)
    # Create q Quantum Circuit called "qc" involving the Quantum Register "qr"
    # and Classifical Register "cr"
    quantum_circuit = q_program.create_circuit("bell", [quantum_reg], [classical_reg])
    # Add the H gate in Qubit 0, putting this qubit in superposition.
    quantum_circuit.h(quantum_reg[0])
    # Add the CX gate on control qubit 0 and target qubit 1, putting ht 
    # qubits in a Bell state.
    quantum_circuit.cx(quantum_reg[0], quantum_reg[1])
    # Add a Measure gate to see the state.
    quantum_circuit.measure(quantum_reg, classical_reg)
    result = q_program.execute(['bell'], backend=backend, shots=1024, seed=1)
    # show the results 
    print(result)
    print(result.get_data("bell"))
except QISKitError as ex:
    print('There was an error in the circuit!. Error = {}'.format(ex))
except RegisterSizeError as ex:
    print('Error in the number of register!. Error ={}',format(ex))





