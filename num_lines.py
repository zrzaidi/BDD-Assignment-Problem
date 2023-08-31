import numpy as np

sampleM = [[0,4,1,2,2],[0,3,0,4,2],[2,0,1,0,1],[1,3,0,4,1],[2,0,1,4,0]]

def num_lines(M):
    dim = len(M)
    lines = []
    bool_M = np.zeros((dim,dim),dtype = bool)
    for i in range(dim):
        for j in range(dim):
            if M[i][j] == 0:
                bool_M[i][j] = True
    
    print(bool_M)

    while(np.any(bool_M)):
        print(max_zeros(bool_M))
        rc, index = max_zeros(bool_M)

        if rc == 0:
            lines.append("col " + str(index + 1))
            bool_M[:, index] = False
        
        if rc == 1:
            lines.append("row " + str(index + 1))
            bool_M[index] = False

    print(bool_M)
    print(lines)
    
    return lines

def max_zeros(bool_M):
    dim = len(bool_M)

    rc = 1
    index = -1
    for i in range(dim):
        count_true = np.sum(bool_M[:, i] == True)
        if count_true == 1:
            for j in range(dim):
                if bool_M[j, i] == True:
                    index = j

    if index != -1:
        return rc, index

    rc = 0
    index = -1
    for i in range(dim):
        count_true = np.sum(bool_M[i] == True)
        if count_true == 1:
            for j in range(dim):
                if bool_M[i, j] == True:
                    index = j

    if index != -1:
        return rc, index
    
    return 0
    
num_lines(sampleM)