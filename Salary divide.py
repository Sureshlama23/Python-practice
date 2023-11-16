class SalaryBudget:
    def __init__(self):
        self.salary = 0
        self.investment = 0
        self.emergency = 0
        self.insurance = 0
        self.expenses = 0
    def get_user_input(self):
        self.salary = float(input("Enter here your monthly salary:- "))
        if self.salary <= 0:
            print("Invalid salary input")
        else:
            self.investment = float(input("Enter the percentage of salary you want to allocate for investment (0-100%):- "))
            self.emergency = float(input("Enter the percentage of salary you want to allocate for emergency (0-100%):"))
            self.insurance = float(input("Enter the percentage of salary you want to allocate for insurance (0-100%):"))
            self.expenses = float(input("Enter the percentage of salary you want to allocate for expenses (0-100%):"))
            total_percentage = self.investment+ self.emergency + self.insurance + self.expenses
            if total_percentage != 100:
                            print("Error: Total percentage should be 100%. Please re-allocate.")
    def budget_calculate(self):
        self.investment = self.salary*(self.investment/100)
        self.emergency = self.salary*(self.emergency/100)
        self.insurance = self.salary*(self.insurance/100)
        self.expenses = self.salary*(self.expenses/100)

        return {
            "Investment": self.investment,
            "emergency": self.emergency,
            "insurance": self.insurance,
            "expenses": self.expenses
            }
    def displaybudget(self,budget):
            print("\nBudget Summary:")
            for category,amount in budget.items():
                print(f"{category}:{amount:.2f}")

budget_planner = SalaryBudget()
budget_planner.get_user_input()
budget = budget_planner.budget_calculate()
budget_planner.displaybudget(budget)