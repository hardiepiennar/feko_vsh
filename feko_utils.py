"""
Reading and manipulating FEKO files

Hardie Pienaar
Cavendish Lab
Oct 2017
"""

import csv
import numpy as np

def read_outfile(filename):
    """
    Reads out file and returns all of the available data
    :param filename: filename and directory as string
    :return: Z: impedance
    :return: sph: spherical harmonics [freq, (J, mag, phase), J_index]
    """

    # open out file
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')

        # Read row
        read_sph_modes = False
        J = []
        sph_mag = []
        sph_phase = []
        sph = []
        freq = []
        impedance = []
        for row in reader:
            row = list(filter(None, row))   # Filter out empty items

            # Get data points for this frequency
            if "FREQ" in row:
                # Make sure this is the first time we read this frequency
                if len(freq) == 0 or not (freq[-1] == float(row[5])):
                    freq.append(float(row[5]))
            if "Impedance" in row:
                impedance.append(float(row[4]) + 1j*float(row[5]))
            if read_sph_modes:
                if len(row) < 7:
                    read_sph_modes = False
                    sph.append({"J":np.array(J), "Mag":np.array(sph_mag), "Phase":np.array(sph_phase)})
                    J = []
                    sph_mag = []
                    sph_phase = []
                else:
                    J.append(int(row[0]))
                    sph_mag.append(float(row[4]))
                    sph_phase.append(float(row[5]))
            if "J" in row:
                read_sph_modes = True

        return freq, impedance, sph




