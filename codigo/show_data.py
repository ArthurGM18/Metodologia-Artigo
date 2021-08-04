import matplotlib.pyplot as plt
import numpy as np
import math

def plot_data(x, y1, y2, y3):
    
    plt.plot(x, y1, label="countSort - Aleatório")
    plt.plot(x, y2, label="countSort - Ordenado crescente")
    plt.plot(x, y3, label="countSort - Ordenado decrescente")

    x4 = []
    y4 = []

    x5 = []
    y5 = []
    for i in range(10**2, 10**6, 10**2):
        x4.append(i)
        y4.append(i / 10**6)

        x5.append(i)
        y5.append((i * math.log(i)) / 10**6)
    

    plt.plot(x4, y4, label="O(n)")
    plt.plot(x5, y5, label="O(nlog(n))")
    


    plt.xlabel('tamanho da entrada')
    plt.ylabel('tempo de execução (em segundos)')

    plt.legend()

    plt.show()



if __name__ == '__main__':
    
    f1 = open('../resultados/result_aleatorio.out', 'r')
    f2 = open('../resultados/result_ordenado.out', 'r')
    f3 = open('../resultados/result_inverso.out', 'r')
    
    y1 = []
    y2 = []
    y3 = []

    x = [ 10**2, 10**3, 10**4, 10**5, 10**6 ]
    #x = [ 10**1, 10**2, 10**3, 10**4, 10**5 ]

    n1_list = []
    n2_list = []
    n3_list = []

    for n in f1.read().split():
        n1_list.append(float(n))

    for n in f2.read().split():
        n2_list.append(float(n))

    for n in f3.read().split():
        n3_list.append(float(n))
    
    n1_list2 = np.array(n1_list)
    n2_list2 = np.array(n2_list)
    n3_list2 = np.array(n3_list)
    
    for i in range(5):
        y1.append(np.mean(n1_list2[i*25:(i+1)*25]))
        y2.append(np.mean(n2_list2[i*25:(i+1)*25]))
        y3.append(np.mean(n3_list2[i*25:(i+1)*25]))


    #for i in range(4, 5):
    #    aux = n_list2[i*25:(i+1)*25]
    #    for j in range(5):
    #        y.append(np.mean(aux[j*5:(j+1)*5]))

    plot_data(x, y1, y2, y3)

    f1.close()
    f2.close()
    f3.close()
