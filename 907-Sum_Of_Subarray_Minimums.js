/**
 * @param {number[]} arr
 * @return {number}
 */
var sumSubarrayMins = function(arr) {
    let n = arr.length;
    let prevSmaller = new Array(n).fill(-1);
    let res = new Array(n).fill(0);
    let monoStack = [];
    
    for (let i=0; i < n; i++){
        while (monoStack.length && arr[monoStack.at(-1)] > arr[i]) monoStack.pop();
        
        if (monoStack.length) prevSmaller[i] = monoStack.at(-1);
        monoStack.push(i);
    }

    for (let i=0; i < n; i++) res[i] = res.at(prevSmaller[i]) + arr[i]*(i-prevSmaller[i]);
    return res.reduce((a, b) => {return a+b}, 0) % (10**9+7);
};

