def quick_sort(array):
    
    def quick_sort_recursive(array, start, end):
        if start >= end:
            return
        right_start = quick_sort_part(array, start, end)
        quick_sort_recursive(array, start, right_start - 1)
        quick_sort_recursive(array, right_start, end)
        
    
    def quick_sort_part(array, left, right):
        pivot = array[(left + right) // 2]
        while(left <= right):
            while(array[left] < pivot):
                left += 1
            while(pivot < array[right]):
                right -= 1
            if left <= right:
                temp = array[left]
                array[left] = array[right]
                array[right] = temp
                left += 1
                right -= 1
        
        return left
    
    quick_sort_recursive(array, 0, len(array) - 1)
