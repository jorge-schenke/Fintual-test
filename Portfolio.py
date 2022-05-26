from dateutil.relativedelta import relativedelta

class Portfolio:
    def __init__(self):
        self.stocks = []
    
    def profit(self, start_date, end_date, profit_mode):
        if profit_mode == "profit":
            profit = 0.0
            for stock in self.stocks:
                #For the next line, I assume that the Profit class has a "quantity" attribute that is the number of shares of the stock.
                profit += (stock.price(end_date) - stock.price(start_date))*stock.quantity
            return profit
        elif profit_mode == "annualized_profit":
            year_difference = (relativedelta(end_date - start_date)).years
            profits = []
            if year_difference > 1:
                for stock in self.stocks:
                    for n in range (0, year_difference):
                        start = start_date + relativedelta(years = n)
                        end = start_date + relativedelta(years = n+1)
                        profit = (stock.price(end) - stock.price(start))/stock.price(start)
                        profits.append(profit + 1)
                    annualized = profits[0]
                    for n in range (1, len(profits)):
                        annualized *= profits[n]
                    annualized = annualized**(1/len(profits)) - 1
                    profit = annualized
            else:
                for stock in self.stocks:
                    profit += (stock.price(end_date) - stock.price(start_date))/stock.price(start_date)
        return profit
