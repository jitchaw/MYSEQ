def countBase(seq, base):
    count = seq.count(base)
    return(count)
     
def gcContent(seq):
    sumGC = countBase(seq, 'G') + countBase(seq, 'C')
    #print(sumGC)
    totalBase = countBase(seq, 'A') + countBase(seq, 'T') + countBase(seq, 'G') + countBase(seq, 'C')
    #print(totalBase)
    return(sumGC/totalBase)

def atContent(seq):
    sumAT = countBase(seq, 'A') + countBase(seq, 'T')
    #print(sumAT)
    totalBase = countBase(seq, 'A') + countBase(seq, 'T') + countBase(seq, 'G') + countBase(seq, 'C') 
    #print(totalBase)
    return(sumAT/totalBase) 

def countBasesDict(seq):
    basesM = {}
    for base in seq:
        basesM[base] = basesM.setdefault(base, 0) + 1
    return basesM