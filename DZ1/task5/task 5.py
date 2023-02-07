strs = ["eat","tea","tan","ate","nat","bat"]
anagrams = [] 
  

for word in strs: 
    sortedWord = ''.join(sorted(word)) 
    if sortedWord not in anagrams: 
        anagrams.append(sortedWord)  
          

for anagram in anagrams: 
    words = [word for word in strs if ''.join(sorted(word)) == anagram] 
    if len(words) > 1: 
        print(*words)