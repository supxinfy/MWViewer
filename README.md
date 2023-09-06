# MWViewer
Some tools for visualizing [Krawtchouk matrices](https://en.wikipedia.org/wiki/Krawtchouk_matrices) (or MacWilliams matrices)

## Brief information

The `manimvideo` folder consists of a script written in Python with the Manim Community library (repo [here](https://github.com/ManimCommunity/manim)). This is the code I've made for a manim-slides [presentation](https://github.com/supxinfy/Diplom-slides). Module `macwilliams.py` uses some algorithm that I would call "Gogin's algorithm". Details about that algorithm can be found in this [article](https://www.researchgate.net/publication/31597175_Recurrent_Construction_of_MacWilliams_and_Chebyshev_Matrices).

`consts.toml` is a file for constants. If you want to change an order or a module, change the file.

An example of the rendered video is right here.
![or not](manimvideo/example/MacWilliams.mp4)
<div align="center">
<video width="600" height="600" controls>
  <source src="manimvideo/example/MacWilliams.mp4" type="video/mp4">
</video>
</div>
If you want to play with it a little bit, you need to know how to run Manim.