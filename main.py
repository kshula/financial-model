from financial_valuation import calculate_npv, calculate_irr, calculate_payback_period
from risk_management import calculate_value_at_risk
from portfolio_optimization import calculate_optimal_weights, calculate_portfolio_sharpe_ratio
from financial_analysis import calculate_profitability_ratio, calculate_return_on_investment, calculate_debt_to_equity_ratio

class FinancialModeling:
    def __init__(self, initial_investment, cash_flows):
        self.initial_investment = initial_investment
        self.cash_flows = cash_flows
    
    def calculate_npv(self, discount_rate):
        """
        Calculate Net Present Value (NPV).
        """
        npv = calculate_npv(self.initial_investment, self.cash_flows, discount_rate)
        return npv
    
    def calculate_irr(self):
        """
        Calculate Internal Rate of Return (IRR).
        """
        irr = calculate_irr(self.initial_investment, self.cash_flows)
        return irr
    
    def calculate_payback_period(self):
        """
        Calculate Payback Period.
        """
        payback_period = calculate_payback_period(self.initial_investment, self.cash_flows)
        return payback_period
    
    def calculate_value_at_risk(self, returns, confidence_level=0.95):
        """
        Calculate Value at Risk (VaR).
        """
        var = calculate_value_at_risk(returns, confidence_level)
        return var
    
    def calculate_optimal_portfolio_weights(self, expected_returns, cov_matrix):
        """
        Calculate Optimal Portfolio Weights for maximum Sharpe ratio.
        """
        optimal_weights = calculate_optimal_weights(expected_returns, cov_matrix)
        return optimal_weights
    
    def calculate_portfolio_sharpe_ratio(self, weights, expected_returns, cov_matrix, risk_free_rate):
        """
        Calculate Sharpe ratio of a portfolio.
        """
        sharpe_ratio = calculate_portfolio_sharpe_ratio(weights, expected_returns, cov_matrix, risk_free_rate)
        return sharpe_ratio
    
    def calculate_profitability_ratio(self, profit, revenue):
        """
        Calculate Profitability Ratio (Profit Margin).
        """
        profitability_ratio = calculate_profitability_ratio(profit, revenue)
        return profitability_ratio
    
    def calculate_return_on_investment(self, gain, cost):
        """
        Calculate Return on Investment (ROI).
        """
        roi = calculate_return_on_investment(gain, cost)
        return roi
    
    def calculate_debt_to_equity_ratio(self, total_debt, total_equity):
        """
        Calculate Debt-to-Equity Ratio.
        """
        debt_to_equity_ratio = calculate_debt_to_equity_ratio(total_debt, total_equity)
        return debt_to_equity_ratio

# Example usage:
initial_investment = -100000  # Initial investment cost (negative value)
cash_flows = [30000, 40000, 50000, 60000, 70000]  # Future cash flows (positive values)

# Create an instance of FinancialModeling
financial_model = FinancialModeling(initial_investment, cash_flows)

# Calculate NPV, IRR, Payback Period
discount_rate = 0.1  # Discount rate per period (10%)
npv_result = financial_model.calculate_npv(discount_rate)
irr_result = financial_model.calculate_irr()
payback_period_result = financial_model.calculate_payback_period()

print("Net Present Value (NPV): ${:,.2f}".format(npv_result))
print("Internal Rate of Return (IRR): {:.2%}".format(irr_result))
print("Payback Period: {} periods".format(payback_period_result))

# Other financial analysis
profit = 50000  # Profit generated (positive value)
revenue = 200000  # Total revenue (positive value)
profitability_ratio = financial_model.calculate_profitability_ratio(profit, revenue)
print("Profitability Ratio (Profit Margin): {:.2f}%".format(profitability_ratio))

# Additional functionalities (e.g., risk management, portfolio optimization) can be integrated similarly.
