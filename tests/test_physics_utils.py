"""
Tests for the physics_utils module.
"""
import numpy as np
import pytest
from src.utils.physics_utils import (
    normalize_vector,
    cartesian_to_spherical,
    spherical_to_cartesian,
    euler_step,
    rk4_step,
    fermi_dirac
)

# Test data
VECTOR = [1, 2, 3]
NORMALIZED_VECTOR = np.array([0.26726124, 0.53452248, 0.80178373])
CARTESIAN_POINT = (1.0, 1.0, 1.0)
SPHERICAL_POINT = (np.sqrt(3), 0.955316618, 0.785398163)  # (r, theta, phi)

def test_normalize_vector():
    """Test vector normalization."""
    result = normalize_vector(VECTOR)
    np.testing.assert_allclose(result, NORMALIZED_VECTOR, rtol=1e-8)
    
    # Test zero vector
    zero_vec = [0, 0, 0]
    result = normalize_vector(zero_vec)
    np.testing.assert_array_equal(result, zero_vec)

def test_cartesian_to_spherical():
    """Test Cartesian to spherical coordinates conversion."""
    x, y, z = CARTESIAN_POINT
    r, theta, phi = cartesian_to_spherical(x, y, z)
    
    # Check against precomputed values
    expected_r, expected_theta, expected_phi = SPHERICAL_POINT
    assert np.isclose(r, expected_r, rtol=1e-8)
    assert np.isclose(theta, expected_theta, rtol=1e-6)
    assert np.isclose(phi, expected_phi, rtol=1e-6)
    
    # Test origin
    r, theta, phi = cartesian_to_spherical(0, 0, 0)
    assert r == 0
    assert theta == 0  # By convention

def test_spherical_to_cartesian():
    """Test spherical to Cartesian coordinates conversion."""
    r, theta, phi = SPHERICAL_POINT
    x, y, z = spherical_to_cartesian(r, theta, phi)
    
    # Should convert back to original Cartesian coordinates
    expected_x, expected_y, expected_z = CARTESIAN_POINT
    assert np.isclose(x, expected_x, rtol=1e-8)
    assert np.isclose(y, expected_y, rtol=1e-8)
    assert np.isclose(z, expected_z, rtol=1e-8)

def test_euler_step():
    """Test Euler's method step."""
    # Test with simple ODE: dy/dx = y, y(0) = 1
    # Solution: y(x) = e^x
    def dydx(x, y):
        return y
    
    x0, y0 = 0.0, 1.0
    h = 0.1
    y1 = euler_step(dydx, x0, y0, h)
    
    # Compare with exact solution
    exact = np.exp(h)
    assert np.isclose(y1, 1.1, rtol=1e-2)  # First order approximation
    assert abs(y1 - exact) > 0  # Should have some error

def test_rk4_step():
    """Test 4th-order Runge-Kutta step."""
    # Test with simple ODE: dy/dx = y, y(0) = 1
    # Solution: y(x) = e^x
    def dydx(x, y):
        return y
    
    x0, y0 = 0.0, 1.0
    h = 0.1
    y1 = rk4_step(dydx, x0, y0, h)
    
    # Compare with exact solution
    exact = np.exp(h)
    assert np.isclose(y1, exact, rtol=1e-6)  # Should be very close

def test_fermi_dirac():
    """Test Fermi-Dirac distribution function."""
    # At T=0, should be step function
    energies = np.array([-1.0, 0.0, 1.0])
    mu = 0.0
    kT = 0.0
    expected = np.array([1.0, 1.0, 0.0])  # f(E) = 1 for E <= mu, 0 otherwise
    result = fermi_dirac(energies, mu, kT)
    np.testing.assert_array_equal(result, expected)
    
    # At finite temperature, should be smooth
    kT = 0.1
    result = fermi_dirac(mu, mu, kT)
    assert np.isclose(result, 0.5)  # At E = mu, f = 0.5
    
    # Test scalar input
    assert fermi_dirac(-1.0, mu, kT) > 0.9
    assert fermi_dirac(1.0, mu, kT) < 0.1

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
