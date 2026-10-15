# Comparação entre Ordenação por Inserção e Intercalação

Repositório para medição empírica e analítica do comportamento dos algoritmos de ordenação por Inserção (Insertion Sort), Intercalação (Merge Sort) e a função nativa `sorted()` do Python.

## Estrutura do Repositório

- `ordenacao.py`: Implementação da ordenação por inserção e por intercalação com contagem de comparações.
- `testes.py`: Testes unitários com casos especiais (lista vazia, elemento único, elementos repetidos, ordenada, invertida).
- `medir.py`: Script que executa os benchmarks, salva os dados brutos e gera os gráficos.
- `dados.csv`: Dados numéricos brutos obtidos pelas medições (médias de 15 execuções).
- `grafico_tempos.png`: Gráfico comparativo de tempo médio de execução.
- `grafico_comparacoes.png`: Gráfico comparativo de número médio de comparações.
- `RELATORIO.md`: Análise teórica e empírica dos resultados obtidos.
- `README.md`: Instruções de ambiente e execução.

## Pré-requisitos

- Python 3.8 ou superior
- Biblioteca `matplotlib`

Instalação de dependências:

```bash
pip install matplotlib

---

# Rodar os Testes Unitários
python testes.py

# Recriar CSV e Gráficos do Zero
python medir.py

# Relatório de Análise Comparativa

## 1. Tabela de Tempos e Comparações

| n | Tempo Inserção (s) | Tempo Intercalação (s) | Tempo sorted() (s) | Comparações Inserção | Comparações Intercalação | Comparações sorted() |
|---|---|---|---|---|---|---|
| 5 | 0.00000185 | 0.00000687 | 0.00000057 | 7.33 | 7.20 | 9.27 |
| 10 | 0.00000529 | 0.00001853 | 0.00000087 | 30.53 | 23.33 | 25.20 |
| 20 | 0.00001216 | 0.00002993 | 0.00000123 | 118.13 | 64.07 | 64.40 |
| 30 | 0.00002243 | 0.00004412 | 0.00000189 | 243.20 | 111.27 | 110.47 |
| 50 | 0.00006121 | 0.00007809 | 0.00000324 | 652.53 | 222.80 | 219.47 |
| 75 | 0.00014851 | 0.00012806 | 0.00000674 | 1428.07 | 376.07 | 372.67 |
| 100 | 0.00027287 | 0.00018990 | 0.00007075 | 2617.67 | 542.27 | 535.87 |
| 200 | 0.00106536 | 0.00036967 | 0.00001913 | 10054.73 | 1279.53 | 1271.87 |
| 500 | 0.00691027 | 0.00101441 | 0.00004910 | 63259.93 | 3851.93 | 3830.07 |
| 1000 | 0.03888329 | 0.00244950 | 0.00011481 | 246995.20 | 8704.47 | 8660.13 |

---

## 2. Gráficos Gerados

Os gráficos gerados pelo script `medir.py` estão salvos na raiz do projeto:
- `grafico_tempos.png`
- `grafico_comparacoes.png`

---

## 3. Ponto de Virada em Tempo

A intercalação passa a ser mais rápida que a inserção na faixa entre **$n = 50$ e $n = 75$**:
- Para $n = 50$: Inserção levou `0.000061 s` vs Intercalação `0.000078 s` (Inserção mais rápida).
- Para $n = 75$: Inserção levou `0.000149 s` vs Intercalação `0.000128 s` (Intercalação passa a ser mais rápida).

A partir de $n = 75$, a complexidade $\mathcal{O}(n^2)$ da inserção cresce exponencialmente em tempo comparada a $\mathcal{O}(n \log n)$ da intercalação (para $n = 1000$, a inserção foi $\approx 15$ vezes mais lenta).

---

## 4. Divergência entre Ponto de Virada de Tempo e de Comparações

O ponto de virada **não** ocorre no mesmo $n$:
- **Em Comparações:** O ponto de virada ocorre logo em **$n \approx 5 \text{ a } 10$** (com $n = 10$, a inserção faz $30.5$ comparações contra $23.3$ da intercalação).
- **Em Tempo:** O ponto de virada só ocorre entre **$n = 50 \text{ e } 75$**.

### Motivo:
A contagem de comparações ignora custos de infraestrutura de execução. A ordenação por inserção trabalha *in-place*, com laço iterativo simples e poucas operações de atribuição. A intercalação precisa instanciar novos arrays recursivamente (`arr[:meio]` e `arr[meio:]`) e realocar listas auxiliares na memória. Esse custo adicional de chamadas de função e cópias em memória atrasa a vantagem temporal da intercalação para entradas pequenas e médias.

---

## 5. Inadequação do `sorted()` para Decidir entre os Dois Algoritmos

A função `sorted()` do Python utiliza o Timsort, cuja rotina é compilada nativamente em **linguagem C**. Já as implementações de inserção e intercalação foram feitas em **Python interpretado**.

A máquina virtual CPython impõe uma sobrecarga de interpretação (despacho de bytecode, checagem dinâmica de tipos e controle de frame de pilha) que não existe no binário C do `sorted()`. A diferença de ordens de grandeza no tempo decorre da tecnologia de execução (C vs. Python), e não apenas da complexidade assintótica dos algoritmos.

---

## 6. Caso em que a Inserção é a Escolha Adequada

A inserção é a escolha recomendada quando a coleção de dados está **quase ordenada** (poucas inversões) ou quando os dados chegam como um fluxo contínuo (*online sorting*). 

Nesse cenário:
- A inserção opera em tempo **$\mathcal{O}(n)$** com custo de comparações mínimo por elemento.
- Não exige alocação de memória auxiliar (**$\mathcal{O}(1)$** de espaço extra contra **$\mathcal{O}(n)$** da intercalação).

---

## 7. Extra: Contagem de Comparações do `sorted()` e Limite de $n \log_2 n$

O número de comparações do `sorted()` foi medido interceptando as chamadas ao método mágico `__lt__` de objetos encapsulados.

Para $n = 1000$:
- **Comparações realizadas pelo `sorted()`:** $8.660$
- **Limite teórico inferior $n \log_2 n$:** $1000 \times \log_2(1000) \approx 1000 \times 9.9658 \approx 9.966$ comparações.

O Timsort realiza aproximadamente **$87\%$** de $n \log_2 n$ comparações em listas aleatórias, cumprindo com folga o limite de comparações de ordenação baseada em árvore de decisão e superando a intercalação pura (que fez $8.704$ comparações).