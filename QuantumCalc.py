import qiskit
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute
from qiskit import BasicAer as Aer
from qiskit.aqua.algorithms import Grover

class QuantumCalc:
    def print(self, string):
        print(string)

    def test(self):
        q = QuantumRegister(2)
        c = ClassicalRegister(2)
        qc = QuantumCircuit(q, c)

        qc.h(q[0])
        qc.cx(q[0], q[1])
        qc.measure(q, c)

        backend = Aer.get_backend('qasm_simulator')
        job_sim = execute(qc, backend)
        sim_result = job_sim.result()

        print(sim_result.get_counts(qc))
