

from  numpy import *

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)

    for line in fr.readline():
        curLine = line.strip().split(',')
        fitName = map(float,curLine)
        dataMat.append(fitName)
    return  dataMat

