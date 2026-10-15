# Comparação entre Ordenação por Inserção e Intercalação

Repositório para medição empírica e analítica do comportamento dos algoritmos de ordenação por Inserção (*Insertion Sort*), Intercalação (*Merge Sort*) e a função nativa `sorted()` do Python.

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

Instalação das dependências:
```bash
pip install matplotlib

Como Rodar
Executar os testes unitários:

Bash
python testes.py
(Todos os testes devem retornar OK).

Gerar medições, CSV e gráficos do zero:

Bash
python medir.py
(O script regera automaticamente os arquivos dados.csv, grafico_tempos.png e grafico_comparacoes.png).
