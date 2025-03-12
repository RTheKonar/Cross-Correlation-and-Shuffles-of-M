import numpy as np

def rank_with_random_ties(data):
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

# Example usage:

    
data = [2, 3, 2, 2, 4, 4,89,89,87]
ranks = rank_with_random_ties(data)
#for i in range(1,10):
print(ranks)
