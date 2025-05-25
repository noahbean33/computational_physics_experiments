"""
Common physics calculations and utilities.
"""
import numpy as np
from typing import Union, Tuple

def normalize_vector(v: Union[list, np.ndarray]) -> np.ndarray:
    """Normalize a vector to unit length.
    
    Args:
        v: Input vector (list or numpy array)
        
    Returns:
        numpy.ndarray: Normalized vector
    """
    v = np.asarray(v, dtype=float)
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

def cartesian_to_spherical(x: float, y: float, z: float) -> Tuple[float, float, float]:
    """Convert Cartesian coordinates to spherical coordinates (r, theta, phi).
    
    Args:
        x, y, z: Cartesian coordinates
        
    Returns:
        Tuple of (r, theta, phi) where:
        - r: radial distance
        - theta: polar angle (0 to π)
        - phi: azimuthal angle (0 to 2π)
    """
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z / r) if r != 0 else 0.0
    phi = np.arctan2(y, x)
    return r, theta, phi

def spherical_to_cartesian(r: float, theta: float, phi: float) -> Tuple[float, float, float]:
    """Convert spherical coordinates to Cartesian coordinates.
    
    Args:
        r: radial distance
        theta: polar angle (0 to π)
        phi: azimuthal angle (0 to 2π)
        
    Returns:
        Tuple of (x, y, z) Cartesian coordinates
    """
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z

def euler_step(dydx: callable, x: float, y: Union[float, np.ndarray], h: float, *args):
    """Perform one step of Euler's method for ODEs.
    
    Args:
        dydx: Function that computes the derivative dy/dx
        x: Current x value
        y: Current y value(s)
        h: Step size
        *args: Additional arguments to pass to dydx
        
    Returns:
        Updated y value(s) after one Euler step
    """
    return y + h * dydx(x, y, *args)

def rk4_step(dydx: callable, x: float, y: Union[float, np.ndarray], h: float, *args):
    """Perform one step of the 4th-order Runge-Kutta method for ODEs.
    
    Args:
        dydx: Function that computes the derivative dy/dx
        x: Current x value
        y: Current y value(s)
        h: Step size
        *args: Additional arguments to pass to dydx
        
    Returns:
        Updated y value(s) after one RK4 step
    """
    k1 = h * dydx(x, y, *args)
    k2 = h * dydx(x + 0.5*h, y + 0.5*k1, *args)
    k3 = h * dydx(x + 0.5*h, y + 0.5*k2, *args)
    k4 = h * dydx(x + h, y + k3, *args)
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6

def fermi_dirac(energy: Union[float, np.ndarray], mu: float, kT: float) -> Union[float, np.ndarray]:
    """Fermi-Dirac distribution function.
    
    Args:
        energy: Energy value(s)
        mu: Chemical potential
        kT: Temperature in energy units (Boltzmann constant * temperature)
        
    Returns:
        Occupation probability
    """
    if kT == 0:
        return np.where(energy <= mu, 1.0, 0.0)
    return 1.0 / (np.exp((energy - mu) / kT) + 1.0)
