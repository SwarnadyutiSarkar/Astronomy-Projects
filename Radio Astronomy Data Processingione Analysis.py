import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy.signal import find_peaks

# Load radio astronomy data from FITS file
def load_radio_data(filename):
    with fits.open(filename) as hdul:
        data = hdul[0].data
    return data

# Perform data processing and analysis
def analyze_radio_data(data, threshold):
    # Example: Find peaks in the data
    peaks, _ = find_peaks(data, height=threshold)
    return peaks

# Plot the radio astronomy data with detected peaks
def plot_radio_data_with_peaks(data, peaks):
    plt.figure(figsize=(10, 6))
    plt.plot(data, label='Radio Astronomy Data')
    plt.plot(peaks, data[peaks], 'ro', label='Detected Peaks')
    plt.xlabel('Time (arb. units)')
    plt.ylabel('Intensity (arb. units)')
    plt.title('Radio Astronomy Data with Detected Peaks')
    plt.legend()
    plt.grid(True)
    plt.show()

# Load radio astronomy data file
filename = 'radio_data.fits'  # Example radio astronomy data file

# Load radio astronomy data
data = load_radio_data(filename)

# Define threshold for peak detection
threshold = 0.5  # Adjust as needed

# Analyze the data
peaks = analyze_radio_data(data, threshold)

# Plot the data with detected peaks
plot_radio_data_with_peaks(data, peaks)
