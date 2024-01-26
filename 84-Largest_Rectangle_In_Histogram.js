/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    let n = heights.length;
    let nextSmaller = new Array(n).fill(n);
    let prevSmaller = new Array(n).fill(-1);
    let monoStack = [];

    for (let i=0; i < n; i++){
        while (monoStack.length && heights[monoStack.at(-1)] > heights[i]){
            let next = monoStack.pop();
            nextSmaller[next] = i;
        }

        if (monoStack.length){
            prevSmaller[i] = monoStack.at(-1);
        }

        monoStack.push(i);
    };

    let maxArea = -1;
    for (let i=0; i < n; i++){
        let width = nextSmaller[i] - prevSmaller[i] - 1;
        let currentHeight = heights[i];
        maxArea = Math.max(maxArea, currentHeight * width);
    }

    return maxArea;
};
