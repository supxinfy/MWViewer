#!/usr/bin/env sage -python

from sage.all import *
from sage.repl.image import Image

# import PIL

import sys

def diagonal_matrix(arr, n):
    m = matrix(ZZ, [1] + (n-1) * [0])
    for i in range(1, n):
        m = m.insert_row(i, [Integer(0)] * i + [Integer(arr[i])] + [Integer(0)] * (n - i - 1))
    return m

def _MW(n, p):
    mw = matrix(ZZ, [[1, 1], [1, -1]])
    for i in srange(2, n+1):
        mw = ((mw.insert_row(i, [Integer(0)]*i)).transpose().insert_row(i, [Integer(0)]*(i+1)).transpose() +\
        (mw.insert_row(0, [Integer(0)]*i)).transpose().insert_row(i, [Integer(0)]*(i+1)).transpose() +\
        (mw.insert_row(i, [Integer(0)]*i)).transpose().insert_row(0, [Integer(0)]*(i+1)).transpose() -\
        (mw.insert_row(0, [Integer(0)]*i)).transpose().insert_row(0, [Integer(0)]*(i+1)).transpose())
        mw = mw * diagonal_matrix([1] + ([round((p+1)/2)]*(i-1)) + [1], i+1)
        matrix_plot(matrix(IntegerModRing(p), mw), cmap='magma').save(f'{i}.png', dpi=250)
    return matrix(IntegerModRing(p), (mw * diagonal_matrix([1] + ([round((p+1)/2)]*(n-1)) + [1], n+1)))

def hu(x):
    return 0.77 if 0 <= x < 0.5 else 0.414

def br(x):
    return 5 * x + 0.5 if 0 <= x < 0.1 else -5 * x + 5.5 if 0.9 < x <= 1 else 1

def CreateVisual(n, p):

    mw = matrix(ZZ, [[1, 1], [1, -1]])
    for i in range(2, n+1):
        mw = ((mw.insert_row(i, [Integer(0)]*i)).transpose().insert_row(i, [Integer(0)]*(i+1)).transpose() +\
        (mw.insert_row(0, [Integer(0)]*i)).transpose().insert_row(i, [Integer(0)]*(i+1)).transpose() +\
        (mw.insert_row(i, [Integer(0)]*i)).transpose().insert_row(0, [Integer(0)]*(i+1)).transpose() -\
        (mw.insert_row(0, [Integer(0)]*i)).transpose().insert_row(0, [Integer(0)]*(i+1)).transpose())
        mw = mw * diagonal_matrix([1] + ([round((p+1)/2)]*(i-1)) + [1], i+1)

        img = Image('RGB', (i+1, i+1))
        pixels = img.pixels()

        pixel_size = ((n - i) >> 2) + 4
        res_img = Image('RGB', (pixel_size * (i+1), pixel_size * (i+1)))
        res_pixels = res_img.pixels()

        for j in range(0, i+1):
            for k in range(0, i+1):
                H = hue(hu(int(mod(mw[j, k], p))/p) * (1 - int(mod(mw[j, k], p))/p), 1, br(int(mod(mw[j, k], p))/p))
                pixels[j, k] = (int(round(255*H[0])), int(round(255*H[1])), int(round(255*H[2])))
                for x in range(pixel_size):
                    for y in range(pixel_size):
                        res_pixels[j * pixel_size + x, k * pixel_size + y] = pixels[j, k]

        res_img.save(f'.video/hue_{i}.png')
        #matrix_plot(matrix(IntegerModRing(p), mw), cmap='magma').save(f'{i}.png', dpi=250)
    return

def main(argv):
    CreateVisual(Integer(sys.argv[2]), Integer(sys.argv[3]))
if __name__ == '__main__':
    main(sys.argv)
