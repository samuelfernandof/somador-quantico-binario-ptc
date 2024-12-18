#### Somador quântico 

Aluno: Samuel Fernando F. Silva  

 

# **Somador Binário Quântico com Qiskit**

Implementação de um **somador binário** usando **qubits** e **portas lógicas quânticas**. O somador quântico é utilizado para somar números binários, aproveitando as propriedades dos sistemas quânticos, como **superposição** e **entanglement**.

---

## **Recursos Utilizados**

- **Tecnologia**: Qiskit (IBM Quantum)  
- **Ambiente**: Python (código disponível no repositório)  
- **Qubits**: 10 no total  
   - **4 qubits** no registrador `zero`: Armazenam os **carry** intermediários.  
   - **3 qubits** no registrador `a`: Representam os **bits do primeiro número**.  
   - **3 qubits** no registrador `b`: Representam os **bits do segundo número**.

---

## **Portas Lógicas Quânticas**

- **Porta X (NOT):** Inicializa qubits ou inverte estados.  
- **Porta CX (CNOT):** Realiza a **soma exclusiva (XOR)** entre qubits.  
- **Porta CCX (Toffoli):** Calcula o **carry** — a parte importante para a adição binária.

---

## **Objetivo**

O circuito foi projetado para calcular:

1. **Os bits de carry** — valores intermediários que surgem durante a soma binária.  
2. **Os bits de soma** — a soma dos dois números binários representados pelos registradores `a` e `b`.

---

## **Estrutura do Circuito**

A imagem mostra claramente a organização do somador em **três partes principais**:

1. **Cálculo do Carry (Bloco C):**
   - Calcula o **carry** dos bits `a[i]` e `b[i]` e armazena o resultado nos qubits `zero`.
   - Utiliza **portas CCX (Toffoli)**, pois o carry depende de duas entradas.

2. **Cálculo da Soma (Bloco S):**
   - Calcula a soma dos bits usando **portas CX (CNOT)**.  
   - A soma é realizada **após** o cálculo do carry.

3. **Reversão do Carry (Bloco C*):**
   - Reverte os cálculos intermediários do carry para **limpar os qubits auxiliares**.  
   - Isso é feito aplicando operações inversas.

---

## **Metodologia**

### **Carry:**
Quando somamos dois números binários, o resultado pode "transbordar" (carry). Por exemplo:  
\[
1 + 1 = 10 \quad (\text{1 é a soma, 0 é o carry})
\]  
O qubit `zero` armazena o carry intermediário, usado para somar bits mais significativos.

### **Soma:**
A soma é realizada usando **operações XOR** (CNOT) entre os bits de entrada `a` e `b`, ajustando com o carry.

### **Reversão:**
A reversão do carry **limpa os qubits auxiliares**, garantindo que não haja resíduos — algo essencial em computação quântica.

---

## **Interpretação do Output**

- **Linhas Horizontais** representam os qubits:  
   - `zero_0, zero_1, zero_2`: Armazenam os carrys.  
   - `a_0, a_1, a_2` e `b_0, b_1, b_2`: São os bits de entrada.

- **Portas Lógicas**:  
   - **Quadrados com X**: Portas **NOT** para inicialização.  
   - **Quadrados ligados por linhas verticais**: Portas **CNOT** e **Toffoli**, usadas para soma e carry.

- **Barreiras**:  
   - Dividem visualmente as etapas do circuito (Carry, Soma e Carry Inverso).

---

## **Resultado**

O circuito implementa:

1. **Carry**: Calcula os valores intermediários necessários para a soma binária.  
2. **Soma**: Obtém os bits finais da soma dos números `a` e `b`.

- **Qubits `b`**: Contêm os resultados parciais da soma.  
- **Qubits `zero`**: Armazenam os **carry bits intermediários**.

---

## **Resumo**

- O circuito é organizado em **três fases**: **Carry → Soma → Carry Inverso**.  
- Utiliza **10 qubits no total**.  
- Demonstra o uso das portas lógicas **CCX (Toffoli)** e **CX (CNOT)** para implementar a soma binária no paradigma quântico.  

---

## **Imagem da Saída Gerada**
*Inclua aqui a imagem do circuito gerado pelo Qiskit.*

---

## **Link para o Código no GitHub**

[Repositório do Projeto](#)  

---

**Aluno**: Samuel Fernando F. Silva  
**Disciplina**: Computação Quântica
 
 
