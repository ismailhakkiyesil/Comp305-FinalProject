İsmail Hakkı Yeşil and Beyza Gündoğan

# This is our Comp305-FinalProject

We are trying to find different solutions and ultimately the optimal solution for a 1-D k-center problem

Details of the problems is following:

n = number of paper factories
k = number of warehouses

Rules are:
• It is feasible to move product between any two pairs of factories.
• It is not permitted to partially move product from factories. In other words, if
  there is v tones at a factory, you only can move the whole v or nothing.
• The cost of moving v tons of paper from factory located in xi to factory located
  in xj is equal to |xi −xj|×v
---------------------------------------------------------------------------------------------------------------------
Input:
First line contains two integers n and k (1 ≤ k ≤ n ≤ 5000)
Next n lines, you are given two integers defining the location of a factory, and the output capacity of the factory.
To be more precise, the i-th line contains xi, the location of i-th factory, and vi, the capacity of i-th factory.
1≤vi,xi ≤10**6
---------------------------------------------------------------------------------------------------------------------
Output:
The total cost of consolidating the output of n factories into k warehouses.

Solution 1 - version 1
  Sort by xi values and create k clusters. If there is/are factories left outside because n (mod k) != 0, then add them to the last cluster.
  Then for the each cluster, calculate the average of the xis. Then match them to the closest xi since warehosue locations are selected from existing factories
  Finally calculate the cost of transfering products from factory located at xi to warehouse located at xj.
