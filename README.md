# MWViewer

Some tools for visualizing [Krawtchouk matrices](https://en.wikipedia.org/wiki/Krawtchouk_matrices) (or MacWilliams matrices).

## Brief information
The `manimvideo` folder consists of a script written in Python with the Manim Community library (repo [here](https://github.com/ManimCommunity/manim)). This code was created for a manim-slides [presentation](https://github.com/supxinfy/Diplom-slides). The `macwilliams.py` module uses an algorithm referred to as "Gogin's algorithm". Details about that algorithm can be found in this [article](https://www.researchgate.net/publication/31597175_Recurrent_Construction_of_MacWilliams_and_Chebyshev_Matrices). `consts.toml` contains constants. Modify this file to change the order or a module.

The `ffmpeg` folder consists of scripts I used during the conference talk on PCA2023, where I, in conjunction with Nikita Gogin, presented [this](https://pca-pdmi.ru/2023/files/17/Gogin-Shubin-2023.pdf) paper. These scripts are similar but use [SageMath](https://www.sagemath.org) to generate a video. Run `makevideo.py` to learn how to use it. 

<div align="center">
  <video width="600" height="600" controls>
    <source src="manimvideo/example/MacWilliams.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>
To experiment with these tools, you need to know how to run Manim or have SageMath installed.