 def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Step 1: Check if the strings align
        if str1 + str2 != str2 + str1:
            return ""  # No common divisor exists
        
        # Step 2: Identify the smaller string as the candidate divisor
        shorter, longer = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        
        # Step 3: Check all possible divisors of the shorter string
        for length in range(len(shorter), 0, -1):  # Start from the full length and go down
            candidate = shorter[:length]
            
            # Check if the candidate divides both strings
            if len(str1) % length == 0 and len(str2) % length == 0:
                if candidate * (len(str1) // length) == str1 and candidate * (len(str2) // length) == str2:
                    return candidate
        
        return ""  # No valid divisor found