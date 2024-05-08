#include <iostream>
#include <cmath>

class Star {
private:
    double mass; // Mass of the star in solar masses
    double luminosity; // Luminosity of the star in solar luminosities
    double temperature; // Surface temperature of the star in Kelvin

public:
    // Constructor
    Star(double m, double l, double t) : mass(m), luminosity(l), temperature(t) {}

    // Getters
    double getMass() const { return mass; }
    double getLuminosity() const { return luminosity; }
    double getTemperature() const { return temperature; }

    // Calculate the main sequence lifetime of the star in years
    double calculateMainSequenceLifetime() const {
        return pow(mass, -2.5) * 1.0e10;
    }

    // Calculate the radius of the star in solar radii
    double calculateRadius() const {
        return sqrt(luminosity) / temperature / 3.828e26;
    }
};

int main() {
    // Create a star object with mass = 1 solar mass, luminosity = 1 solar luminosity, and temperature = 5778 K (Sun-like)
    Star sun(1.0, 1.0, 5778.0);

    // Calculate and print the main sequence lifetime of the star
    double mainSeqLifetime = sun.calculateMainSequenceLifetime();
    std::cout << "Main Sequence Lifetime: " << mainSeqLifetime << " years" << std::endl;

    // Calculate and print the radius of the star
    double radius = sun.calculateRadius();
    std::cout << "Radius: " << radius << " solar radii" << std::endl;

    return 0;
}
