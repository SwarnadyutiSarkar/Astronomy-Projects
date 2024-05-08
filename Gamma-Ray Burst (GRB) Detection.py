import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, peak_prominences

# Simulate GRB data
def simulate_grb_data(duration, peak_time, peak_intensity, noise_level):
    time = np.linspace(0, duration, num=1000)
    data = np.random.normal(0, noise_level, size=len(time))
    data[int(peak_time * len(time) / duration)] += peak_intensity
    return time, data

# Detect GRBs in the data
def detect_grbs(time, data, threshold):
    peaks, _ = find_peaks(data, height=threshold)
    prominences = peak_prominences(data, peaks)[0]
    grb_indices = peaks[prominences > threshold]  # Select peaks with prominence above threshold
    return grb_indices

# Plot GRB data with detected bursts
def plot_grb_data(time, data, grb_indices):
    plt.figure(figsize=(10, 6))
    plt.plot(time, data, color='b', label='GRB Data')
    plt.scatter(time[grb_indices], data[grb_indices], color='r', label='Detected GRBs')
    plt.xlabel('Time (s)')
    plt.ylabel('Intensity')
    plt.title('Gamma-Ray Burst (GRB) Detection')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    # Simulate GRB data
    duration = 10  # Duration of observation in seconds
    peak_time = 5  # Time of GRB peak in seconds
    peak_intensity = 10  # Intensity of GRB peak
    noise_level = 1  # Level of background noise
    time, data = simulate_grb_data(duration, peak_time, peak_intensity, noise_level)

    # Detect GRBs in the data
    threshold = 3  # Adjust as needed
    grb_indices = detect_grbs(time, data, threshold)

    # Plot GRB data with detected bursts
    plot_grb_data(time, data, grb_indices)

    # Print detected GRB indices
    print("Detected GRB Indices:", grb_indices)
