# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 13:13:48 2021

@author: Ritwiz
"""
import random

PopSize=100
MaxIter=100

#INPUT started
line1=input() #euclidean / non euclidean
N=int(input()) #Number of cities
#Coordinates of the N cities
city_coordinates=[]
for i in range(N):
    temp = list(map(float,input().split()))
    city_coordinates.append(temp)
    
#Distances
distance=[]
for i in range(N):
    temp1 = list(map(float,input().split()))
    distance.append(temp1)    
#INPUT finished

#Using GA for TSP
#Fitness/Cost Calculation
def fitness(route):
    cost=0
    for i in range(len(route)-1):
        cost=cost+distance[route[i]][route[i+1]]
    cost+=distance[route[-1]][route[0]]
    return cost

#Order Crossover
def crossover(parent1,parent2):
    child1=[-5]*len(parent1)
    child2=[-5]*len(parent1)
    a=random.sample(range(1,len(parent1)-2),1)[0]
    b=random.sample(range(a+1,len(parent1)),1)[0]
    child1[a:b]=parent1[a:b]
    child2[a:b]=parent2[a:b]
    map1=parent1[a:b]
    map2=parent2[a:b]
    toinsert1=[] #values from parent2 to be inserted in child1
    toinsert2=[] #values from parent1 to be inserted in child2
    for i in range(len(parent1)):
        if (parent2[i] in map1)==False:
            toinsert1.append(parent2[i])
        if (parent1[i] in map2)==False:
            toinsert2.append(parent1[i])
    for i in range(len(child1)):
        if child1[i]<0:
            child1[i]=toinsert1[0]
            toinsert1=toinsert1[1:len(toinsert1)]
        if child2[i]<0:
            child2[i]=toinsert2[0]
            toinsert2=toinsert2[1:len(toinsert2)]    
    return child1,child2

#Mutation by swapping two random points
def mutate(route):
    new_route=[]
    pt1,pt2=random.sample(range(0,len(route)-1),2)
    for i in range(len(route)):
        new_route.append(route[i])
    temp=new_route[pt1]
    new_route[pt1]=new_route[pt2]
    new_route[pt2]=temp
    return new_route
    

#Initialize population of 80 candidate solutions
pop=[]
for i in range(PopSize):
    l=random.sample(range(0,N),N)
    pop.append(l)    


#Main Genetic Algorithm run for 100 iterations
for iter in range(MaxIter):
    fitval=[]
    for i in range(PopSize):
        cost=fitness(pop[i])
        fitval.append(cost)
    avgcost=sum(fitval)/len(fitval)
    new_pop=[]
    for i in range(PopSize):
        if fitval[i] <= avgcost:
            new_pop.append(pop[i])
    if(len(new_pop)<PopSize):
        while(len(new_pop)<PopSize):
            a,b=random.sample(range(0,len(new_pop)),2)
            if new_pop[a] != new_pop[b]:
                c1,c2=crossover(new_pop[a],new_pop[b])      #Crossover
                new_pop.append(c1)
                new_pop.append(c2)
                
    if(len(new_pop)>PopSize):
        new_pop=new_pop[0:PopSize]
    mut_rate=int(0.25*PopSize)               #Mutation
    mut_indices=random.sample(range(0,PopSize),mut_rate)
    for i in range(mut_rate):
        new_pop[mut_indices[i]]=mutate(new_pop[mut_indices[i]])
    pop=new_pop
    
final_fitval=[]
for i in range(PopSize):
    cost=fitness(pop[i])
    final_fitval.append(cost)

best_index=final_fitval.index(min(final_fitval))
best_route=pop[best_index]
print(*best_route)
#print(final_fitval[best_index])

    

    
    
    
    