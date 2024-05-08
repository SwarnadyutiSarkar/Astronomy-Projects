import numpy as np
from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from astropy.visualization import SqrtStretch, ZScaleInterval, ImageNormalize
from photutils import DAOStarFinder, CircularAperture, aperture_photometry
import matplotlib.pyplot as plt

# Load FITS image
def load_image(filename):
    with fits.open(filename) as hdul:
        image_data = hdul[0].data
    return image_data

# Background subtraction
def subtract_background(image_data):
    mean, median, std = sigma_clipped_stats(image_data)
    return image_data - median

# Detect stars using DAOStarFinder
def detect_stars(image_data, fwhm=3.0, threshold=5.0):
    daofind = DAOStarFinder(fwhm=fwhm, threshold=threshold)
    sources = daofind(image_data)
    return sources

# Measure properties of detected stars
def measure_stars(image_data, sources, aperture_radius=5.0):
    positions = np.transpose((sources['xcentroid'], sources['ycentroid']))
    apertures = CircularAperture(positions, r=aperture_radius)
    phot_table = aperture_photometry(image_data, apertures)
    return phot_table

# Plot image with detected stars
def plot_image_with_stars(image_data, sources):
    plt.figure(figsize=(10, 8))
    norm = ImageNormalize(stretch=SqrtStretch(), interval=ZScaleInterval())
    plt.imshow(image_data, cmap='gray', origin='lower', norm=norm)
    plt.colorbar(label='Intensity')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Sky Survey Image with Detected Stars')
    plt.plot(sources['xcentroid'], sources['ycentroid'], 'ro', markersize=10)
    plt.show()

if __name__ == '__main__':
    # Load sky survey image
    filename = 'sky_survey_image.fits'
    image_data = load_image(filename)

    # Subtract background
    background_subtracted = subtract_background(image_data)

    # Detect stars
    sources = detect_stars(background_subtracted)

    # Measure properties of detected stars
    phot_table = measure_stars(background_subtracted, sources)

    # Plot image with detected stars
    plot_image_with_stars(background_subtracted, sources)

    # Print measured properties of stars
    print(phot_table)
