import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

def load_image(filename):
    """
    Load an astronomical image from a FITS file.
    """
    with fits.open(filename) as hdul:
        image_data = hdul[0].data
    return image_data

def plot_image(image_data, title='Astronomical Image'):
    """
    Plot the astronomical image.
    """
    plt.figure(figsize=(8, 6))
    plt.imshow(image_data, cmap='gray', origin='lower')
    plt.colorbar(label='Intensity')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def process_image(image_data):
    """
    Process the astronomical image (e.g., background subtraction, noise reduction).
    """
    # Example: Subtract background (mean value) and apply Gaussian smoothing
    background = np.mean(image_data)
    processed_image = image_data - background
    processed_image = gaussian_smoothing(processed_image)
    return processed_image

def gaussian_smoothing(image_data, sigma=2):
    """
    Apply Gaussian smoothing to the image.
    """
    from scipy.ndimage import gaussian_filter
    smoothed_image = gaussian_filter(image_data, sigma=sigma)
    return smoothed_image

# Example usage:
if __name__ == "__main__":
    # Load the astronomical image
    filename = 'astronomical_image.fits'
    image_data = load_image(filename)

    # Process the image
    processed_image = process_image(image_data)

    # Plot the original and processed images
    plot_image(image_data, title='Original Astronomical Image')
    plot_image(processed_image, title='Processed Astronomical Image')
