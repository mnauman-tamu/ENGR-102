# file_io.py
#
# Read and write data
#

# Create lists to store header and data
header = []
data = []

# Open the file data.dat and print it out
with open('data.dat', 'r') as t_d:
    for line in t_d:
        line = line.strip().split(',')
        if line[0][0] is '#':
            header_line = []
            for value in line:
                    header_line.append(value.strip('#').strip())
            header.append(header_line)
        else:
            data_line = []
            for value in line:
                data_line.append(float(value.strip()))
            data.append(data_line)

print(header)
print(data)

header_data = header
temp_data = data

with open('data.out', 'w') as output_file:

    header = []
    for i in range(2):
        line = '# ' + header_data[i][0] + ', ' + header_data[i][1] + '\n'
        header.append(line)
    print(header)
    output_file.write(''.join(header))

    data_line = []
    for i in range(len(temp_data)):
        line = str(temp_data[i][0]) + ', ' + str(temp_data[i][1]) + '\n'
        output_file.write(line)
