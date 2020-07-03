import os
file = os.path.join('data', '03_Prod.mdout')
outfile = open('Etot.txt', 'w+') #w+, makes new file if doesnt exist
file = open(file, 'r')
data = file.readlines()
file.close()
for line in data:
    if 'Etot' in line:
        etot_line = line
        words = etot_line.split()
        etot = words[2]
        outfile.write(f'{etot}\n')
outfile.close()