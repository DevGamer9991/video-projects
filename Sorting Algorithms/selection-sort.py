import matplotlib.pyplot as plt 
import numpy as np

A = np.random.randint(1, 100, 100)

plt.rcParams['toolbar'] = 'None'

plt.figure(figsize=(4, 8), facecolor="#171717")

for i in range(5):
    print(f"Starting in {5-i} seconds...")
    plt.pause(1)

for i in range(len(A)-1):

    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
      
    A[i], A[min_idx] = A[min_idx], A[i]
    
    print(A)
    
    plt.clf()
    
    plt.bar(range(len(A)), A)
    
    plt.bar(range(i+1), A[:i+1], color='g')

    plt.bar(range(i+1, len(A)), A[i+1:], color='r')

    plt.bar(i, A[i], color='b')
    
    plt.tick_params(labelleft=False)
    plt.tick_params(labelbottom=False)
    plt.tick_params(left=False)
    plt.tick_params(bottom=False)
    
    plt.pause(0.1)

plt.show()