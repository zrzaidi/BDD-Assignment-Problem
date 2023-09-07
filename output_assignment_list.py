from hungarian import *

#take in output matrix from hungarian algorithm, the hospital names,and the number of doctors and output a list with a hospital assignment for each doctor
def assignment_list(matrix,col_names,residents):
    assignments = []
    num_doctors = len(residents)
    matrix = pd.DataFrame(matrix, columns = col_names)
    for i in range(num_doctors):
        assignments.append((matrix.iloc[i]>0)[matrix.iloc[i]>0].index[0].split('.')[0])
    for i in range(num_doctors):
        print(residents[i]+' is assigned to '+assignments[i])
