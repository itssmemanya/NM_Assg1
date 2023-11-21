import numpy as np
import matplotlib.pyplot as plt

# Declaring constants
h = 6.62607015e-34  # Planck's constant 
c = 3.0e8           # Speed of light 
k = 1.380649e-23    # Boltzmann constant 


def black_body_spectrum(freq, T):
    x = (h * freq) / (k * T)
    return 2 * h * (freq ** 3) * np.exp(-x) / ((1 - np.exp(-x)) * c ** 2)

# Importing textfile containing required data
frequency = np.loadtxt("firas_monopole_spec_v1.txt")[:, 0]
cmb_flux = np.loadtxt("firas_monopole_spec_v1.txt")[:, 1]

temp = 2.725
intensity = black_body_spectrum(frequency*3e10, temp)

# Finding the wavelength at which the CMB peaks
max_index = np.argmax(cmb_flux)
max_wav = 1/frequency[max_index]
print("Wavelength at which black body peaks (cm): ",max_wav)

# Adding labels 
plt.title("CMB Monopole Spectrum")
plt.xlabel("frequency(Hz)")
plt.ylabel("CMB Flux(W / m^2 / Hz / sr)")
# Plotting the cmb data points from the file
plt.scatter(frequency * 3e10, cmb_flux*1e-20, color="red", label='Data points')
# Plotting the planck radiation function
plt.plot(frequency*3e10, intensity, color="green", label='Planck radiation function') 
plt.show()
