/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let solutions = [];
    
    function dfs(left, right, s){
        if (s.length == n*2){
            solutions.push(s);
            return;
        }
        
        if (left < n) dfs(left+1, right, s + '(');
        if (right < left) dfs(left, right + 1, s + ')');
    }
    
    dfs(0, 0, "");
    return solutions;
};