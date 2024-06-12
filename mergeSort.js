function merge_sort(arr){
    if (arr.length > 1){
        let mid = Math.floor(arr.length / 2) 
        let left_half = []
        let right_half = []
        for (let i = 0; i < mid; i += 1){
            left_half.push(arr[i])
        }
        for (let i = mid; i <  arr.length; i += 1){
            right_half.push(arr[i])
        }
        for (let i = 0; i <  mid; i += 1){
            left_half[i] = arr[i]
        }
        for (let i = mid; i <  arr.length; i += 1){
            right_half[i - mid] = arr[i]
        }
        merge_sort(left_half) 
        merge_sort(right_half) 
        let i = 0
        let j = 0
        let k = 0
        while (i < left_half.length && j < right_half.length){
            if (left_half[i] < right_half[j]){
                arr[k] = left_half[i]
                i += 1
            }
            else{
                arr[k] = right_half[j]
                j += 1
            }
            k += 1
        }
        while (i < left_half.length){
            arr[k] = left_half[i]
            i += 1
            k += 1
        }
        while (j < right_half.length){
            arr[k] = right_half[j]
            j += 1
            k += 1
}
}
}
let arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
console.log("Array ordenado é:", arr)
