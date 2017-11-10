"""
Functions for calculating vector spherical harmonics specifically to match the output in FEKO.
As a result, the code comes with a complimentary scaling fudge factor. Feel free to help me
remove it.

Hardie Pienaar
Cavendish Lab
Oct 2017
"""

# Lets import some things
import numpy as np
import matplotlib.pyplot as plt
import scipy.special


def vsh(s, m, n, theta, phi, kr=0.05152015*(0.99993)):
    """
    Calculate vector spherical harmonics for given s, m, n parameters. 

    Arguments:
	    s - mode (0 - TE, 1 - TM)
	    n, m - harmonic parameters
	    k - wavenumber
	    r - distance from source
	    theta, phi - calculation coordinates 

	Returns:
		vsh_theta - theta component of vectorised spherical harmonic
		vsh_phi	- theta component of vectorised spherical harmonic
    """

    # Convert variable into numpy array
    if not isinstance(theta, np.ndarray):
        theta = np.array([theta])
    if not isinstance(phi, np.ndarray):
        phi = np.array([phi])

    # Dirty method to avoid dividing by 0 errors
    theta = theta + 0.0000001
    phi = phi + 0.00000001

   	# Keeps last coord term from exceeding pi or 2pi boundaries
    if len(theta) > 1:
        theta[-1] = theta[-1] - 0.0000001 * 2
    if len(phi) > 1:
        phi[-1] = phi[-1] - 0.0000001 * 2

    # Calculate the first term (note the fudge factor kr)
    A = np.power(-1, (1 - s)) * np.power(1j, n - s)/kr #* np.exp(-1j * kr) / kr
    B = (2 * n + 1) / (4 * np.pi * n * (n + 1))
    C = np.math.factorial(n - m) / np.math.factorial(n + m)

    # Calculate the legendre values
    Pmn = scipy.special.lpmv(m, n, np.cos(theta))
    Pmn_d1 = np.sqrt(1 - np.power(np.cos(theta), 2)) * scipy.special.lpmv(m + 1, n, np.cos(theta))
    Pmn_d2 = m * np.cos(theta) * Pmn
    Pmn_d3 = np.power(np.cos(theta), 2) - 1
    Pmn_d = (Pmn_d1 + Pmn_d2) / Pmn_d3

    # Calculate the middle term
    D = ((1j * m) / np.sin(theta)) * Pmn
    E = np.sin(theta) * Pmn_d

    # Depending on the mode a certain combination of the inner term is used
    if s == 0:
        phase_corr = 1j
        vsh = A * np.sqrt(B * C) * np.exp(1j * m * phi)
        vsh_theta = np.power(-1,np.abs(m))*-phase_corr * vsh * D
        vsh_phi = np.power(-1,np.abs(m))*-phase_corr * vsh * E
    else:
        phase_corr = 1j
        vsh = A * np.sqrt(B * C) * np.exp(1j * m * phi)
        vsh_theta = np.power(-1, np.abs(m))*-1j * vsh * E
        vsh_phi = -1j * vsh * D

    return vsh_theta, vsh_phi


def j2smn(j):
    """
    Translates the compact J form into the smn form

    Argument:
    	j - j index

    Returns:
    	s, m, n index terms
    """

    s = 2 - j%2
    n = (np.floor(np.sqrt(np.ceil(j/2))))
    m = (j-s)/2 + 1 - n*(n+1)

    return s, m, n


def create_pattern(theta_grid, phi_grid, structure):
    """
    Create a pattern from the vector spherical harmonics

    Arguments:
	    theta - theta angles in radians
	    phi - phi angle in radians
	    structure = [[J],
	                 [Magnitude],
	                 [Phase]]

    Returns: 
    	E-field pattern
    """

    # Decompress J
    s, m, n = j2smn(structure[0, :])

    # Build e-field
    e_theta = np.zeros(theta_grid.shape, dtype=complex)
    e_phi = np.zeros(theta_grid.shape, dtype=complex)
    for i in np.arange(len(s)):
        e_theta_t, e_phi_t = vsh(s[i]-1, m[i], n[i], theta_grid, phi_grid)
        mag = structure[1, i]
        phase = structure[2, i]*np.pi/180

        e_theta = e_theta + mag*np.exp(1j*phase)*e_theta_t
        e_phi = e_phi + mag*np.exp(1j*phase)*e_phi_t

    return e_theta, e_phi


def calc_total_power(farfield):
	"""
	Calculate the farfield power pattern from the complex farfield values

	Arguments:
		farfield - complex farfield values

	Returns:
		farfield - farfield scalar power values
	"""
    tot_power = np.sum(np.power(farfield[1], 2)) / 2
    return tot_power


def truncate_modes_at_power_fraction(farfield, fraction):
	"""
	Trunate list of modes leaving only the specified amount of power.
	Very usefull for compressing the spherical harmonics. This function
	can be further improved by throwing away in-bwtween 0 magnitude modes	

	Arguments:
		farfield - spherical mode data: [[J], [Magnitude], [Phase]]
		fraction - fraction of power to truncate data structure at

	Returns:
		truncated spherical mode data

	"""
    tot_power = calc_total_power(farfield)
    acc_power = 0
    index = 0
    while acc_power / tot_power < fraction:
        acc_power += np.sum(np.power(farfield[1, index], 2)) / 2
        index += 1
    return farfield[:, 0:index+1], index


def calc_gain(farfield, E):
	"""
	Calculate the farfield gain for a halfspace

	Arguments:
		farfield - complex farfield value
		E - Voltage applied at port

	Returns:
		farfield gain 
	"""
    Pt = calc_total_power(farfield)
    Ud = (np.abs(E) ** 2) / 376.730
    Um = Pt / (2 * np.pi) # For a halfsphere

    return Ud / Um


