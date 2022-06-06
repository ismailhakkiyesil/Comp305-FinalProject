# n = number of paper factories
# k = number of warehouses
# Rules are:
# • It is feasible to move product between any two pairs of factories.
# • It is not permitted to partially move product from factories. In other words, if
#   there is v tones at a factory, you only can move the whole v or nothing.
# • The cost of moving v tons of paper from factory located in xi to factory located
#   in xj is equal to |xi −xj|×v
# ---------------------------------------------------------------------------------------------------------------------
# Input:
# First line contains two integers n and k (1 ≤ k ≤ n ≤ 5000)
# Next n lines, you are given two integers defining the location of a factory, and the output capacity of the factory.
# To be more precise, the i-th line contains xi, the location of i-th factory, and vi, the capacity of i-th factory.
# 1≤vi,xi ≤10**6
# ---------------------------------------------------------------------------------------------------------------------
# Output:
# The total cost of consolidating the output of n factories into k warehouses.

import numpy as np

# Taking number of factories and warehouses
user_input = input("Please type number of factories and warehouses (fact wh): ")
user_input = user_input.split()
no_of_facts, no_of_whs = int(user_input[0]), int(user_input[1])

while no_of_facts < no_of_whs:
    print('Number of factories cannot be lower than number of warehouses!')
    user_input = input("Please type number of factories and warehouses (fact wh): ")
    user_input = user_input.split()
    no_of_facts, no_of_whs = int(user_input[0]), int(user_input[1])

print('Planned to place {fact} factorise to {wh} warehouses optimally\n'.format(fact=no_of_facts, wh=no_of_whs))

# Taking the location of i-th factory and the capacity of i-th factory
facts = []
for i in range(no_of_facts):
    fact_input = input("Please type x{i} and v{i}: ".format(i=i + 1))
    fact_input = fact_input.split()
    facts.append([int(fact_input[0]), int(fact_input[1])])


# Calculate the cost of transferring products from factory to warehouse
def cost_func(factory, warehouse):
    cost = abs(factory[0] - warehouse) * factory[1]
    return cost


# Solution 1:
# Use the means of the xis as warehouse places
# k-Cluster values with respect to their distances between them
def solution1():
    print('\nNow running the algorithm that uses means of the clusters for warehouse locations')
    print('Clusters are formed with respect to their distances between them\n')
    ordered_facts = sorted(facts)
    wh_places = []
    sum_of_locs = 0

    # Dividing n factories to k warehouses
    # and matching them to clusters on xi=mean
    ordered_facts = list(np.array_split(np.array(ordered_facts), no_of_whs))
    for clusters in ordered_facts:
        for fact in clusters:
            sum_of_locs += fact[0]
        wh_places.append(sum_of_locs / no_of_whs)
    print('Warehouses are planned to placed on', wh_places)

    # Making sure of matching found places to match existing places
    # if mean is not matched with a location, go to the closest location

    updated_wh_places = []
    wh_no = 0
    copy_ordered_facts = ordered_facts
    for clusters in copy_ordered_facts:
        clusters = np.asarray(clusters)
        updated_wh_places.append(clusters[np.linalg.norm(clusters - wh_places[wh_no], axis=1).argmin()][0])
        wh_no += 1
    print('Updated warehouse places are', updated_wh_places)

    print('\nFactory clusters are =>', ordered_facts)
    print('Warehouse places are =>', updated_wh_places)
    print()

    total_cost = 0
    for clusters, whs in zip(ordered_facts, updated_wh_places):
        for fact in clusters:
            print('Cost to move {product} product from fact located at {fact_location} to warehouse located at '
                  '{whs} = {cost}'.format(product=fact[1], fact_location=fact[0], whs=whs,
                                          cost=cost_func(fact, whs)))
            total_cost += cost_func(fact, whs)

    print(
        '\nTotal cost to move products from {fact} factories to {wh} warehouse/s is {cost}'.format(fact=no_of_facts,
                                                                                                   wh=no_of_whs,
                                                                                                   cost=total_cost))


# Solution 2:
# Use the means of the xis as warehouse places
# k-Cluster values with respect to their weighted distances between them

def solution2():
    print('\nClusters are formed with respect to their weighted (product size) distances between them\n')

    ordered_facts = sorted(facts)
    wh_places = []
    sum_of_weights = 0
    weighted_distances = 0

    # Dividing n factories to k warehouses
    # and matching them to clusters on xi=mean
    ordered_facts = np.array_split(np.array(ordered_facts), no_of_whs)
    for clusters in ordered_facts:
        for fact in clusters:
            sum_of_weights += fact[1]
            weighted_distances += fact[0] * fact[1]
        wh_places.append(weighted_distances / sum_of_weights)
    print('Warehouses are planned to placed on', wh_places)

    # Making sure of matching found places to match existing places
    # if mean is not matched with a location, go to the closest location
    updated_wh_places = []
    wh_no = 0
    copy_ordered_facts = ordered_facts
    for clusters in copy_ordered_facts:
        clusters = np.asarray(clusters)
        updated_wh_places.append(clusters[np.linalg.norm(clusters - wh_places[wh_no], axis=1).argmin()][0])
        wh_no += 1
    print('Updated warehouse places are', updated_wh_places)

    print('\nFactory clusters are =>', ordered_facts)
    print('Warehouse places are =>', updated_wh_places)
    print()

    total_cost = 0
    for clusters, whs in zip(ordered_facts, updated_wh_places):
        for fact in clusters:
            print('Cost to move {product} product from fact located at {fact_location} to warehouse located at '
                  '{whs} = {cost}'.format(product=fact[1], fact_location=fact[0], whs=whs,
                                          cost=cost_func(fact, whs)))
            total_cost += cost_func(fact, whs)

    print(
        '\nTotal cost to move products from {fact} factories to {wh} warehouse/s is {cost}'.format(fact=no_of_facts,
                                                                                                   wh=no_of_whs,
                                                                                                   cost=total_cost))


# Solution 3:
# k-means clustering in 1-D
# Distances are calculated as transfer cost between 2 points

# Solution 4:
# Jenks natural break algorithm


solution1()
solution2()
