# Sentence Reverse
# You are given an array of characters arr that consists of sequences of characters separated by space characters.
# Each space-delimited sequence of characters defines a word.

# Implement a function reverseWords that reverses the order of the words in the array in the most efficient manner.

# Explain your solution and analyze its time and space complexities.

# Time
# O(n)
# n = len(arr)

# Space
# O(1)


def reverse_words(arr):
    arr.reverse()
    i = 0
    while i < len(arr):
        wordStart = findNextWordStart(arr, i)
        if wordStart == len(arr):
            return arr
        wordEnd = findWordEnd(arr, wordStart)
        reverseWord(arr, wordStart, wordEnd)
        i = wordEnd + 1
    return arr


def findNextWordStart(arr, i):
    while i < len(arr) and arr[i] == " ":
        i += 1
    return i


def findWordEnd(arr, wordStart):
    wordEnd = wordStart
    while wordEnd + 1 < len(arr) and arr[wordEnd + 1] != " ":
        wordEnd += 1
    return wordEnd


def reverseWord(arr, wordStart, wordEnd):
    for i in range((wordEnd - wordStart + 1) // 2):
        arr[wordStart + i], arr[wordEnd - i] = arr[wordEnd - i], arr[wordStart + i]