# --- Mock Data ---

# Daily closing prices for a volatile asset over a 10-day period
prices = [105, 102, 108, 98, 92, 99, 115, 101, 120, 110]

# Trading day indices recorded in a trading log (notice some days were skipped)
logged_days = [1, 2, 3, 5, 6, 8, 9, 12]


# --- Function Signatures to Implement ---

def max_profit(prices_list: list[int]) -> int:
    """
    Phase 1: Find maximum profit from a single buy and single sell.
    Must buy before selling. If no profit possible, return 0.
    
    Expected output for 'prices': 28 (Buy at 92 on day 5, sell at 120 on day 9)
    """
    low_buy = min(prices)
    high_sell = max(prices)
    if high_sell > low_buy:
        return high_sell - low_buy
    pass


def moving_average(prices_list: list[int], k: int) -> list[float]:
    """
    Phase 2: Calculate a k-day moving average using a sliding window.
    Return a list of averages rounded to 2 decimal places.
    
    Expected output for 'prices' with k = 3:
    [105.0, 102.67, 99.67, 96.33, 102.0, 105.0, 112.0, 110.33]
    """

    averages = []
    for i in range(len(prices)-k+1):
        window = prices[i:i+k]
        window_mavg = sum(window)/len(window)
        averages.append(window_mavg) 
    rounded_averages = [round(averages,2) for averages in averages]
    print(rounded_averages)

pass


def find_missing_days(days_list: list[int]) -> list[int]:
    """
    Phase 3: Identify all missing sequential days from the minimum day 
    to the maximum day present in the array.
    
    Expected output for 'logged_days': [4, 7, 10, 11]
    """

    absent_days = []

    for values in logged_days:
        missing_day = values =+ 1
        if missing_day != values:
            absent_days.append(missing_day)
        print(absent_days)
    
            
    pass


# --- Test Runner ---
if __name__ == "__main__":
    print("--- Phase 1: Max Profit ---")
    print("Result:", max_profit(prices))

    print("\n--- Phase 2: 3-Day Moving Average ---")
    print("Result:", moving_average(prices, k=3))

    print("\n--- Phase 3: Missing Days ---")
    print("Result:", find_missing_days(logged_days))