function bubble_sort(arr){
    let n = arr.length
    for (let i = 0; i < n; i += 1){
        for (let j = 0; j <  n-i-1; j += 1){
            if (arr[j] > arr[j+1]){
                arr[j], arr[j+1] = arr[j+1], arr[j]
}
}
}
}
let arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
console.log("Sorted array is:", arr)