#include <iostream>
#include <vector>
#include <cmath>

// Constants
const int N = 1000;  // Number of particles
const int Ngrid = 128;  // Grid size for PM method
const double L = 100.0;  // Box size (Mpc/h)
const double G = 6.67430e-11;  // Gravitational constant (m^3/kg/s^2)
const double M = 1.989e30;  // Solar mass (kg)

// Particle structure
struct Particle {
    double x, y, z;  // Position
    double vx, vy, vz;  // Velocity
    double mass;  // Mass
};

// Simulation parameters
const double dt = 0.1;  // Time step (Gyr)
const int num_steps = 100;  // Number of time steps

// Particle-mesh (PM) method
void particleMesh(std::vector<Particle>& particles, std::vector<double>& potential) {
    // Initialize potential grid
    std::vector<double> grid(Ngrid * Ngrid * Ngrid, 0.0);

    // Compute potential using PM method
    for (const auto& particle : particles) {
        int i = static_cast<int>(particle.x / L * Ngrid);
        int j = static_cast<int>(particle.y / L * Ngrid);
        int k = static_cast<int>(particle.z / L * Ngrid);
        grid[i * Ngrid * Ngrid + j * Ngrid + k] += particle.mass;
    }

    // Compute potential at particle positions
    for (int idx = 0; idx < particles.size(); ++idx) {
        int i = static_cast<int>(particles[idx].x / L * Ngrid);
        int j = static_cast<int>(particles[idx].y / L * Ngrid);
        int k = static_cast<int>(particles[idx].z / L * Ngrid);
        particles[idx].vx += -G * grid[i * Ngrid * Ngrid + j * Ngrid + k] / (particles[idx].mass * L);
        particles[idx].vy += -G * grid[i * Ngrid * Ngrid + j * Ngrid + k] / (particles[idx].mass * L);
        particles[idx].vz += -G * grid[i * Ngrid * Ngrid + j * Ngrid + k] / (particles[idx].mass * L);
    }

    // Store potential for analysis (optional)
    potential = grid;
}

// Run simulation
void runSimulation(std::vector<Particle>& particles) {
    std::vector<double> potential;

    for (int step = 0; step < num_steps; ++step) {
        // Perform PM method
        particleMesh(particles, potential);

        // Update particle positions
        for (auto& particle : particles) {
            particle.x += particle.vx * dt;
            particle.y += particle.vy * dt;
            particle.z += particle.vz * dt;
        }

        // Output current step (optional)
        std::cout << "Step " << step + 1 << "/" << num_steps << std::endl;
    }
}

int main() {
    // Initialize particles with random positions and velocities
    std::vector<Particle> particles(N);
    for (auto& particle : particles) {
        particle.x = L * static_cast<double>(rand()) / RAND_MAX;
        particle.y = L * static_cast<double>(rand()) / RAND_MAX;
        particle.z = L * static_cast<double>(rand()) / RAND_MAX;
        particle.vx = 0.0;  // Initial velocity (optional)
        particle.vy = 0.0;  // Initial velocity (optional)
        particle.vz = 0.0;  // Initial velocity (optional)
        particle.mass = M / N;  // Equal mass particles
    }

    // Run simulation
    runSimulation(particles);

    return 0;
}
