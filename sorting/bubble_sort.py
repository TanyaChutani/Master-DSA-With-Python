def bubblesort(array, size):
    for i in range(size):
        for j in range(size-i-1):
         
            if array[j] > array[j+1]:         
               (array[j], array[j+1]) = (array[j+1], array[j])
      
    return array
