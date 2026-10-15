import time
import random
import csv
import matplotlib.pyplot as plt
from ordenacao import ordenacao_insercao, ordenacao_intercalacao

class ComparadorContador:
    total_comparacoes = 0

    def __init__(self, valor):
        self.valor = valor

    def __lt__(self, outro):
        ComparadorContador.total_comparacoes += 1
        return self.valor < outro.valor

TAMANHOS = [5, 10, 20, 30, 50, 75, 100, 200, 500, 1000]
REPETICOES = 15

def executar_medicoes():
    dados = []

    for n in TAMANHOS:
        t_ins_total = 0.0
        t_int_total = 0.0
        t_sor_total = 0.0
        c_ins_total = 0
        c_int_total = 0
        c_sor_total = 0

        for _ in range(REPETICOES):
            lista_base = [random.randint(-100000, 100000) for _ in range(n)]

            inicio = time.perf_counter()
            _, c_ins = ordenacao_insercao(lista_base)
            t_ins_total += time.perf_counter() - inicio
            c_ins_total += c_ins

            inicio = time.perf_counter()
            _, c_int = ordenacao_intercalacao(lista_base)
            t_int_total += time.perf_counter() - inicio
            c_int_total += c_int

            inicio = time.perf_counter()
            _ = sorted(lista_base)
            t_sor_total += time.perf_counter() - inicio

            lista_obj = [ComparadorContador(x) for x in lista_base]
            ComparadorContador.total_comparacoes = 0
            _ = sorted(lista_obj)
            c_sor_total += ComparadorContador.total_comparacoes

        dados.append({
            "n": n,
            "tempo_insercao": t_ins_total / REPETICOES,
            "tempo_intercalacao": t_int_total / REPETICOES,
            "tempo_sorted": t_sor_total / REPETICOES,
            "comps_insercao": c_ins_total / REPETICOES,
            "comps_intercalacao": c_int_total / REPETICOES,
            "comps_sorted": c_sor_total / REPETICOES
        })

    return dados

def salvar_csv(dados):
    with open("dados.csv", "w", newline="", encoding="utf-8") as f:
        campos = [
            "n", 
            "tempo_insercao", 
            "tempo_intercalacao", 
            "tempo_sorted", 
            "comps_insercao", 
            "comps_intercalacao", 
            "comps_sorted"
        ]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados)

def gerar_graficos(dados):
    ns = [d["n"] for d in dados]
    t_ins = [d["tempo_insercao"] for d in dados]
    t_int = [d["tempo_intercalacao"] for d in dados]
    t_sor = [d["tempo_sorted"] for d in dados]
    c_ins = [d["comps_insercao"] for d in dados]
    c_int = [d["comps_intercalacao"] for d in dados]
    c_sor = [d["comps_sorted"] for d in dados]

    plt.figure(figsize=(9, 5))
    plt.plot(ns, t_ins, marker="o", label="Inserção")
    plt.plot(ns, t_int, marker="s", label="Intercalação")
    plt.plot(ns, t_sor, marker="^", label="Python sorted()")
    plt.title("Tempo de Execução Médio vs Tamanho da Lista (n)")
    plt.xlabel("Tamanho da Lista (n)")
    plt.ylabel("Tempo (segundos)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig("grafico_tempos.png", dpi=300)
    plt.close()

    plt.figure(figsize=(9, 5))
    plt.plot(ns, c_ins, marker="o", label="Inserção")
    plt.plot(ns, c_int, marker="s", label="Intercalação")
    plt.plot(ns, c_sor, marker="^", label="Python sorted() [Extra]")
    plt.title("Número Médio de Comparações vs Tamanho da Lista (n)")
    plt.xlabel("Tamanho da Lista (n)")
    plt.ylabel("Número de Comparações")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig("grafico_comparacoes.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    resultados = executar_medicoes()
    salvar_csv(resultados)
    gerar_graficos(resultados)
