import pytest

def test_portfolio_weights_normalization():
    """Verify that asset allocation weights sum to 1.0 (100% portfolio allocation)."""
    weights = [0.35, 0.25, 0.20, 0.20]  # Multi-asset portfolio weights
    
    total_allocation = sum(weights)
    
    assert pytest.approx(total_allocation, 0.0001) == 1.0

def test_portfolio_expected_return():
    """Verify portfolio expected return calculation given asset weights and expected returns."""
    weights = [0.5, 0.5]
    expected_returns = [0.12, 0.08]  # 12% and 8% expected returns
    
    portfolio_return = sum(w * r for w, r in zip(weights, expected_returns))
    
    assert pytest.approx(portfolio_return, 0.001) == 0.10
