def word_cruncher(words, target):
    results = []

    def dfs(path, start, used):
        if start == len(target):
            result = ' '.join(words[i] for i in path)
            if result not in results:
                results.append(result)
            return
        for i in range(len(words)):
            if i not in used and target[start:start + len(words[i])] == words[i]:
                used.add(i)
                dfs(path + [i], start + len(words[i]), used)
                used.remove(i)

    dfs([], 0, set())

    return results

words = input().split(', ')
target = input()
print('\n'.join(word_cruncher(words, target)))
