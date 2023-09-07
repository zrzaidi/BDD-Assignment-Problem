# BDD-Assignment-Problem

Here we provide code to optimally assign residents to hospitals using the Hungarian algorithm. Each hospital has a capacity for residents that cannot be exceded.

The Hungarian algorithm is a combinatorial optimization algorithm that can find assignments at the lowest cost.

We use the Hungarian algorithm implementation provided at the following link: https://python.plainenglish.io/hungarian-algorithm-introduction-python-implementation-93e7c0890e15

To allow the Hungarian algorithm to take into account the capacity of each hospital, we modify the input matrix by duplicating each hospital's ranking by its capacity, allowing for multiple residents to be assigned to a hospital.

We assume that there are more residency spots than there are residents and that every resident provides a ranking for every hospital.
