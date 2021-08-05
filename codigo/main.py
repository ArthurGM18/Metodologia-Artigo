from counting_sort import countSort
import sys
import datetime
import numpy as np

is_aleatorio = False
is_ordenado = False
is_inverso = False

rand_seeds = [ 10, 24, 48, 76, 104 ]

array_sizes = [ 10**2, 10**3, 10**4, 10**5, 10**6 ]

k_sizes = [ 10**1, 10**2, 10**3, 10**4, 10**5 ]

dados = []

def main(tipo):

    for size in array_sizes:

        dados_k = []

        for k in k_sizes:

            dados_seed = []

            for seed in rand_seeds:
            
                arr = np.loadtxt( f'../dados/entrada_{size}_{k}_{seed}.dat', delimiter=',')
                arr2 = np.asarray(arr, dtype=int)
                
                if tipo == 'ordenado':
                    arr2.sort()
                elif tipo == 'inverso':
                    arr2.sort()
                    aux = arr2[::-1]
                    arr2 = aux
 
                begin_time = datetime.datetime.now()
                out = countSort(arr2)
                end_time = datetime.datetime.now() - begin_time

                dados_seed.append(end_time)
            
            dados_k.append(dados_seed)

        dados.append(dados_k)
    

    f = open(f'../resultados/result_{tipo}.out', 'w')
    for dados_k in dados:
        for dados_seed in dados_k:
            for time in dados_seed:
                f.write(str(time.total_seconds())+' ')
            f.write('\n')
        f.write('\n')

    f.close()
    

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print("Argumento do tipo de ordenação não passado!")
        print("Adicione um dos argumentos: aleatorio | ordenado | inverso")
    else:
        main(sys.argv[1])
