# Inkscape2Fritzing

A small utility to set IDs of SVG image layers created in Inkscape
based on its label in order to be easily usable in Fritzing.

## Introduction

If for some strange reason have you ever tried to use SVG files created  
in Inkscape to define custom PCBs or parts in Fritzing you probably  
have been noticed with the error:

```
There are no copper layers defined in path/to/your/file.svg. See this explanation.

This will not be a problem in the next release of the Parts Editor, but  
for now please modify the file according the instructions in the link.
```

You probably setup properly your layers including `copper` and `silkscreen`
words as layer name but still, nothing is working. The error is produced
due to that Inkscape does not set id attribute of a layer and Fritzing
uses this attribute to classify properly a layer.

## Usage

Of course you can set up the attributes manually in any text editor but
also you can clone this repo and just type something similar to:

    python3 ink2fritz.py -i path/to/your/file.svg -o path/to/out/file.svg

## License

Copyright © 2020 by BikePixels.com and contributors:

Krzysztof Stopa (kstopa).
Inkscape2Fritzing contains free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or any
later version.

Inkscape2Fritzing is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with CAMS tools. If not, see http://www.gnu.org/licenses/.