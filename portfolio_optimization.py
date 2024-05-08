import numpy as np
from scipy.optimize import minimize

def calculate_portfolio_return(weights, expected_returns):
    """
    Calculate the expected return of a portfolio given weights and expected returns.
    """
    portfolio_return = np.dot(weights.T, expected_returns)
    return portfolio_return

def calculate_portfolio_volatility(weights, cov_matrix):
    """
    Calculate the volatility (standard deviation) of a portfolio given weights and covariance matrix.
    """
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return portfolio_volatility

def calculate_optimal_weights(expected_returns, cov_matrix):
    """
    Calculate the optimal weights for maximum Sharpe ratio portfolio.
    """
    num_assets = len(expected_returns)
    initial_weights = np.array([1 / num_assets] * num_assets)  # Initial equal weights
    bounds = tuple((0, 1) for asset in range(num_assets))  # Bounds for weights (0 to 1)
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})  # Sum of weights = 1
    
    def negative_sharpe_ratio(weights, expected_returns, cov_matrix):
        portfolio_return = calculate_portfolio_return(weights, expected_returns)
        portfolio_volatility = calculate_portfolio_volatility(weights, cov_matrix)
        sharpe_ratio = portfolio_return / portfolio_volatility
        return -sharpe_ratio
    
    optimal_weights = minimize(negative_sharpe_ratio, initial_weights,
                               args=(expected_returns, cov_matrix),
                               bounds=bounds, constraints=constraints)
    
    return optimal_weights.x

def calculate_portfolio_sharpe_ratio(weights, expected_returns, cov_matrix, risk_free_rate):
    """
    Calculate the Sharpe ratio of a portfolio given weights, expected returns, and risk-free rate.
    """
    portfolio_return = calculate_portfolio_return(weights, expected_returns)
    portfolio_volatility = calculate_portfolio_volatility(weights, cov_matrix)
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility
    return sharpe_ratio
