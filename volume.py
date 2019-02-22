# volume.py
#
# Use a simple user defined function to calculate the volume of a block with a hole drilled in it
#
# Muhammad Nauman
# UIN: 927008027
# 10/29/2018
# ENGR 102-213
#
# Lab 10b - 1

import math


def vol(l, w, h, r):
    """
    Compute the volume of a block with a hole drilled in the middle

    Parameters
    ----------
    l, w, h: float, int
        The length, width and height of the block, respectively
    r: float, int
        Radius of the hole to be drilled

    Returns
    -------
    v: float, int
        volume of a block with length l , width w and height h with a hole of radius r drilled in the middle
    fit: boolean
        Returns true or false depending on if the hole will fit in the cube
    """
    fit = True
    if 2*r > l or 2*r > w:
        fit = False
    v_cube = l*w*h
    v_hole = math.pi * r**2 * h
    v_block = v_cube - v_hole
    n = 3
    return (v_block, fit)


if __name__ == '__main__':
    ans = vol(10., 20., 3., 4.)
    print(ans)

    l, w, h, r = 4, 5, 7, 5
    ans, flag = vol(l, w, h, r)
    print(ans, flag)