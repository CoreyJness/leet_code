    def kidsWithCandies(self, candies, extraCandies):
        results = []
        for i in candies: 
            if i + extraCandies >= max(candies):
                results.append(True)
            if i + extraCandies < max(candies):
                results.append(False)
        return results