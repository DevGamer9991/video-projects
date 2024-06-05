import matplotlib.pyplot as plt 
import numpy as np

A = np.random.randint(1, 100, 100)

plt.rcParams['toolbar'] = 'None'

plt.figure(figsize=(4, 8), facecolor="#171717")

for i in range(5):
    print(f"Starting in {5-i} seconds...")
    plt.pause(1)

# Traverse through all Aay elements
for i in range(len(A)-1):
    
    # Find the minimum element in remaining 
    # unsorted Aay
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
            
    # Swap the found minimum element with 
    # the first element        
    A[i], A[min_idx] = A[min_idx], A[i]
    
    print(A)
    
    plt.clf()
    
    # plot the array as a bar chart after each iteration and update the plot
    plt.bar(range(len(A)), A)
    
    # highlight the sorted part of the array in green
    plt.bar(range(i+1), A[:i+1], color='g')
    
    # highlight the unsorted part of the array in red
    plt.bar(range(i+1, len(A)), A[i+1:], color='r')
    
    # highlight the current element being compared in blue
    plt.bar(i, A[i], color='b')
    
    plt.tick_params(labelleft=False)
    plt.tick_params(labelbottom=False)
    plt.tick_params(left=False)
    plt.tick_params(bottom=False)
    
    plt.pause(0.1)

# Driver code to test above
print ("Sorted Aay")
for i in range(len(A)):
    print(A[i],end=" ") 