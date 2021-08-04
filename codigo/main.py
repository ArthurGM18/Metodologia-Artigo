from counting_sort import countSort
import sys
import datetime
import numpy as np

rand_seeds = [ 10, 24, 48, 76, 104 ]

array_sizes = [ 10**2, 10**3, 10**4, 10**5, 10**6 ]

k_sizes = [ 10**1, 10**2, 10**3, 10**4, 10**5 ]

dados = []

def main():

    for size in array_sizes[:1]:

        dados_k = []

        for k in k_sizes[:1]:

            dados_seed = []

            for seed in rand_seeds[:1]:
            
                arr = np.loadtxt( f'../dados/entrada_{size}_{k}_{seed}.dat', delimiter=',')
                arr2 = np.asarray(arr, dtype=int)
                arr2.sort()
 
                begin_time = datetime.datetime.now()
                out = countSort(arr2[::-1])
                end_time = datetime.datetime.now() - begin_time

                dados_seed.append(end_time)
            
            dados_k.append(dados_seed)

        dados.append(dados_k)
    
    
    f = open('result.out', 'w')
    for dados_k in dados:
        for dados_seed in dados_k:
            for time in dados_seed:
                f.write(str(time.total_seconds())+' ')
            f.write('\n')
        f.write('\n')

    f.close()
    

if __name__ == '__main__':
    main()
