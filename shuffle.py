import lib
import timeit

n=10
deck = [i for i in range(1, n+1)]
print(deck)
print(lib.sqi(deck))

deck2 = lib.fisher_yates(deck)
print(deck2)
print(lib.sqi(deck2))

temps = timeit.timeit("lib.fisher_yates(deck)", setup="from __main__ import ma_fonction", number=1000)
print(f"Temps d'exécution : {temps} secondes")
