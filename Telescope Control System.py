import serial
import time
import numpy as np

class TelescopeControl:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        self.current_position = np.array([0.0, 0.0])  # Assuming a 2D telescope, adjust if needed

    def move_telescope(self, azimuth, altitude):
        # Send commands to move telescope to specified azimuth and altitude
        command = f"AZ{azimuth:0.2f} ALT{altitude:0.2f}\n"  # Adjust format based on your telescope's protocol
        self.ser.write(command.encode())
        response = self.ser.readline().decode().strip()  # Read response from telescope
        print("Telescope response:", response)
        self.current_position = np.array([azimuth, altitude])

    def track_object(self, object_coordinates):
        # Example function to track a celestial object based on its coordinates
        target_azimuth, target_altitude = object_coordinates
        # Calculate difference between current and target positions
        delta_azimuth = target_azimuth - self.current_position[0]
        delta_altitude = target_altitude - self.current_position[1]
        # Move telescope to track the object
        self.move_telescope(self.current_position[0] + delta_azimuth, self.current_position[1] + delta_altitude)

    def park_telescope(self):
        # Example function to park the telescope at a predefined position
        self.move_telescope(0.0, 0.0)  # Assuming home position is at azimuth=0, altitude=0

# Example usage:
if __name__ == "__main__":
    telescope = TelescopeControl()  # Initialize telescope control
    # Move telescope to specific coordinates
    telescope.move_telescope(45.0, 30.0)  # Example: azimuth=45, altitude=30
    # Track a celestial object (e.g., specified by its coordinates)
    telescope.track_object([50.0, 40.0])  # Example: object at azimuth=50, altitude=40
    # Park the telescope at home position
    telescope.park_telescope()
