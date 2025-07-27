"""Test for kahane_simplify gamma matrices functions."""

from sympy.physics.hep.gamma_matrices import GammaMatrix as G, gamma_trace, LorentzIndex
from sympy.physics.hep.gamma_matrices import kahane_simplify
from sympy.tensor.tensor import tensor_indices


def test_kahane_leading_gamma_matrix_bug():
    """Test that kahane_simplify preserves order of leading gamma matrices."""
    mu, nu, rho, sigma = tensor_indices("mu, nu, rho, sigma", LorentzIndex)

    # Test case 1: G(mu)*G(-mu)*G(rho)*G(sigma)
    t = G(mu)*G(-mu)*G(rho)*G(sigma)
    r = kahane_simplify(t)
    assert r.equals(4*G(rho)*G(sigma))

    # Test case 2: G(rho)*G(sigma)*G(mu)*G(-mu)
    t = G(rho)*G(sigma)*G(mu)*G(-mu)
    r = kahane_simplify(t)
    assert r.equals(4*G(rho)*G(sigma))