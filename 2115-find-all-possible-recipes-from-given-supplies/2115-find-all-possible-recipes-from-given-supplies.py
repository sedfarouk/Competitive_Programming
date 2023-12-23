class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degrees = defaultdict(int)

        for i in range(len(recipes)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
            in_degrees[recipes[i]] = len(ingredients[i])

        ans = []
        queue = deque([i for i in supplies])
        recipes = set(recipes)

        while queue:
            q = queue.popleft()

            for nei in graph[q]:
                in_degrees[nei] -= 1

                if in_degrees[nei]==0:
                    queue.append(nei)

                    if nei in recipes:
                        ans.append(nei)

        return ans

