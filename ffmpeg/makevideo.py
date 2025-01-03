#!/usr/bin/env python3

import os, glob, time
import sys

from multiprocessing import Process

def save(n, name):
    while len(glob.glob(".video/*.png")) < n:
        print(round(100 * len(glob.glob(".video/*.png"))/(n-1)), "%")
        time.sleep(1)
        if len(glob.glob(".video/*.png")) >= n-1:
            return

def makeMWs(n0, n1, p):
    os.system(f"./mws.py {n0} {n1} {p}")

def main(argv):
    if len(argv) != 5:
        print("Usage: python3 makevideo.py n0 n1 p output.")
        print("Use -h or --help for more information...")
        return
    
    if argv[1] == '-h' or argv[1] == '--help':
        print("Usage: python3 makevideo.py <n0> <n1> <p> <file>")
        print("This script generates a video of the sequence of Krawtchouk matrices modulo prime. The output is saved in the file <file>.mp4")
        print("n0: initial order of the matrix")
        print("n1: final order of the matrix")
        print("p: prime modulo")
        print("file: output file name")
        return

    if not os.path.exists('.video/'):
        os.makedirs('.video/')
    else:
        assert False, "Careful! We need to create folder '.video' but it exists already!"
    p1 = Process(target = makeMWs, args=(sys.argv[1], sys.argv[2], sys.argv[3]))
    p2 = Process(target = save, args=(int(sys.argv[2]), sys.argv[4]))
    p2.start()
    p1.start()

    p1.join()
    p2.join()
    
    print("Please wait while we create the video...")
    os.system("sips -Z 320 .video/hue_*.png")
    #os.system(f"ffmpeg -r 1 -i %01d.png -vcodec mpeg4 -y {sys.argv[4]}.mp4")
    os.system(f"ffmpeg -r 1 -i .video/hue_%01d.png -qscale:v 0 -vcodec mpeg4 -y {sys.argv[4]}.mp4")

    if os.path.exists('.video/'):
        os.system("rm -rf .video")
    else:
        assert False, "We tried to delete .video folder, but it's not there!"

    os.system(f"open {sys.argv[4]}.mp4")
if __name__ == '__main__':
    main(sys.argv)
