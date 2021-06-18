d = {}
for word in L:
    for i in range(len(word)):
        bucket = word[:i] + '_' + word[i+1:]
        if bucket in d:
            d[bucket].append(word)
        else:
            d[bucket] = [word]

print()