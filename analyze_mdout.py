import os
import argparse

#Tell argparse to handle arguments
parser = argparse.ArgumentParser(description = "This script parses amber mdout files to extract the total energy.")

#Tell argparse what args to expect
parser.add_argument("path", help = "The filepath to the file to be analyzed.")

#Get arguments from user
args = parser.parse_args()

filename = args.path

f = open(filename, 'r')
data = f.readlines()
f.close()

base_filename = filename.split('.')
output_filename = f'{base_filename[0]}_Etot.txt'

f_write = open(output_filename, 'w+')
print(f'Writing to {output_filename}')
f_write.write('Total Energy\n')

etot = []
for line in data:
    if 'Etot' in line:
        words = line.split()
        etot.append(words[2])
        
etot = etot[:-2]

for energy in etot:
    f_write.write(F"{energy}\n")

f_write.close() 