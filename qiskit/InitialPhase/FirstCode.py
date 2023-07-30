from qiskit import *
from qiskit.tools.visualization import plot_histogram
from matplotlib import *


qr = QuantumRegister(1)
cr = ClassicalRegister(1)
circuit = QuantumCircuit(qr, cr)
circuit.h(0);
circuit.measure(qr,cr)

simulator = Aer.get_backend('qasm_simulator')
result =execute(circuit, backend =simulator, shots = 1024).result()
print(result.get_counts())
plot_histogram(result.get_counts())