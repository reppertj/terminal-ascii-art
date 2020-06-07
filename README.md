# Terminal ASCII Art
> Turn images into ASCII art.

I created this in a weekend attempt to learn some Python beyond the statistical uses I'm familiar with, as one of [Robert Heaton's Programming Projects for Advanced Beginners](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/). This probably doesn't follow good practices in all sorts of ways, because I'm still learning what those are.

![](header.png)

## Usage

### Capture image from a connected video source

Webcam usage requires [ImageSnap](http://iharder.sourceforge.net/current/macosx/imagesnap/) (```$ brew install imagesnap```) and uses the first camera (```$ imagesnap -l```) if multiple are installed. The webcam image will be saved as snapshot.jpg.

### After you clone the project:

1. Run the requirements.txt: ```$ pip install -r requirements.txt```
2. Run asciiart.py: ```$ python asciiart.py -f 'sample.jpg'```

You may need to change your font size to see the whole output, or try changing the width with ```-w [WIDTH]```.

The following options are supported:
* ```-f [filename]```: Path to image file to process; omit to use webcam.
* ```-c```: Render in 256-bit color against black background if your environment supports it
* ```-m```: Method for calculating pixel density. (Default='lightness')
    * ```'mean'```: Average of pixel red, green, and blue values
    * ```'lightness'```: Average of minimum and maximum of red, green, and blue values
    * ```'luminosity'```: Weighted average of red, green, and blue values (0.21R + .72G + .07B) to account for human perception
* ```-w [WIDTH]```: Width of ASCII image before applying width scalar (see below). (Default=80)
* ```-s [SCALE]```: Width scalar of 1, 2, or 3 to compensate for the fact that characters are taller than they are wide. Doubles or triples each character printed to the terminal. (Default=2)

---

Justin Reppert

Script was written on Python 3.7.4

Distributed under the MIT license. See ``LICENSE`` for more information.