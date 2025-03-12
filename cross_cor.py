
import numpy as np
import random

#Function to find no. of elements less than a given entry in an array
def rank(arr):
    """
    arr=arr.tolist()
    arr_new=sorted(arr)
    rank=[]
    for i in range(len(arr)):
        rank.append(arr_new.index(arr[i])+1)
    return rank
    
    """
    sorted_arr = sorted(arr)
    
    # Initialize an empty array to store the counts
    counts = np.empty_like(arr)
    
    # Iterate over each element in the sorted array
    for i, val in enumerate(arr):
        # Count the number of elements less than or equal to the current element
        counts[i] = np.sum(arr <= val)
    
    return counts    
    
    
        
    
#Function to find no. of elements greater than a given entry in an array
def l(arr):
    """
    arr=arr.tolist()
    arr_new=sorted(arr)
    l=[]
    for i in range(len(arr)):
        l.append(len(arr)-arr_new.index(arr[i]))
    return l
    """
    sorted_arr = sorted(arr)
    
    # Initialize an empty array to store the counts
    counts = np.empty_like(arr)
    
    # Iterate over each element in the sorted array
    for i, val in enumerate(arr):
        # Count the number of elements greater than or equal to the current element
        counts[i] = np.sum(arr >= val)
    
    return counts    
    

#Function to break ties uniformly at random

def break_ties_rand_unif(data):
    # Convert input data to numpy array
    data_array = np.array(data)
    
    # Get unique values and their counts
    unique_values, counts = np.unique(data_array, return_counts=True)
    
    # Determine indices of tied values
    tied_indices = np.where(counts > 1)[0]
    
    # Assign ranks
    ranks = np.zeros_like(data_array)
    
    current_rank = 1  # Initialize rank counter
    
    # Process each unique value
    for value in unique_values:
        mask = (data_array == value)  # Mask to identify positions with this value
        
        if np.sum(mask) == 1:
            # Unique value: Assign current rank
            ranks[mask] = current_rank
            current_rank += 1
        else:
            # Handle ties: Shuffle ranks for tied positions
            tied_positions = np.nonzero(mask)[0]  # Get indices of tied positions
            tied_ranks = np.random.permutation(np.arange(current_rank, current_rank + np.sum(mask)))
            ranks[tied_positions] = tied_ranks
            current_rank += np.sum(mask)
    
    return ranks








"""
def break_ties_rand_unif(arr):
    #Converting type to list
    arr=arr.tolist()
    # Identify tied elements
    tied_elements = []
    unique_elements = set(arr)
    for element in unique_elements:
        count = arr.count(element)
        if count > 1:
            tied_elements.append(element)

    # Shuffle and assign new values to tied elements
    for element in tied_elements:
        indices = [i for i, x in enumerate(arr) if x == element]
        random.shuffle(indices)
        for i, index in enumerate(indices):
            arr[index] = element + i / len(indices) 
    arr.sort()
    return arr
"""
#Chatterjee Correlation Coefficient 

def CCC(Z):  
    '''Z is a nx2 matrix, 
    where n is the number of cases, first column is SL.No., 
    second column is X and third column is Y
   '''
    
    #L=l(Z_new[:,2])
    
    
    Z_new=Z[Z[:,0].argsort()]
    #print(Z_new)
    flag=0
    for i in range(1,len(Z[:,0])):
        if Z_new[:,0][i]==Z_new[:,0][i-1]:
            flag+=1
    if flag>0:
        Z_new[:,0] = break_ties_rand_unif(Z_new[:,0])
        Z_prime = Z_new[Z_new[:,0].argsort()]
        R_1 = rank(Z_prime[:,1])
        R_2 = l(Z_prime[:,1])
        c=0
        for i in range(1,len(R_1)):  
            c+=abs(R_1[i]-R_1[i-1]) #c stores the rank
        s=0                          #s stores the denominator in case of ties
        for i in range(len(R_2)):
            s+=R_2[i]*(len(R_2)-R_2[i])
        return 1-(len(R_1)*c/(2*s))
    
    else:
        
        Z_new = Z[Z[:,0].argsort()]
        #print(Z_new)
        R = rank(Z_new[:,1])
        #print(rank(Z_new[:,1]))
        count=0                       #Count stores sum in case of no ties, also in case of ties
        for i in range(1,len(R)):
            
                 
            count+=abs(R[i]-R[i-1])
        #print(count)
        return 1-(3*count/(len(R)*len(R)-1))
            
            
        
#print(rank([1,1,2,2,3,4]))        
            
            
    
"""           
arr = [1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 7]
print("Original array:", arr)
arr = break_ties_rand_unif(arr)
print("After breaking ties:", arr)

   
arr=np.array([1,23,45,6])
Z=np.array([(1,4),(2,4),(2,-1),(4,1)])

print(rank(arr))
        
print(CCC(Z))        
    
"""
