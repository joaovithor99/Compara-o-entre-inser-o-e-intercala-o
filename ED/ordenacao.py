def ordenacao_insercao(lista):
    A = list(lista)
    n = len(A)
    comparacoes = 0
    for i in range(1, n):
        chave = A[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if A[j] > chave:
                A[j + 1] = A[j]
                j -= 1
            else:
                break
        A[j + 1] = chave
    return A, comparacoes

def ordenacao_intercalacao(lista):
    A = list(lista)
    
    def _intercalar(esq, dir):
        i = 0
        j = 0
        resultado = []
        comps = 0
        len_esq = len(esq)
        len_dir = len(dir)
        
        while i < len_esq and j < len_dir:
            comps += 1
            if esq[i] <= dir[j]:
                resultado.append(esq[i])
                i += 1
            else:
                resultado.append(dir[j])
                j += 1
        
        resultado.extend(esq[i:])
        resultado.extend(dir[j:])
        return resultado, comps

    def _mergesort(arr):
        if len(arr) <= 1:
            return arr, 0
        meio = len(arr) // 2
        esq, comps_e = _mergesort(arr[:meio])
        dir, comps_d = _mergesort(arr[meio:])
        mesclado, comps_m = _intercalar(esq, dir)
        return mesclado, comps_e + comps_d + comps_m

    return _mergesort(A)
