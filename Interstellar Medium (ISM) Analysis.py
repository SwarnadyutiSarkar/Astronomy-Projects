import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.visualization import imshow_norm, MinMaxInterval, SqrtStretch

# Load ISM data (simulated example)
def load_ism_data(filename):
    with fits.open(filename) as hdul:
        data = hdul[0].data
    return data

# Preprocess ISM data
def preprocess_ism_data(data):
    # Normalize pixel values to range [0, 1]
    data = (data - np.min(data)) / (np.max(data) - np.min(data))
    return data

# Analyze ISM data
def analyze_ism_data(data):
    # Example analysis (replace with your own analysis code)
    mean_intensity = np.mean(data)
    max_intensity = np.max(data)
    min_intensity = np.min(data)
    return mean_intensity, max_intensity, min_intensity

# Visualize ISM data
def visualize_ism_data(data):
    plt.figure(figsize=(8, 6))
    norm = imshow_norm(data, interval=MinMaxInterval(), stretch=SqrtStretch())
    plt.imshow(data, cmap='viridis', norm=norm, origin='lower')
    plt.colorbar(label='Intensity')
    plt.title('Interstellar Medium (ISM) Data')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

if __name__ == '__main__':
    # Load ISM data (replace 'filename.fits' with your actual data file)
    filename = 'ism_data.fits'  # Example ISM data file
    ism_data = load_ism_data(filename)

    # Preprocess ISM data
    ism_data = preprocess_ism_data(ism_data)

    # Visualize ISM data
    visualize_ism_data(ism_data)

    # Analyze ISM data
    mean_intensity, max_intensity, min_intensity = analyze_ism_data(ism_data)

    # Print analysis results
    print("Mean Intensity:", mean_intensity)
    print("Maximum Intensity:", max_intensity)
    print("Minimum Intensity:", min_intensity)
