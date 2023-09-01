import pandas as pd
import numpy as np

def min_zero_row(zero_mat, mark_zero):
    
    '''
    The function can be splitted into two steps:
    #1 The function is used to find the row which containing the fewest 0.
    #2 Select the zero number on the row, and then marked the element corresponding row and column as False
    '''

    #Find the row
    min_row = [99999, -1]

    for row_num in range(zero_mat.shape[0]): 
        if np.sum(zero_mat[row_num] == True) > 0 and min_row[0] > np.sum(zero_mat[row_num] == True):
            min_row = [np.sum(zero_mat[row_num] == True), row_num]

    # Marked the specific row and column as False
    zero_index = np.where(zero_mat[min_row[1]] == True)[0][0]
    mark_zero.append((min_row[1], zero_index))
    zero_mat[min_row[1], :] = False
    zero_mat[:, zero_index] = False

def mark_matrix(mat):

    '''
    Finding the returning possible solutions for LAP problem.
    '''

    #Transform the matrix to boolean matrix(0 = True, others = False)
    cur_mat = mat
    zero_bool_mat = (cur_mat == 0)
    zero_bool_mat_copy = zero_bool_mat.copy()

    #Recording possible answer positions by marked_zero
    marked_zero = []
    while (True in zero_bool_mat_copy):
        min_zero_row(zero_bool_mat_copy, marked_zero)

    #Recording the row and column indexes seperately.
    marked_zero_row = []
    marked_zero_col = []
    for i in range(len(marked_zero)):
        marked_zero_row.append(marked_zero[i][0])
        marked_zero_col.append(marked_zero[i][1])
    #step 2-2-1
    non_marked_row = list(set(range(cur_mat.shape[0])) - set(marked_zero_row))
    
    marked_cols = []
    check_switch = True
    while check_switch:
        check_switch = False
        for i in range(len(non_marked_row)):
            row_array = zero_bool_mat[non_marked_row[i], :]
            for j in range(row_array.shape[0]):
                #step 2-2-2
                if row_array[j] == True and j not in marked_cols:
                    #step 2-2-3
                    marked_cols.append(j)
                    check_switch = True

        for row_num, col_num in marked_zero:
            #step 2-2-4
            if row_num not in non_marked_row and col_num in marked_cols:
                #step 2-2-5
                non_marked_row.append(row_num)
                check_switch = True
    #step 2-2-6
    marked_rows = list(set(range(mat.shape[0])) - set(non_marked_row))
    
    return(marked_zero, marked_rows, marked_cols)

def adjust_matrix(mat, cover_rows, cover_cols):
    cur_mat = mat
    non_zero_element = []

    #Step 4-1
    for row in range(len(cur_mat)):
        if row not in cover_rows:
            for i in range(len(cur_mat[row])):
                if i not in cover_cols:
                    non_zero_element.append(cur_mat[row][i])
    
    min_num = min(non_zero_element)

    #Step4-2
    for row in range(len(cur_mat)):
        if row not in cover_rows:
            for i in range(len(cur_mat[row])):
                if i not in cover_cols:
                    cur_mat[row, i] = cur_mat[row, i] - min_num

def ans_calculation(mat, pos):
    total = 0
    ans_mat = np.zeros((mat.shape[0], mat.shape[1]))
    for i in range(len(pos)):
        total += mat[pos[i][0], pos[i][1]]
        ans_mat[pos[i][0], pos[i][1]] = mat[pos[i][0], pos[i][1]]
    return total, ans_mat

def hungarian(ranks, capacities):
    for columnName,capacity in zip(ranks,capacities):
        for i in range(capacity-1):
            ranks[columnName + '.' + str(i+2)] = ranks.loc[:, columnName]
    #print(ranks)
    num_doctors = ranks.shape[0]
    num_hospitals = ranks.shape[1]
    #print([ranks.values.max()]*num_hospitals)
    for i in range(num_hospitals - num_doctors):
        ranks.loc[len(ranks)] = [ranks.values.max()]*num_hospitals
    #print(ranks.iloc[[0]])
    num_doctors = ranks.shape[0]
    num_hospitals = ranks.shape[1]
    #print(ranks)
    for row in range(num_doctors):
        ranks.iloc[[row]] = ranks.iloc[[row]] - np.min(ranks.iloc[[row]].values)
    
    for col in range(num_hospitals):
        ranks.iloc[:,col] = ranks.iloc[:,col] - np.min(ranks.iloc[:,col].values)

    print(ranks)
    ranks = ranks.to_numpy()
    #print(ranks)
    zero_count = 0
    dim = num_doctors
    while zero_count < dim:
        #Step 2 & 3
        ans_pos, marked_rows, marked_cols = mark_matrix(ranks)
        zero_count = len(marked_rows) + len(marked_cols)

        if zero_count < dim:
            cur_mat = adjust_matrix(cur_mat, marked_rows, marked_cols)
    
    return ans_pos

def ans_calculation(mat, pos, capacities):
    ranks = mat
    for columnName,capacity in zip(ranks,capacities):
        for i in range(capacity-1):
            ranks[columnName + '.' + str(i+2)] = ranks.loc[:, columnName]
    #print(ranks)
    num_doctors = ranks.shape[0]
    num_hospitals = ranks.shape[1]
    #print([ranks.values.max()]*num_hospitals)
    for i in range(num_hospitals - num_doctors):
        ranks.loc[len(ranks)] = [ranks.values.max()]*num_hospitals
    #print(ranks.iloc[[0]])
    num_doctors = ranks.shape[0]
    num_hospitals = ranks.shape[1]
    #print(ranks)
    for row in range(num_doctors):
        ranks.iloc[[row]] = ranks.iloc[[row]] - np.min(ranks.iloc[[row]].values)
    
    for col in range(num_hospitals):
        ranks.iloc[:,col] = ranks.iloc[:,col] - np.min(ranks.iloc[:,col].values)

    #print(ranks)
    mat = ranks.to_numpy()
    total = 0
    ans_mat = np.zeros((mat.shape[0], mat.shape[1]))
    for i in range(len(pos)):
        total += mat[pos[i][0], pos[i][1]]
        ans_mat[pos[i][0], pos[i][1]] = mat[pos[i][0], pos[i][1]]
    return total, ans_mat


#df = pd.DataFrame(np.random.randint(1,3,size=(5, 3)), columns=list('ABC'))
ranks = np.array([[1, 2, 3],
				[3, 2, 1],
				[3, 1, 2],
				[1, 3, 2],
				[3, 2, 1]])
df = pd.DataFrame(ranks, columns=['A','B','C'])
cap = [2,3,2]
ans_pos = hungarian(df.copy(),cap)#Get the element position.
ans, ans_mat = ans_calculation(df, ans_pos,cap)#Get the minimum or maximum value and corresponding matrix.
print(ans_mat)

