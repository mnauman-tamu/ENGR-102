# files.py
#
# Write user-defined functions to read and write files
#
# Muhammad Nauman
# UIN: 927008027
# 10/29/2018
# ENGR 102-213
#
# Lab 10b - 2

import numpy as np


def reader(name, header):
    """
    Reads a file

    Parameters
    ----------
    name: string
        The name of the file with .csv extension
    header: string, list, int
        Character that designates a header line as input or the number of lines of the header

    Returns
    -------
    header_info: string, list
        The header information
    data: np.array
        The data in the file
    """

    header_info = []
    data = []

    with open(name, 'r') as t_d:
        for line in t_d:
            # data_line = line.split(',')
            data.append(line)

        if type(header) == str:
            header_info = header
        elif type(header) == list:
            header_info = header
        elif type(header) == int:
            for i in range(header):
                header_info.append(data[0])
                del data[0]
        else:
            return "Error: wrong header type"

        data = np.array(data)

    return(header_info, data)


def writer(header, data, name):
    """
    Writes a file

    Parameters
    ----------
    header: string, list
        The header information
    data: np.array
        The data of the file
    name: string
        The name of the file with .csv extension

    Returns
    -------
    *** Returns nothing but writes a .csv file with the given name ***
    """

    with open(name, 'w') as t_d:
        for j in header:
            for i in j:
                t_d.write(i)
        for i in data:
            t_d.write(str(i))


if __name__ == "__main__":
    ans = reader("WeatherDataWindows.csv", 1)
    print(ans)

    ans = writer(ans[0], ans[1], "Test.csv")
