from plistlib import PlistFormat
from tokenize import String


class Proceso:
    def __init__(self,pid,tam,posI, posF):
        self.tam = tam
        self.pid = pid
        self.posI = posI
        self.posF = posF
        pass
    def __str__(self):
        return "PID: "+str(self.pid) +" Tam: "+str(self.tam) +" PosI: "+str(self.posI) +" PosI: "+str(self.posF)
        pass
    def __repr__(self):
        return "\nPID: "+str(self.pid) +" Tam: "+str(self.tam) +" PosI: "+str(self.posI) +" PosI: "+str(self.posF)
        pass
pList = []
pids = 0
posI = 0
tam = 3
tRam = 20
ram=[None] *tRam
mBits=[None]*8
if (tRam % 8) == 0:
    numF = tRam / 8
else:
    numF = (tRam // 8) + 1 
for i in range(numF):
    mBits[i] = [None]*8

for i in range (1,7):
    posF = posI + tam
    aux = Proceso(pids, tam ,posI, posF)
    pids +=1
    pList.append(aux)
    for j in range (posI,posF):
        ram[j] = aux.pid
    posI = posF
for proc in pList:
    print(proc)
print(ram)
print(pList)
for i in range(numF):
    print(mBits[i]," ")
