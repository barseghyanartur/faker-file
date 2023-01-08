============================
Custom MP3 generator example
============================
Generate MP3 file from random text using custom MP3 generator based on
``MaryTts``.

Prerequisites
=============
Install ``speak2mary`` (``Apache 2``) and ``ffmpeg-python``
(``Apache 2``):

.. code-block:: shell

    pip install speak2mary ffmpeg-python

Run ``marytts`` in docker:

https://github.com/synesthesiam/docker-marytts

.. code-block:: shell

    docker run -it -p 59125:59125 synesthesiam/marytts:5.2

Usage example
=============
Generate MP3 from random text using custom MP3 generator:

.. code-block:: python

    import os
    import sys
    sys.path.insert(
        0, os.path.abspath(os.path.join("examples", "customizations"))
    )

    from faker import Faker
    from faker_file.providers.mp3_file import Mp3FileProvider
    from marytts_mp3_generator import MaryTtsMp3Generator

    FAKER = Faker()

    file = Mp3FileProvider(FAKER).mp3_file(
        mp3_generator_cls=MaryTtsMp3Generator,
        mp3_generator_kwargs={},
    )
