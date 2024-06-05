import matplotlib.pyplot as plt 
import numpy as np

def bubbleSort(arr, i):
    n = len(arr)

    # Last i elements are already in place
    for j in range(0, n-i-1):

        # Traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]


# Driver code to test above
if __name__ == "__main__":
    # generate a random array of 50 integers from 1 to 100
    arr = np.random.randint(1, 100, 100)
    
    plt.rcParams['toolbar'] = 'None'
    
    plt.figure(figsize=(4, 8), facecolor="#171717")

    for i in range(5):
        print(f"Starting in {5-i} seconds...")
        plt.pause(1)

    for i in range(len(arr)):
        bubbleSort(arr, i)
        print(arr)
        
        plt.clf()
        # plot the array as a bar chart after each iteration and update the plot
        plt.bar(range(len(arr)), arr)
        
        # highlight the sorted part of the array in green
        plt.bar(range(len(arr)-i-1, len(arr)), arr[len(arr)-i-1:], color='g')
        
        # highlight the unsorted part of the array in red
        plt.bar(range(len(arr)-i-1), arr[:len(arr)-i-1], color='r')
        
        # highlight the current element being compared in blue
        plt.bar(len(arr)-i-1, arr[len(arr)-i-1], color='b')
        
        plt.tick_params(labelleft=False)
        plt.tick_params(labelbottom=False)
        plt.tick_params(left=False)
        plt.tick_params(bottom=False)
        
        plt.pause(0.1)
    plt.show()
