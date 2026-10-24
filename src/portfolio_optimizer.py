import numpy as np

def calculate_portfolio_metrics(weights: np.ndarray, expected_returns: np.ndarray, cov_matrix: np.ndarray, risk_free_rate: float):
    """
    Calculates expected portfolio return, annualized variance, and the Sharpe Ratio.
    """
    port_return = np.dot(weights, expected_returns)
    port_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
    port_volatility = np.sqrt(port_variance)
    sharpe_ratio = (port_return - risk_free_rate) / port_volatility
    return port_return, port_volatility, sharpe_ratio

def run_monte_carlo_optimization(assets: list, expected_returns: np.ndarray, cov_matrix: np.ndarray, risk_free_rate: float, num_simulations: int = 10000):
    """
    Executes a Monte Carlo simulation to plot the Efficient Frontier 
    and isolate the Max Sharpe Ratio portfolio allocation.
    """
    num_assets = len(assets)
    all_weights = np.zeros((num_simulations, num_assets))
    ret_arr = np.zeros(num_simulations)
    vol_arr = np.zeros(num_simulations)
    sharpe_arr = np.zeros(num_simulations)
    
    print(f"Running {num_simulations:,} Portfolio Optimization Simulations...")
    np.random.seed(42)
    
    for i in range(num_simulations):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        all_weights[i, :] = weights
        
        p_ret, p_vol, p_sharpe = calculate_portfolio_metrics(weights, expected_returns, cov_matrix, risk_free_rate)
        ret_arr[i] = p_ret
        vol_arr[i] = p_vol
        sharpe_arr[i] = p_sharpe
        
    max_sharpe_idx = sharpe_arr.argmax()
    optimal_weights = all_weights[max_sharpe_idx, :]
    
    print("\n================ OPTIMAL ASSET ALLOCATION (MAX SHARPE) ================")
    for asset, weight in zip(assets, optimal_weights):
        print(f"Asset: {asset:<8} | Target Allocation Weight: {weight * 100:>6.2f}%")
        
    print("\n================== EXPECTED PORTFOLIO METRICS ==================")
    print(f"Expected Annualized Return: {ret_arr[max_sharpe_idx] * 100:.2f}%")
    print(f"Expected Annualized Risk:   {vol_arr[max_sharpe_idx] * 100:.2f}%")
    print(f"Maximized Sharpe Ratio:     {sharpe_arr[max_sharpe_idx]:.4f}")
    print("=================================================================")
    
    return optimal_weights

if __name__ == "__main__":
    asset_basket = ["SPY", "TLT", "GLD", "DBC"]
    simulated_returns = np.array([0.10, 0.04, 0.06, 0.05])
    simulated_cov = np.array([
        [0.0225, -0.0025, 0.0015,  0.0045],
        [-0.0025, 0.0081, 0.0020, -0.0010],
        [0.0015,  0.0020, 0.0144,  0.0030],
        [0.0045, -0.0010, 0.0030,  0.0196]
    ])
    
    run_monte_carlo_optimization(
        assets=asset_basket,
        expected_returns=simulated_returns,
        cov_matrix=simulated_cov,
        risk_free_rate=0.045
    )

