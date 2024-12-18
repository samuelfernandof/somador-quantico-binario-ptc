from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import plot_circuit_layout
import matplotlib.pyplot as plt

# Criando registradores para cada grupo funcional
zeros = QuantumRegister(4, 'zero')   # para os |0⟩
a = QuantumRegister(3, 'a')          # para os aᵢ
b = QuantumRegister(3, 'b')          # para os bᵢ
cr = ClassicalRegister(4, 'c')       # para as medições

# Criando o circuito
qc = QuantumCircuit(zeros, a, b, cr)

def add_C_block(qc, a, b, target):
    """Bloco C (Carry)"""
    qc.ccx(a, b, target)
    qc.cx(a, target)
    qc.cx(b, target)

def add_Cstar_block(qc, a, b, target):
    """Bloco C* (Carry inverso)"""
    qc.cx(b, target)
    qc.cx(a, target)
    qc.ccx(a, b, target)

def add_S_block(qc, a, b, target):
    """Bloco S (Soma)"""
    qc.cx(a, target)
    qc.cx(b, target)

# Primeiro nível
add_C_block(qc, a[0], b[0], zeros[0])

# Segundo nível
add_C_block(qc, a[1], b[1], zeros[1])

# Terceiro nível
add_C_block(qc, a[2], b[2], zeros[2])

# Blocos de soma
add_S_block(qc, a[0], zeros[0], b[0])
add_S_block(qc, a[1], zeros[1], b[1])
add_S_block(qc, a[2], zeros[2], b[2])

# Blocos C* inversos
add_Cstar_block(qc, a[1], b[1], zeros[1])
add_Cstar_block(qc, a[0], b[0], zeros[0])

# Barreira para separar as medições
qc.barrier()

# Medições (descomente se necessário)
# qc.measure(b[0], cr[0])
# qc.measure(b[1], cr[1])
# qc.measure(b[2], cr[2])
# qc.measure(zeros[2], cr[3])

# Para visualizar o circuito em texto
print(qc.draw(output='text', fold=100))

# Para visualizar o circuito em gráfico
circuit_mpl = qc.draw(output='mpl')
plt.show()  # Força a exibição do gráfico
