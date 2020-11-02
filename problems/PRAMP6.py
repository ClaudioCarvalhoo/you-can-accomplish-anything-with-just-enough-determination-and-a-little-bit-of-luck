# Word Count Engine
# Implement a document scanning function wordCountEngine, which receives 
# a string document and returns a list of all unique words in it and their 
# number of occurrences, sorted by the number of occurrences in a descending order. 
# If two or more words have the same count, they should be 
# sorted according to their order in the original sentence. 
# Assume that all letters are in english alphabet. 
# You function should be case-insensitive, so for instance, 
# the words “Perfect” and “perfect” should be considered the same word.

# The engine should strip out punctuation (even in the middle of a word) 
# and use whitespaces to separate words.

# Analyze the time and space complexities of your solution. 
# Try to optimize for time while keeping a polynomial space complexity.

# Examples:
# input:  document = "Practice makes perfect. you'll only
#                     get Perfect by practice. just practice!"

# output: [ ["practice", "3"], ["perfect", "2"],
#           ["makes", "1"], ["youll", "1"], ["only", "1"], 
#           ["get", "1"], ["by", "1"], ["just", "1"] ]

# Important: please convert the occurrence integers in the output list 
# to strings (e.g. "3" instead of 3). 
# We ask this because in compiled languages such as C#, Java, C++, C etc., 
# it’s not straightforward to create mixed-type arrays 
# (as it is, for instance, in scripted languages like JavaScript, Python, Ruby etc.). 
# The expected output will simply be an array of string arrays.

# Time:
# O(n)
# n = len(document)

# Space:
# O(n)
# n = len(document)

def word_count_engine(document):
  document = document.lower()
  newDoc = ""
  for character in document:
    if character.isalpha() or character == " ":
      newDoc += character
      
  words = newDoc.split(" ")
  temp = []
  for word in words:
    if len(word) > 0:
      temp.append(word)
  words = temp
  
  counter = {}
  for word in words:
    if word in counter:
      counter[word] += 1
    else:
      counter[word] = 1
  
  buckets = [[] for _ in range(len(words))]
  
  used = {}
  for word in words:
    if not word in used:
      buckets[counter[word]].append(word)
      used[word] = True
    
  output = []
  for j in range(len(buckets)-1, -1, -1):
    for i in range(len(buckets[j])):
      output.append([buckets[j][i], str(j)])
      
  return output