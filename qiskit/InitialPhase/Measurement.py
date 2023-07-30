from qiskit import *
from qiskit.tools.visualization import plot_histogram, array_to_latex, plot_bloch_multivector
from matplotlib import *

qr= QuantumRegister(1)
cr = ClassicalRegister(1)
circuit = QuantumCircuit(qr, cr)
circuit.h(qr)
circuit.measure(qr, cr)

simulator = Aer.get_backend('statevector_simulator')
result= execute(circuit, backend =simulator, shots=1024 ).result()
statevector = result.get_statevector()
array_to_latex(statevector)
plot_bloch_multivector(statevector)