function solution(arr, queries) {
    for(let [i, j] of queries) {
        let temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    return arr;
}

