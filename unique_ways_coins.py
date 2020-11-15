import timeit
def bottomUp(amount, coins):
    dp = [0]*(amount+1)
    dp[0] = 1
    for c in coins:
        for i in range(1, amount +1):
            if c <= i:
                dp[i] += dp[i-c]
    return dp[amount]

def topDown(amount, coins, index, dp):
    if amount == 0:
        return 1
    if index >= len(coins):
        return 0
    
    key = (amount, index)
    if not key in dp:
        ways = 0
        for i in range(index, len(coins)):
            if coins[i] <= amount:
                ways += topDown(amount-coins[i], coins, i, dp)

        dp[key] = ways
    return dp[key]
def TopDown(amount, coins):
    dp = {}
    index = 0
    return topDown(amount, coins, index, dp)
if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]
    unique_ways = bottomUp(amount, coins)
    print('There are {} unique ways to form {} with {}'.format(unique_ways, amount, coins))

    time_bottom = timeit.timeit(lambda: bottomUp(amount, coins), number=10)/10
    print('time of Bottom up approach is {:.10} s'.format(time_bottom))
    
    time_topDown = timeit.timeit(lambda: TopDown(amount, coins), number=10)/10
    print('time of Top Down approach is {:.10} s'.format(time_topDown))