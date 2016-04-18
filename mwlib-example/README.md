# Wikipedia Book Building with mwlib

# Setup

[mwlib documentation is here](http://mwlib.readthedocs.org/en/latest/basics.html)

Follow [instructions for installation here](http://mwlib.readthedocs.org/en/latest/installation.html)

Note, this seems likely to only work on Ubuntu. [Virtualbox](https://www.virtualbox.org/wiki/Downloads) or [Docker](https://www.docker.com/) is recommended for running locally.

Important: If installing Pillow instead of PIL, a pre 3.0.0 version is required. e.g.:

`pip install 'Pillow<3.0.0'`

## Using mwlib

[mwlib](https://pypi.python.org/pypi/mwlib) and [mwlib.rl](https://pypi.python.org/pypi/mwlib.rl) are available from pypi, however I have found the code pretty difficult to use as a library. I have included instead an example of using the mwlib command-line tools from Python via subprocesses. This is far from ideal, but currently seems to be the most straightforward approach to interfacing with mwlib.

Building a book is a two-step process: extracting Wikipedia content into a zip file (via mwlib proper) and rendering the zip contents into a pdf (via mwlib.rl). `rl` in this context refers to reportlab, the library that is used to render the pdf files.

The example file `buildbook.py` executes both steps to build a book from the included "metabook" json file.

Note: the metabook json file must be proper JSON syntax -- not Python dictionary syntax.
