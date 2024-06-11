function insertion_sort(arr){
    for (let i = 1; i <  arr.length; i += 1){
        let key = arr[i] 
        let j = i - 1    
        while (j >= 0 && key < arr[j]){
            arr[j + 1] = arr[j]
            j -= 1
        }
        arr[j + 1] = key
}
}
let arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
console.log("Lista ordenada:", arr)