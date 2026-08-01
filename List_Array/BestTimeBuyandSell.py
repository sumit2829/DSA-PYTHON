#  Brute Force:
'''
def maxprofit(prices):
    n = len(prices)
    profit = 0
    
    for i in range(n):
        for j in range(i+1,n):
            if prices[j] > prices[i]:
                profit = max(profit,prices[j]-prices[i])
    return profit
prices = [7,1,5,3,6,4]
print(maxprofit(prices))
'''
# optimal

def maxprofit(prices):
    profit = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit
prices = [7,1,5,3,6,4]
print(maxprofit(prices))
