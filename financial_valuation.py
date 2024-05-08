import numpy as np

def calculate_present_value(cash_flow, discount_rate, time_period):
    """
    Calculate the present value of a future cash flow using a discount rate.
    """
    present_value = cash_flow / ((1 + discount_rate) ** time_period)
    return present_value

def calculate_npv(initial_investment, cash_flows, discount_rate):
    """
    Calculate the Net Present Value (NPV) of an investment project.
    """
    npv = initial_investment
    for t, cash_flow in enumerate(cash_flows):
        npv += calculate_present_value(cash_flow, discount_rate, t + 1)
    return npv

def calculate_irr(initial_investment, cash_flows):
    """
    Calculate the Internal Rate of Return (IRR) of an investment project.
    """
    cash_flows_with_investment = [initial_investment] + cash_flows
    irr = np.irr(cash_flows_with_investment)
    return irr

def calculate_payback_period(initial_investment, cash_flows):
    """
    Calculate the Payback Period of an investment project.
    """
    cumulative_cash_flow = initial_investment
    payback_period = 0
    for cash_flow in cash_flows:
        cumulative_cash_flow += cash_flow
        payback_period += 1
        if cumulative_cash_flow >= 0:
            return payback_period
    return None
