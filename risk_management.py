import numpy as np

def calculate_portfolio_var(cov_matrix, weights):
    """
    Calculate the variance of a portfolio given covariance matrix and weights.
    """
    portfolio_var = np.dot(weights.T, np.dot(cov_matrix, weights))
    return portfolio_var

def calculate_portfolio_volatility(cov_matrix, weights):
    """
    Calculate the volatility (standard deviation) of a portfolio.
    """
    portfolio_var = calculate_portfolio_var(cov_matrix, weights)
    portfolio_volatility = np.sqrt(portfolio_var)
    return portfolio_volatility

def calculate_value_at_risk(returns, confidence_level=0.95):
    """
    Calculate the Value at Risk (VaR) of an investment/portfolio.
    """
    var = np.percentile(returns, (1 - confidence_level) * 100)
    return var
