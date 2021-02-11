from random import randrange

class Rueppel:
    def __init__(self, xorTable:list, lfsr:list, result:list):
        self.xorTable = xorTable
        self.lfsr = lfsr
        self.result = result

    def LFSRStart(self):
        index = self.xorTable.get(len(self.lfsr))
        tmp = self.lfsr[index[0]]
        for i in range(1,len(index)):
            tmp ^= self.lfsr[index[i]]
        result = self.lfsr.pop()
        self.lfsr.insert(0,tmp)
        return result
    
    def generate(self, d, k, start):
        if start == 0:
            for i in range(d):
                tmp = self.LFSRStart()
            self.result.append(tmp)
        else:
            for x in range(k):
                tmp = self.LFSRStart()
            self.result.append(tmp)
    
    def genLFSR(self):
        x = randrange(21,31)
        for i in range(x):
            self.lfsr.append(randrange(2))
        for n in range(len(self.lfsr)):
            if self.lfsr[n] == 1:
                self.lfsr[n % len(self.lfsr)] = 0
                break
          
    def runGenerator(self, amount, d, k):
        startNum = self.LFSRStart()
        self.result.append(startNum)
        for i in range(amount - 1):
            self.generate(d, k, startNum)
    
    def binToString(self):
        fileInput = ""
        for n in self.result:
            fileInput += str(n)
        return fileInput
    
    def saveLFSR(self):
        fileInput = ""
        for n in self.lfsr:
            fileInput += str(n)
        f = open("lfsr.txt","w")
        with f:
            f.write(fileInput)
        