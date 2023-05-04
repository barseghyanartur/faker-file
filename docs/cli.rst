CLI
===
It's possible to generate files from CLI.

.. note::

    For using CLI you should install all common dependencies:

.. code-block:: sh

    pip install faker-file[common]

List available provider options
-------------------------------
.. code-block:: sh

    faker-file --help

Output:

.. code-block:: text

    usage: faker-file [-h] [-o OUTPUT_DIR]
                      {bin_file,csv_file,docx_file,eml_file,epub_file,ico_file,jpeg_file,mp3_file,odp_file,ods_file,odt_file,pdf_file,png_file,pptx_file,rtf_file,svg_file,tar_file,txt_file,webp_file,xlsx_file,zip_file}
                      ...

    CLI for the faker-file package.

    positional arguments:
      {bin_file,csv_file,docx_file,eml_file,epub_file,ico_file,jpeg_file,mp3_file,odp_file,ods_file,odt_file,pdf_file,png_file,pptx_file,rtf_file,svg_file,tar_file,txt_file,webp_file,xlsx_file,zip_file}
                            Available file providers.
        bin_file            Generate a bin file.
        csv_file            Generate a csv file.
        docx_file           Generate a docx file.
        eml_file            Generate a eml file.
        epub_file           Generate a epub file.
        ico_file            Generate a ico file.
        jpeg_file           Generate a jpeg file.
        mp3_file            Generate a mp3 file.
        odp_file            Generate a odp file.
        ods_file            Generate a ods file.
        odt_file            Generate a odt file.
        pdf_file            Generate a pdf file.
        png_file            Generate a png file.
        pptx_file           Generate a pptx file.
        rtf_file            Generate a rtf file.
        svg_file            Generate a svg file.
        tar_file            Generate a tar file.
        txt_file            Generate a txt file.
        webp_file           Generate a webp file.
        xlsx_file           Generate a xlsx file.
        zip_file            Generate a zip file.

    options:
      -h, --help            show this help message and exit

List options for a certain provider
-----------------------------------
.. code-block:: sh

    faker-file docx_file --help

Output:

.. code-block:: text

    usage: faker-file docx_file [-h] [--prefix PREFIX] [--max_nb_chars MAX_NB_CHARS] [--wrap_chars_after WRAP_CHARS_AFTER] [--content CONTENT] [--nb_files NB_FILES]

    options:
      -h, --help            show this help message and exit
      --prefix PREFIX       prefix (default: None)
      --max_nb_chars MAX_NB_CHARS
                            max_nb_chars (default: 10000)
      --wrap_chars_after WRAP_CHARS_AFTER
                            wrap_chars_after (default: None)
      --content CONTENT     content (default: None)
      --nb_files NB_FILES   number of files to generate (default: 1)

Generate a file using certain provider
--------------------------------------
.. code-block:: sh

    faker-file docx_file

Output:

.. code-block:: text

    Generated docx_file file: tmp/tmpva0mp3lp.docx

Shell auto-completion
---------------------
First, generate shell auto-completion file.

.. code-block:: sh

    faker-file generate-completion

Then, source the generated file:

.. code-block:: sh

    source ~/faker_file_completion.sh

Now you can use auto-completion. Simply type faker-file [tab-tab] to see the
list of available options:

.. code-block:: sh

    $ faker-file
    bin_file   eml_file   jpeg_file  ods_file   png_file   svg_file   webp_file
    csv_file   epub_file  mp3_file   odt_file   pptx_file  tar_file   xlsx_file
    docx_file  ico_file   odp_file   pdf_file   rtf_file   txt_file   zip_file

It works with sub options too:

.. code-block:: sh

    $ faker-file docx_file --
    --content    --max_nb_chars    --prefix    --wrap_chars_after    --nb_files

To update the completion script, simply run the ``generate-completion`` command
again and source the ``~/faker_file_completion.sh`` as already shown above.
