    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        j=0
        finalWord = []
        while i < len(word1) and j < len(word2):
            finalWord.append(word1[i])
            finalWord.append(word2[j])
            i+=1
            j+=1
        finalWord.extend(word1[i:])
        finalWord.extend(word2[j:])
        
        return ''.join(finalWord)