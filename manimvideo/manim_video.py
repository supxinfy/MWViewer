from manim import *

import macwilliams as mw

import tomllib as toml

with open("consts.toml", "rb") as f:
    const = toml.load(f)

size = const['size']
units = const['units']

maxorder = const['max-order']
modulo = const['modulo']

config.pixel_height = size
config.pixel_width = size

config.frame_height = units
config.frame_width = units

class MacWilliams(Scene):
    def construct(self):
        mws = [ImageMobject(mw.MWplot(i, modulo)) for i in range(2, maxorder+1)]
        for i, img in enumerate(mws):
            img.height = (units >> 1) * (1 + i/maxorder) # The first image is half-way through the whole screen, and the last is almost the whole screen
            img.set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        print(mws)
        for img in mws:
            self.add(img)
            self.play(FadeIn(img, run_time = modulo/maxorder)) # in seconds

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )