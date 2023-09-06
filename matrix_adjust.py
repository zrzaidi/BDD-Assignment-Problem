import pandas as pd
import numpy as np

#Take in dataframe of each doctor's ranking of hospitals and a list of capacities of the hospitals and output an adjusted square ranks numpy matrix
#and hospital names
def matrix_with_capacities(ranks,capacities):
  #duplicate columns by the hospital's capacity
	for columnName,capacity in zip(ranks,capacities):
		for i in range(capacity-1):
			ranks[columnName + '.' + str(i+2)] = ranks.loc[:, columnName]
	ranks = ranks.reindex(sorted(ranks.columns), axis=1) #sort columns by hospital name
	col_names = ranks.columns
	num_doctors = ranks.shape[0]
	num_hospitals = ranks.shape[1]
  #add dummy rows to make matrix square
	for i in range(num_hospitals - num_doctors):
		ranks.loc[len(ranks)] = [ranks.values.max()+1]*num_hospitals
	num_doctors = ranks.shape[0]
	num_hospitals = ranks.shape[1]
	cost_matrix = ranks.to_numpy()
	return cost_matrix, col_names
