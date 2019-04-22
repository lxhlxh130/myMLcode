import numpy as np 
import matplotlib.pyplot as plt

def file2matrix(filename):
    with open(filename,'r') as f:
        data = f.readlines()
    odatingDataLabels = []
    datingData = []
    for line in data:
        item_data = []
        line = line.strip().split('\t')
        for i in line[0:3]:
            item_data.append(i)
        odatingDataLabels.append(line[3])
        datingData.append(item_data)
    datingDataMat = np.array(datingData)
    
    datingDataLabels = []
    for i in odatingDataLabels:
        # print(type(i))
        if i == 'largeDoses':
            datingDataLabels.append(3)
        if i == 'smallDoses':
            datingDataLabels.append(2)
        if i == 'didntLike':
            datingDataLabels.append(1)
    return datingDataMat,datingDataLabels

def datingDataMat(datingDataMat,datingDataLabels):
    pass


if __name__ == '__main__':
    filename = 'H:/code/myMLcode/datingTestSet.txt'
    datingDataMat,datingDataLabels = file2matrix(filename)

