from qiskit import *
from qiskit.tools.visualization import plot_histogram
from matplotlib import *

circuit = QuantumCircuit(2)

#Prepare the Bell state and distribute qubits
circuit.h(0);
circuit.cx(0,1);

circuit.barrier();

#Sender encodes message and transmits qubit to Recevier

match message := '11' :
 case '00' :
   circuit.id(0)
 case '01' :
   circuit.z(0)
 case '10' :
   circuit.x(0)
 case '11' :
  circuit.z(0)
  circuit.x(0)

circuit.barrier();

# #Receveier decodes Sender Message
circuit.cx(0,1)
circuit.h(0)

# #Receveir measures the qubit to read Senders Message
circuit.measure_all()
circuit.draw(output = 'mpl')

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend= simulator).result()
plot_histogram(result.get_counts())
