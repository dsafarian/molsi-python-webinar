"""
This module has functions associated with analyzing the geometry of a molecule.
"""
import os  
import numpy
import argparse

def calc_distance(coord1, coord2):
    """
    Calculates distance between 2 vectors
    Inputs: 2 sets of coordinates
    Return: Distance between two points
    """
    x_dist = coord1[0] - coord2[0]
    y_dist = coord1[1] - coord2[1]
    z_dist = coord1[2] - coord2[2]
    dist = numpy.sqrt((x_dist)**2 + (y_dist)**2 + (z_dist)**2)
    return dist

def bond_check(distance, min_dist = 0, max_dist = 1.5):
    #documentation for help
    """
    Check if a distance is a bond based on a minimum and maximum length.
    Inputs: distance, min_length, max_length
    Defaults: min_length = 0, max_length = 1.5
    Return: True or False
    """
    if distance > min_dist and distance <= max_dist:
        return True
    else:
        return False

#to be able to import it as a library later
if __name__ == "__main__":
    
    #Using argparse to handle arguments 
    parser = argparse.ArgumentParser(description = "This script analyzes a user provided xyz file and outputs all the bonds.")
    parser.add_argument("xyz_file", help = "The filepath for the xyz file to analyze")
    args = parser.parse_args()

    file_location = args.xyz_file
    xyz_file = numpy.genfromtxt(fname = file_location, dtype = 'unicode', skip_header = 2)

    atoms = xyz_file[:, 0]
    coord = xyz_file[:, 1:].astype(numpy.float)

    for atom1 in range(len(atoms)):
        for atom2 in range(len(atoms)):
            if atom1 < atom2:
                dist = calc_distance(coord[atom1], coord[atom2])
                if bond_check(dist) == True:
                    print(F'{atoms[atom1]} to {atoms[atom2]}: {dist:.3f}')