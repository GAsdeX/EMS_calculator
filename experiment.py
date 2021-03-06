import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
from numpy.linalg import det
import random

from datasets import *

class Experiment:
    def __init__(self, sets, sed_desc):
        self.sets = np.array(sets)
        self.set_desc = sed_desc
        self.a = []

    def __get__(self, obj, objtype):
        print('print')
        return self.sets 

    def __set__(self, obj, val):
        print('asd')
        self.val = val   

    def set_data(self, sets):
        self.sets = np.array(sets)

    def trim_sets(self, trimpoint):
        result = []
        for i in range(len(self.sets)):
            result.append([self.sets[i][j]  for j in range(trimpoint)])
        self.sets = np.array(result)

    def create_C(self):
        C = np.identity(len(self.sets))
        return(C)

    def create_a(self):
        step = len(self.create_C()[0,:])
        a = [(1/step) + (1/step)*i for i in range(len(self.create_C()[0,:]))]    
        return(a)

    def create_A(self):
        A = []
        for i in range(len(self.create_a())):
            a = [pow(self.create_a()[j], i+1) for j in range(len(self.create_a()))]
            A += [a]
        return(np.array(A))
    
    def create_A_T(self):
        return inv(self.create_A())

    def calc_H(self):
        H = [[] for i in range(len(self.sets))]
        C = self.create_C()

        Cr = np.array([np.dot(self.create_A_T(), C[i]) for i in range(len(H))])

        for i in range(len(self.sets[0])):
            B = self.sets[:,i]
            h = []

            for j in range(len(H)):
                h = np.dot(B, Cr[j,:])
                H[j].append(h)

        return(H)

    def calc_det_A(self):
        return det(self.create_A())
    
    def printSet(self):
        print(self.sets)   

    def up_ampl(self, height):
        result = []
        for i in self.sets:
            print(i)
            result.append([j + j * height  for j in i])  

        self.sets = np.array(result)

    def add_noize(self):
        result = []
        for i in range(len(self.sets)):
            # print(random.uniform(0, self.sets[i][0]/10))
            temp = []
        
            for j in range(len(self.sets[i])):
                temp.append((self.sets[i][j] * 0.95) + (self.sets[i][j] * 0.10 * random.random()))
            result.append(temp)  

        self.sets = np.array(result)

def interval(sets):
    return(len(sets[0]))

if __name__ == "__main__":
    #experiment1 = Experiment([dataset_1b, dataset_2b, dataset_3b], '2 набор')
    experiment1 = Experiment([dataset_1c, dataset_2c, dataset_3c], '3 набор')
    experiment3 = Experiment([dataset_1d, dataset_2d, dataset_3d], '4 набор')
    # print(experiment1.sets)
    
    experiment_with_height =  Experiment([dataset_1c, dataset_2c, dataset_3c], '3 набор')
  
    experiment1.trim_sets(15) 
    experiment_with_height.trim_sets(15) 
    
    experiment_with_height.up_ampl(0.3)  
       

    # print(experiment1.sets)
    # print(interval(experiment1.sets))

    # experiment2 = Experiment([dataset_1b, dataset_2b], '2 набор')
    # experiment3 = Experiment([dataset_2c, dataset_4c], '1 набор')
    # experiment4 = Experiment([dataset_2b, dataset_4b], '2 набор')

    # experiment = Experiment([dataset_1,dataset_2,dataset_3], 'Старый эксперимент')
    # experiment.set_data([dataset_1,dataset_2])

    # plt.plot(np.arange(0, experiment1.interval, 1), dataset_1d)
    # plt.plot(np.arange(0, experiment1.interval, 1), dataset_2d)
    # plt.plot(np.arange(0, experiment1.interval, 1), dataset_3d)
    # plt.plot(np.arange(0, experiment1.interval, 1), dataset_4d)
    # plt.plot(np.arange(0, experiment2.interval, 1), experiment2.calc_H()[1], label="H 2, " + experiment2.set_desc +" , det=" + str(experiment2.calc_det_A()))

    # plt.plot(np.arange(0, experiment3.interval, 1), experiment3.calc_H()[0], label="H 2, " + experiment3.set_desc +" , det=" + str(experiment3.calc_det_A()))
    # plt.plot(np.arange(0, experiment4.interval, 1), experiment4.calc_H()[0], label="H 2, " + experiment4.set_desc +" , det=" + str(experiment4.calc_det_A()))
    # experiment1.calc_H()

#
    #for i in range(len(experiment1.sets)):
    #        plt.plot(np.arange(0, interval(experiment1.sets), 1), experiment1.sets[i], label="H " + str(i+1))
  #
    #for i in range(len(experiment1.sets)):
    #        plt.plot(np.arange(0, interval(experiment1.sets), 1), experiment1.sets[i], label="H " + str(i+1))
  #
    #for i in range(len(experiment1.sets)):
    #    plt.plot(np.arange(0, interval(experiment_with_height.sets), 1), experiment_with_height.sets[i], '--',label="H noize " + str(i+1))
    

    #for i in range(len(experiment1.sets)):
    #        plt.plot(np.arange(0, interval(experiment1.sets), 1), experiment1.calc_H()[i], label="H " + str(i+1))

    plt.show()
   
    for i in range(len(experiment1.sets)):
            plt.plot(np.arange(0, interval(experiment1.sets), 1), experiment1.calc_H()[i], label="H " + str(i+1))
    

    for i in range(len(experiment1.sets)):
        plt.plot(np.arange(0, interval(experiment_with_height.sets), 1), experiment_with_height.calc_H()[i], '--',label="H noize " + str(i+1))
    
    plt.legend(loc='upper left')
    plt.show()
    

