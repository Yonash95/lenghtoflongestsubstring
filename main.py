def longestSubstring(string1):
    maxlen = 1
    if string1 == "":
        return 0
    for i in range(len(string1)):
        substring = string1[i]
        for j in range(i + 1, len(string1)):
            if string1[j] not in substring:
                substring += string1[j]
                maxlen = max(maxlen, len(substring))
            else:
                break
    return maxlen


line = input("Podaj ciąg znaków: ")
print(longestSubstring(line))
