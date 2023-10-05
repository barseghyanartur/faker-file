Creating images
===============
.. Internal references

.. _faker-file: https://pypi.org/project/faker-file/

.. External references

.. _imgkit: https://pypi.org/project/imgkit/
.. _Pillow: https://pillow.readthedocs.io/
.. _WeasyPrint: https://pypi.org/project/weasyprint/
.. _wkhtmltopdf: https://wkhtmltopdf.org/

Creating images could be a challenging task. System dependencies on one
side, large variety of many image formats on another.

Underlying creation of image files has been delegated to an abstraction layer
of image generators. If you don't like how image files are generated or format
you need isn't supported, you can create your own layer, using your favourite
library.

Generally speaking, in `faker-file`_ each file provider represents a certain
file type (with only a few exceptions). For generating a file in PNG format
you should use `PngFileProvider`. For JPEG you would use `JpegFileProvider`.

Image providers
---------------
Currently, there are 3 types of image providers implemented:

- Graphic-only image providers.
- Mixed-content image providers.
- Image augmentation providers.

The graphic-only image providers are only capable of producing random
graphics.

The mixed-content image providers can produce an image consisting of
both text and graphics. Moreover, text comes in variety of different
headings (such as h1, h2, h3, etc), paragraphs and tables.

Image augmentation providers simply augment existing images in a various,
declaratively random, ways, such as: flip, resize, lighten, darken,
grayscale and others.

Image generators
----------------
The following image generators are available.

- ``PilImageGenerator``, built on top of the `Pillow`_. It's the generator
  that will likely won't ask for any system dependencies that you don't
  yet have installed.
- ``ImgkitImageGenerator`` (default), built on top of the `imgkit`_
  and `wkhtmltopdf`_. Extremely easy to work with. Supports many formats.
- ``WeasyPrintImageGenerator``, built on top of the `WeasyPrint`_.
  Easy to work with. Supports formats that `imgkit`_ does not.

Building mixed-content images using `imgkit`_
---------------------------------------------
While `imgkit`_ generator is heavier and has `wkhtmltopdf`_ as a system
dependency, it produces better quality images and has no issues with fonts
or unicode characters.

See the following full functional snippet for generating images using `imgkit`_.

.. literalinclude:: _static/examples/creating_images/imgkit_1.py
    :language: python

*See the full example*
:download:`here <_static/examples/creating_images/imgkit_1.py>`

The generated PNG image will have 10,000 characters of text. The generated image
will be as wide as needed to fit those 10,000 characters, but newlines are
respected.

----

If you want image to be less wide, set value of ``wrap_chars_after`` to 80
characters (or any other number that fits your needs). See the example below:

.. literalinclude:: _static/examples/creating_images/imgkit_2.py
    :language: python
    :lines: 8-

*See the full example*
:download:`here <_static/examples/creating_images/imgkit_2.py>`

----

To have a longer text, increase the value of ``max_nb_chars`` accordingly.
See the example below:

.. literalinclude:: _static/examples/creating_images/imgkit_3.py
    :language: python
    :lines: 8-

*See the full example*
:download:`here <_static/examples/creating_images/imgkit_3.py>`

----

As mentioned above, it's possible to diversify the generated context with
images, paragraphs, tables and pretty much everything that you could think of,
although currently only images, paragraphs and tables are supported out of
the box. In order to customise the blocks image file is built from,
the ``DynamicTemplate`` class is used. See the example below for usage
examples:

.. literalinclude:: _static/examples/creating_images/imgkit_4.py
    :language: python
    :lines: 2-7, 13-

*See the full example*
:download:`here <_static/examples/creating_images/imgkit_4.py>`

Building mixed-content images using `WeasyPrint`_
-------------------------------------------------
While `WeasyPrint`_ generator isn't better or faster than the `imgkit`_, it
supports formats that `imgkit`_ doesn't (and vice-versa) and therefore is a
good alternative to.

See the following snippet for generating images using `WeasyPrint`_.

.. literalinclude:: _static/examples/creating_images/weasyprint_1.py
    :language: python
    :lines: 2-4, 9-

*See the full example*
:download:`here <_static/examples/creating_images/weasyprint_1.py>`

----

All examples shown for `imgkit`_ apply for `WeasyPrint`_ generator, however
when building images files from blocks (paragraphs, images and tables), the
imports shall be adjusted:

As mentioned above, it's possible to diversify the generated context with
images, paragraphs, tables and pretty much everything else that you could
think of, although currently only images, paragraphs and tables are supported.
In order to customise the blocks image file is built from, the
``DynamicTemplate`` class is used. See the example below for usage examples:

.. literalinclude:: _static/examples/creating_images/weasyprint_2.py
    :language: python
    :lines: 3-7, 15-

*See the full example*
:download:`here <_static/examples/creating_images/weasyprint_2.py>`

Building mixed-content images using `Pillow`_
---------------------------------------------
Usage example:

.. literalinclude:: _static/examples/creating_images/pillow_1.py
    :language: python
    :lines: 2, 7-

*See the full example*
:download:`here <_static/examples/creating_images/pillow_1.py>`

----

With options:

.. literalinclude:: _static/examples/creating_images/pillow_2.py
    :language: python
    :lines: 8-

*See the full example*
:download:`here <_static/examples/creating_images/pillow_2.py>`

----

All examples shown for `imgkit`_ and `WeasyPrint`_ apply to `Pillow`_ generator,
however when building image files from blocks (paragraphs, images and tables),
the imports shall be adjusted. See the example below:

.. literalinclude:: _static/examples/creating_images/pillow_3.py
    :language: python
    :lines: 3-7, 13-

*See the full example*
:download:`here <_static/examples/creating_images/pillow_3.py>`

Creating graphics-only images using `Pillow`_
---------------------------------------------
There are so called ``graphic`` image file providers available. Produced image
files would not contain text, so don't use it when you need text based content.
However, sometimes you just need a valid image file, without caring much about
the content. That's where graphic image providers comes to rescue:

.. literalinclude:: _static/examples/creating_images/pillow_4.py
    :language: python
    :lines: 2-3, 5-

*See the full example*
:download:`here <_static/examples/creating_images/pillow_4.py>`

The generated file will contain a random graphic (consisting of lines and
shapes of different colours).

----

One of the most useful arguments supported is ``size``.

.. literalinclude:: _static/examples/creating_images/pillow_5.py
    :language: python
    :lines: 7-

*See the full example*
:download:`here <_static/examples/creating_images/pillow_5.py>`

Augment existing images
-----------------------
Augment the input image with a series of random augmentation methods.

.. literalinclude:: _static/examples/creating_images/augment_1.py
    :language: python
    :lines: 2-15, 17, 19-20, 28-

*See the full example*
:download:`here <_static/examples/creating_images/augment_1.py>`
