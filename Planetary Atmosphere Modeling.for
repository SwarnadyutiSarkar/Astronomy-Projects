program atmosphere_model

    implicit none
    
    ! Constants
    real, parameter :: g = 9.81  ! Acceleration due to gravity (m/s^2)
    real, parameter :: Cp = 1004.0  ! Specific heat capacity at constant pressure (J/kg/K)
    real, parameter :: lapse_rate = 0.0098  ! Adiabatic lapse rate (K/m)
    
    ! Variables
    real :: altitude, temperature
    
    ! Open output file
    open(unit=10, file='temperature_profile.txt', status='replace')
    
    ! Write header
    write(10, '(A)') 'Altitude (m)    Temperature (K)'
    
    ! Calculate temperature profile from surface to 20 km altitude
    altitude = 0.0
    do while (altitude <= 20000.0)
        temperature = 288.0 - lapse_rate * altitude
        write(10, '(F10.2, 2X, F10.2)') altitude, temperature
        altitude = altitude + 1000.0  ! Increment altitude by 1 km
    end do
    
    ! Close output file
    close(unit=10)
    
end program atmosphere_model
