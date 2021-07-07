#Q-1  Write a program that takes an array denoting the daily stock price, and retums the maximum profit that could be 
# made by buying and then selling one share of that stock. There is no need to buy if no profit is possible.

#Q-2 Write a program that takes an array of integers and finds the length of a longest subarray all of 
# whose entries are equal

from typing import Counter, List
from timeit import Timer, timeit
#sample list of stock prices
stock_prices = [17.3, 22.3, 23.0, 19.5, 8.2, 5.9, 22.8, 17.3, 27.6, 29.4, 12.8, 11.1, 
2.1, 15.0, 0.6, 32.2, 32.4, 9.0, 8.4, 11.4, 2.6, 25.6, 12.6, 35.8, 24.3, 18.3, 28.4, 
19.1, 9.6, 13.1, 18.3, 13.9, 24.4, 18.1, 10.1, 24.2, 15.0, 13.1, 27.5, 30.0, 36.0, 9.3, 
30.3, 30.0, 8.2, 3.4, 25.6, 29.2, 7.6, 36.2, 6.0, 2.5, 9.1, 2.5, 32.2, 26.5, 4.4, 15.4, 0.1,
6.6, 11.5, 26.4, 31.1, 27.8, 8.8, 17.1, 8.7, 7.3, 4.5, 36.3, 28.1, 10.6, 24.0, 3.5, 12.4, 3.0, 
18.8, 18.7, 14.0, 21.1, 3.9, 28.5, 11.8, 30.3, 25.6, 33.0, 34.6, 30.5, 15.1, 27.6, 9.9, 20.8, 22.5, 
14.1, 31.1, 27.4, 25.5, 24.4, 30.4, 17.4, 25.8, 27.5, 34.0, 29.1, 6.1, 8.5, 33.3, 33.7, 32.0, 34.7, 
17.8, 3.6, 3.6, 9.7, 13.0, 11.8, 21.3, 15.7, 12.2, 4.7, 35.4, 2.6, 17.7, 0.1, 26.9, 7.8, 34.5, 11.1, 
4.3, 22.1, 18.3, 16.3, 23.6, 26.7, 2.0, 6.7, 11.2, 10.8, 36.5, 21.3, 17.6, 3.6, 27.6, 5.8, 12.6, 10.0, 
18.8, 0.3, 35.2, 29.3, 17.0, 8.5, 31.2, 13.1, 36.3, 35.1, 10.3, 18.6, 11.4, 13.7, 32.3, 11.1, 15.9, 35.3, 
20.8, 26.2, 17.6, 15.9, 29.8, 1.5, 28.5, 18.3, 29.5, 32.4, 34.5, 10.9, 24.4, 21.7, 24.5, 8.4, 24.4, 10.9, 
6.3, 27.1, 8.5, 4.3, 27.4, 9.3, 8.1, 23.9, 30.8, 29.8, 12.3, 22.4, 10.8, 22.8, 1.2, 16.3, 16.3, 20.1, 13.3, 
14.1, 19.7, 35.6, 7.8, 13.1, 8.2, 3.2, 9.9, 15.1, 8.7, 29.1, 24.6, 11.9, 27.8, 9.9, 10.7, 22.8, 14.6, 20.5, 
18.4, 19.7, 34.8, 19.5, 16.4, 11.0, 7.5, 8.2, 22.6, 28.4, 13.4, 21.0, 9.0, 4.2, 26.0, 1.8, 12.2, 32.3, 34.6, 
9.5, 19.2, 36.3, 5.9, 26.9, 33.2, 19.7, 3.6, 10.5, 2.5, 3.6, 3.1, 13.4, 16.0, 14.7, 12.9, 2.9, 5.7, 29.1, 
23.9, 1.5, 12.2, 36.4, 24.3, 0.2, 27.7, 25.1, 13.4, 2.4, 13.1, 32.3, 28.1, 31.4, 21.6, 36.5, 27.3, 27.4, 18.3, 
25.2, 15.3, 13.1, 11.4, 33.4, 34.0, 18.1, 9.4, 9.4, 28.3, 13.0, 5.0, 15.0, 28.0, 27.8, 10.3, 17.9, 35.9, 4.3, 
30.0, 3.7, 33.8, 1.7, 7.2, 6.3, 22.4, 10.5, 19.0, 26.1, 16.3, 6.3, 20.5, 3.2, 11.1, 20.4, 1.8, 34.3, 18.1, 30.3, 
14.4, 26.6, 2.1, 10.5, 24.5, 3.7, 22.8, 18.5, 22.0, 22.3, 0.3, 29.4, 8.4, 4.6, 25.3, 15.9, 27.0, 5.2, 10.1, 26.7, 
15.2, 15.3, 16.8, 15.3, 32.0, 8.8, 32.6, 25.8, 30.4, 5.4, 20.9, 28.1, 31.8, 9.7, 16.3, 31.5, 33.5, 17.8, 11.8, 8.3, 14.2, 4.2, 15.9, 19.6, 34.3, 34.7, 10.9, 21.4, 31.8 ]


#The time complexity is O(n) and the space complexity is O(1), where n is the length of the array.
def Q_1_buy_and_sell_stock_once(prices: List[float]) -> float:
    min_stock_price_so_far, max_profit  = float('inf'), 0.0
    for price in prices:
        max_stock_profit_sell_today = (price - min_stock_price_so_far)
        max_profit = max(max_profit, max_stock_profit_sell_today)
        min_stock_price_so_far = min(price, min_stock_price_so_far)
    return min_stock_price_so_far,max_profit

def q_2_length_of_longest_array_for_equal_entries(listOfNumbers):
    entry_and_counter = {}
    listOfNumbers = listOfNumbers * 10
    listOfNumbers.sort()
    for number in listOfNumbers:
        i=0
        counter = 0
        while i < len(listOfNumbers):
            if number == listOfNumbers[i]:
                counter= counter + 1    
            i = i+1
        
        if entry_and_counter.get(number) is None:
            entry_and_counter[number] = counter
        
    return entry_and_counter



if __name__ == '__main__':
    #print(Q_1_buy_and_sell_stock_once(stock_prices))\
    t1_longest_time = Timer('q_2_length_of_longest_array_for_equal_entries(stock_prices)','from __main__ import q_2_length_of_longest_array_for_equal_entries,stock_prices ')
    t = t1_longest_time.timeit(number=1000)
    print(f"timing longest subarray: {t:15.2f} milliseconds")
