class SipCalculator:

    def __init__(self,monthly_investment,annual_interest_rate,investment_period):
        self.monthly_investment = monthly_investment
        self.annual_interest_rate = annual_interest_rate
        self.investment_period = investment_period
    def calculate_final_amount(self):
        monthly_interest_rate = self.annual_interest_rate / 12 /100
        total_months = self.investment_period
        final_amount = 0

        for _ in range(total_months):
            final_amount += self.monthly_investment
            final_amount *= (1+ monthly_interest_rate)

        return final_amount
sip_calculator = SipCalculator(monthly_investment= float(input("Enter monthly investment amount: ")),annual_interest_rate= float(input("Enter annual interest rate(in percentage): ")),investment_period= int(input("Enter investment period (in years): ")))
final_amount =sip_calculator.calculate_final_amount()
print("Total amount after",sip_calculator.investment_period,"is", int(final_amount))




