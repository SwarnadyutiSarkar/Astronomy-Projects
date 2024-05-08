 import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Constants
G = 4.300e-6  # Gravitational constant in units of (km/s)^2 * kpc / Msun

# Define NFW density profile
def nfw_density(r, rs, rho_0):
    x = r / rs
    return rho_0 / (x * (1 + x)**2)

# Calculate total mass enclosed within a given radius using NFW profile
def enclosed_mass(r, rs, rho_0):
    return 4 * np.pi * rho_0 * rs**3 * (np.log((rs + r) / rs) - r / (rs + r))

# Calculate circular velocity using NFW profile
def circular_velocity(r, rs, rho_0):
    return np.sqrt(G * enclosed_mass(r, rs, rho_0) / r)

# Plot density profile
def plot_density_profile(rs, rho_0):
    r = np.logspace(-2, 2, num=100)
    density = nfw_density(r, rs, rho_0)
    plt.figure(figsize=(8, 6))
    plt.plot(r, density, color='b')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Radius (kpc)')
    plt.ylabel('Density ($M_{\odot}$/kpc$^3$)')
    plt.title('Dark Matter Halo Density Profile (NFW)')
    plt.grid(True)
    plt.show()

# Plot circular velocity profile
def plot_circular_velocity(rs, rho_0):
    r = np.logspace(-2, 2, num=100)
    v_circ = circular_velocity(r, rs, rho_0)
    plt.figure(figsize=(8, 6))
    plt.plot(r, v_circ, color='r')
    plt.xscale('log')
    plt.xlabel('Radius (kpc)')
    plt.ylabel('Circular Velocity (km/s)')
    plt.title('Circular Velocity Profile (NFW)')
    plt.grid(True)
    plt.show()

# Calculate and print total mass within a given radius
def print_enclosed_mass(radius, rs, rho_0):
    total_mass = enclosed_mass(radius, rs, rho_0)
    print(f'Total Mass Enclosed within {radius} kpc: {total_mass:.2e} Msun')

if __name__ == '__main__':
    # Parameters for NFW profile (scale radius and characteristic density)
    rs = 10  # Scale radius in kpc
    rho_0 = 1e7  # Characteristic density in Msun/kpc^3

    # Plot density profile
    plot_density_profile(rs, rho_0)

    # Plot circular velocity profile
    plot_circular_velocity(rs, rho_0)

    # Calculate and print total mass within a given radius
    radius = 50  # Radius in kpc
    print_enclosed_mass(radius, rs, rho_0)
