class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []

        line  = ""
        for word in words:
            if len(line) + len(word) > maxWidth:
                lines.append(line[:len(line)-1])
                line = word + " "
            else:
                line += word + " "

        if line != "":
            lines.append(line[:len(line)-1])

        original_ans = []

        for i in range(len(lines)-1):
            group_line = lines[i].split()
            left_space = maxWidth - len(lines[i])

            if len(group_line)==1:
                original_ans.append(group_line[0] + " " * left_space)
                continue

            j = 0
            while left_space > 0:
                group_line[j % (len(group_line)-1)] += " "
                j += 1
                left_space -= 1
            original_ans.append(" ".join(group_line))

        original_ans.append(lines[-1] + (" " * (maxWidth - len(lines[-1]))))

        return original_ans