import numpy as np
import sys

rand_seeds = [ 10, 24, 48, 76, 104 ]

array_sizes = [ 10**2, 10**3, 10**4, 10**5, 10**6]

k_sizes = [ 10**1, 10**2, 10**3, 10**4, 10**5 ]

if __name__ == "__main__":
    
    for size in array_sizes:
        for seed in rand_seeds:
            for k in k_sizes:
                np.random.seed(seed)

                arr = np.random.randint(low=-int(k/2), high=int(k/2), size=size)

                np.savetxt( f'../dados/entrada_{size}_{k}_{seed}.dat', arr, 
                            delimiter=',', newline='\n')
           
