# #BEST TIME TO BUY AND SELL STOCKS(brute)
# prices=[7,2,1,5,6,4,8]
# max_val=0
# n=len(prices)
# for i in range(n):
#     for j in range(i+1,n):
#         val=prices[j]-prices[i]
#         max_val=max(max_val,val)
# print(max_val)


#OPTIMAL
prices=[7,2,1,5,6,4,8]
max_prft=0
min_val=float("inf")
n=len(prices)
for i in prices:
    min_val=min(min_val,i)
    profit=i-min_val
    max_prft=max(max_prft,profit)
print(max_prft)
