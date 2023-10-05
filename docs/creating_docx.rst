Creating DOCX
=============

See the following full functional snippet for generating DOCX.

.. literalinclude:: _static/examples/creating_docx/docx_1.py
    :language: python

*See the full example*
:download:`here <_static/examples/creating_docx/docx_1.py>`

The generated DOCX will have 10,000 characters of text, which is about 5 pages.

If you want DOCX with more pages, you could either:

- Increase the value of ``max_nb_chars`` accordingly.
- Set value of ``wrap_chars_after`` to 80 characters to force longer pages.
- Insert manual page breaks and other content.

----

See the example below for ``max_nb_chars`` tweak:

.. literalinclude:: _static/examples/creating_docx/docx_2.py
    :language: python
    :lines: 8-

*See the full example*
:download:`here <_static/examples/creating_docx/docx_2.py>`

----

See the example below for ``wrap_chars_after`` tweak:

.. literalinclude:: _static/examples/creating_docx/docx_3.py
    :language: python
    :lines: 8-

*See the full example*
:download:`here <_static/examples/creating_docx/docx_3.py>`

----

As mentioned above, it's possible to diversify the generated context with
images, paragraphs, tables, manual text break and pretty much everything that
is supported by DOCX format specification, although currently only images,
paragraphs, tables and manual text breaks are supported out of the box. In
order to customise the blocks DOCX file is built from, the ``DynamicTemplate``
class is used. See the example below for usage examples:

.. literalinclude:: _static/examples/creating_docx/docx_4.py
    :language: python
    :lines: 3-9, 14-

*See the full example*
:download:`here <_static/examples/creating_docx/docx_4.py>`
