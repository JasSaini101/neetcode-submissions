class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice, minPrice, maxIndex, minIndex, index, best = prices[0], prices[0], 0, 0, 0, 0
        for price in prices:
            if price < minPrice:
                if(best < prices[maxIndex] - prices[minIndex]):
                    best = prices[maxIndex] - prices[minIndex]
                minPrice = price
                minIndex = index
                maxPrice = price
                maxIndex = index
            elif price > maxPrice:
                maxPrice = price
                maxIndex = index
            index += 1
        return(max(best, prices[maxIndex] - prices[minIndex]))
        
        