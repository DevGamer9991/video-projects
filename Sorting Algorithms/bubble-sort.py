import matplotlib.pyplot as plt 
import numpy as np

def bubbleSort(arr, i):
    n = len(arr)

    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
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

        plt.bar(range(len(arr)), arr)
        
        plt.bar(range(len(arr)-i-1, len(arr)), arr[len(arr)-i-1:], color='g')

        plt.bar(range(len(arr)-i-1), arr[:len(arr)-i-1], color='r')
        
        # make the next element to be sorted blue
        plt.bar(len(arr)-i-1, arr[len(arr)-i-1], color='b')
        
        plt.tick_params(labelleft=False)
        plt.tick_params(labelbottom=False)
        plt.tick_params(left=False)
        plt.tick_params(bottom=False)
        
        plt.pause(0.1)
    plt.show()
