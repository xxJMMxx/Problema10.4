def SumaListas(Lista1, Lista2):
    resultadoCola = []

    remanente = 0

    while len(Lista1) != 0 and len(Lista2) != 0:
        suma = (remanente + Lista1[-1] + Lista2[-1])
        resultadoCola.append(suma % 10)
        remanente = suma // 10
        Lista1.pop(-1)
        Lista2.pop(-1)

    while len(Lista1) != 0:
        suma = remanente + Lista1[-1]
        resultadoCola.append(suma % 10)
        remanente = suma // 10
        Lista1.pop(-1)
    while len(Lista2) != 0:
        suma = remanente + Lista2[-1]
        resultadoCola.append(suma % 10)
        remanente = suma // 10
        Lista2.pop(-1)

    while remanente > 0:
        resultadoCola.append(remanente)
        remanente //= 10
    resultadoCola = resultadoCola[::-1]
    return resultadoCola


pila1 = [4, 9, 5, 6, 7, 8, 9, 3, 4, 5, 5, 6, 7, 4, 3, 2, 3, 4, 5, 6, 7, 2, 4, 5, 6, 7, 1, 2, 2, 2, 2, 2, 4, 5, 7, 5, 4,
         3, 2, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 3, 2, 6, 7, 8, 9, 2, 3, 4, 5, 6, 3, 4, 5, 5, 6, 7, 4, 3, 2, 3, 4, 5, 6,
         7, 2, 4, 5, 6, 7, 1, 2, 2, 2, 2, 2, 4, 5, 7, 5, 4, 3, 2, 6, 5, 6, 7, 4, 3, 2, 3, 4, 5, 6, 7, 2, 4,5, 6, 7,
         1, 2, 2, 2, 2, 2, 4, 5, 7, 5, 4, 3, 2]

pila2 = [9, 1, 9, 5, 6, 7, 8, 9, 3, 4, 5, 5, 6, 7, 4, 3, 2, 3, 4, 5, 6, 7, 2, 4, 5, 6, 7, 1, 2, 2, 2, 2, 2, 4, 5,
         7, 5, 4, 3, 2, 6, 5, 6, 7, 8, 9, 3, 4, 5, 5, 6, 7, 4, 3, 2, 3, 4, 5, 5, 6, 7, 4, 3, 2, 3, 4, 6, 7, 4, 3,
         2, 3, 4, 5, 6, 7, 2, 4, 5, 6, 7, 1, 2, 2, 2, 2, 2, 4, 5, 7, 5, 4]

res = SumaListas(pila1, pila2)
print(res)
