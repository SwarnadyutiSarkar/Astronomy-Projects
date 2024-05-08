import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d

# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
c = 299792458  # Speed of light (m/s)
M_bh = 1.989e30  # Mass of the black hole (kg)
D = 1.5e21  # Distance to the observer (m)

# Parameters
theta_E = (4 * G * M_bh / c**2 / D)**0.5  # Einstein radius (radians)
grid_size = 1000  # Grid size for the simulation
extent = 10 * theta_E  # Extent of the image (radians)

# Generate image grid
x = np.linspace(-extent / 2, extent / 2, grid_size)
y = np.linspace(-extent / 2, extent / 2, grid_size)
xx, yy = np.meshgrid(x, y)

# Calculate deflection angle
deflection_angle = 4 * G * M_bh / c**2 / D * np.log(np.sqrt(xx**2 + yy**2) / theta_E)

# Interpolate deflection angle
interp_func = interp2d(x, y, deflection_angle, kind='cubic')

# Generate lensed image
def generate_lensed_image(source_image):
    lensed_image = np.zeros_like(source_image)
    for i in range(grid_size):
        for j in range(grid_size):
            xi = x[i] - interp_func(x[i], y[j])[0]
            yj = y[j] - interp_func(x[i], y[j])[1]
            if -extent / 2 <= xi <= extent / 2 and -extent / 2 <= yj <= extent / 2:
                lensed_image[j, i] = source_image[int((yj + extent / 2) / extent * (grid_size - 1)), int((xi + extent / 2) / extent * (grid_size - 1))]
    return lensed_image

# Plot original and lensed images
def plot_images(original_image, lensed_image):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(original_image, extent=(-extent / 2, extent / 2, -extent / 2, extent / 2), cmap='inferno')
    plt.colorbar(label='Intensity')
    plt.title('Original Source Image')
    plt.xlabel('X (radians)')
    plt.ylabel('Y (radians)')
    
    plt.subplot(1, 2, 2)
    plt.imshow(lensed_image, extent=(-extent / 2, extent / 2, -extent / 2, extent / 2), cmap='inferno')
    plt.colorbar(label='Intensity')
    plt.title('Lensed Image')
    plt.xlabel('X (radians)')
    plt.ylabel('Y (radians)')
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # Generate source image (e.g., a Gaussian profile)
    source_image = np.exp(-((xx / (0.5 * extent))**2 + (yy / (0.5 * extent))**2))

    # Generate lensed image
    lensed_image = generate_lensed_image(source_image)

    # Plot original and lensed images
    plot_images(source_image, lensed_image)
