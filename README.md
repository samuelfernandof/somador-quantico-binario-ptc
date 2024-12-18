#### Somador quântico 

Aluno: Samuel Fernando F. Silva  

 

Aqui, temos a implementação de parte de um somador binário usando qubits e portas quânticas. Um somador quântico é usado para somar números binários, similar ao que acontece em um computador clássico, mas aproveitando as propriedades dos sistemas quânticos, como superposição e entanglement. 

 

Recursos utilizados 

Foi usado o simulador Qiskit da IBM Quantum em um ambiente Python local. Código em anexo no Github. 

10 qubits no total: 

4 qubits no registrador zero: Armazenam os carry intermediários. 

3 qubits no registrador a: Representam os bits do primeiro número de entrada. 

3 qubits no registrador b: Representam os bits do segundo número de entrada. 

Portas Lógicas Quânticas: 

Porta X (NOT): Inicializa qubits ou inverte estados. 

Porta CX (CNOT): Realiza a soma exclusiva (XOR) entre qubits. 

Porta CCX (Toffoli): Calcula o carry — a parte importante para a adição binária. 

 

Objetivo 

O objetivo do circuito é calcular: 

Os bits de carry — valores intermediários que surgem durante a soma binária. 

Os bits de soma — a soma dos dois números binários representados pelos registradores a e b. 

 

Estrutura do Circuito 

A imagem mostra claramente a organização do somador em três partes principais: 

Cálculo do Carry (Bloco C): 

A primeira parte do circuito calcula o carry dos bits a[i] e b[i] e armazena o resultado nos qubits zero. 

Portas CCX (Toffoli) são usadas aqui porque o carry depende de duas entradas (a e b). 

Cálculo da Soma (Bloco S): 

A soma dos bits é calculada usando portas CX (CNOT). 

A soma ocorre após o cálculo do carry, pois o carry afeta a soma de bits mais significativos. 

Reversão do Carry (Bloco C*): 

A etapa final reverte os cálculos intermediários do carry para "limpar" o estado dos qubits auxiliares. 

Isso é feito usando operações inversas das portas anteriores (CCX e CX). 

 

Metodologia 

Carry: 

 Quando somamos dois números binários, o resultado pode "transbordar" (carry). Por exemplo: 

1+1=10(1 eˊ a soma, 0 eˊ o carry)1 + 1 = 10 \quad \text{(1 é a soma, 0 é o carry)}  

O qubit zero armazena esse carry intermediário, que será usado para somar bits mais significativos. 

Soma: 

 A soma é realizada usando operações XOR entre os bits de entrada a e b, ajustando com o carry. 

Reversão: 

 A reversão do carry limpa o circuito, garantindo que os qubits auxiliares não contenham informações residuais — isso é essencial em computação quântica. 

 

Interpretação do output 

A imagem do circuito exibe as três etapas claramente: 

Linhas Horizontais representam os qubits: 

zero_0, zero_1, zero_2, etc., armazenam os carrys. 

a_0, a_1, a_2 e b_0, b_1, b_2 são os bits de entrada. 

Portas Lógicas: 

Quadrados grandes com X: Portas NOT aplicadas aos qubits para inicialização. 

Quadrados menores ligados por linhas verticais: CNOT e Toffoli, que realizam operações lógicas essenciais para soma e carry. 

Barreira Visual: 

O circuito é dividido em blocos (Carry, Soma, Carry Inverso) para facilitar a compreensão. 

 

Resultado  

O circuito implementa: 

Carry: Calcula os valores intermediários necessários para a soma binária. 

Soma: Obtém os bits finais da soma dos números a e b. 

No final, os qubits b contêm os resultados parciais da soma, e os qubits zero armazenam os carry bits intermediários. 

 

Resumo  

O circuito é organizado em três fases: Carry → Soma → Carry Inverso. 

Utiliza 10 qubits no total. 

A imagem mostra claramente o uso das portas lógicas CCX e CX para resolver a soma binária. 

O resultado é armazenado nos qubits b e zero, representando a soma dos bits e o carry acumulado. 

Uma observação final: isso exemplifica como operações aritméticas clássicas podem ser implementadas no paradigma quântico! 

 

Link para Github:  

Imagem da saída gerada: 
 
 
