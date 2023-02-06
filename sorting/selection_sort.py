def selectionSort(array, size):
   
    for j in range(size):
        min_idx = j

        for i in range(j + 1, size):
         
            if array[i] < array[min_idx]:
                min_idx = i
         
        (array[j], array[min_idx]) = (array[min_idx], array[j])
