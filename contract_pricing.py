from price_model import get_price
def calculate_contract_price(injection_dates, withdrawal_dates, volumes,storage_cost_per_unit,injection_cost,withdrawal_cost,max_storage_capacity):

    if not (len(injection_dates) == len(withdrawal_dates) == len(volumes)):
        return "Input lists must have the same length"
    
    total_profit = 0

    for i in range(len(injection_dates)):

        injection_date = injection_dates[i]
        withdrawal_date = withdrawal_dates[i]
        volume = volumes[i]
        if volumes[i] > max_storage_capacity:
            return f"Volume at index {i} exceeds maximum storage capacity"

    
        buy_price = get_price(injection_date)
        sell_price = get_price(withdrawal_date)
    

        profit = (sell_price - buy_price) * volume
        final_profit = profit - (storage_cost_per_unit * volume) 
        final_profit -= (injection_cost * volume) + (withdrawal_cost * volume)
        total_profit += final_profit

    return total_profit


print(calculate_contract_price(['2024-06-20','2024-06-21'], ['2025-01-01','2025-01-02'], [1000, 1500], 0.1, 0.05, 0.05, 5000))