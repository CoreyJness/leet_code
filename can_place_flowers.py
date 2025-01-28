  def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        possibilities = 0  # Counter for the number of flowers that can be planted

        for index, value in enumerate(flowerbed):
            # Check if the current spot is empty (value == 0)
            # Also ensure left and right neighbors are empty or out of bounds
            if value == 0:
                left = flowerbed[index - 1] if index > 0 else 0
                right = flowerbed[index + 1] if index < len(flowerbed) - 1 else 0

                if left == 0 and right == 0:
                    # Plant a flower here
                    flowerbed[index] = 1
                    possibilities += 1

            # Stop early if we have already planted enough flowers
            if possibilities >= n:
                return True

        # Return whether we could plant at least `n` flowers
        return possibilities >= n