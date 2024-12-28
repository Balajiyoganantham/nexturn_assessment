# Exercise 16: Compound Interest Calculator
# Create a user-defined function calculate_compound_interest(principal, rate, time) to calculate the compound interest using the formula: A=P×(1+r100)tA = P \times (1 + \frac{r}{100})^tA=P×(1+100r)t Where:
# • P is the principal amount
# • r is the annual interest rate
# • t is the time in years Use this function to calculate the compound interest for a given input.
# Lambda Expressions
def calculate_compound_interest(principal, rate, time):

    amount = principal * (1 + rate / 100) ** time
    compound_interest = amount - principal
    return compound_interest

# Example usage
if __name__ == "__main__":
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (in %): "))
        time = float(input("Enter the time in years: "))

        if principal < 0 or rate < 0 or time < 0:
            print("Please enter positive values for principal, rate, and time.")
        else:
            interest = calculate_compound_interest(principal, rate, time)
            print(f"Compound Interest after {time} years: {interest:.2f}")
    except ValueError:
        print("Please enter valid numeric values.")
