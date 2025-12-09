Project source-tree
===================

Below is the layout of our project (to 10 levels), followed by
the contents of each key file.

.. code-block:: bash
   :caption: Project directory layout

   faker-file/

   ├── docs
   │   ├── _static
   │   │   └── examples
   │   │       ├── creating_docx
   │   │       │   ├── docx_1.py
   │   │       │   ├── docx_2.py
   │   │       │   ├── docx_3.py
   │   │       │   └── docx_4.py
   │   │       ├── creating_images
   │   │       │   ├── augment_1.py
   │   │       │   ├── imgkit_1.py
   │   │       │   ├── imgkit_2.py
   │   │       │   ├── imgkit_3.py
   │   │       │   ├── imgkit_4.py
   │   │       │   ├── pillow_1.py
   │   │       │   ├── pillow_2.py
   │   │       │   ├── pillow_3.py
   │   │       │   ├── pillow_4.py
   │   │       │   ├── pillow_5.py
   │   │       │   ├── weasyprint_1.py
   │   │       │   └── weasyprint_2.py
   │   │       ├── creating_odt
   │   │       │   ├── odt_1.py
   │   │       │   ├── odt_2.py
   │   │       │   ├── odt_3.py
   │   │       │   └── odt_4.py
   │   │       ├── creating_pdf
   │   │       │   ├── pdfkit_1.py
   │   │       │   ├── pdfkit_2.py
   │   │       │   ├── pdfkit_3.py
   │   │       │   ├── pdfkit_4.py
   │   │       │   ├── pillow_1.py
   │   │       │   ├── pillow_2.py
   │   │       │   ├── pillow_3.py
   │   │       │   ├── pillow_4.py
   │   │       │   ├── pillow_5.py
   │   │       │   ├── reportlab_1.py
   │   │       │   └── reportlab_2.py
   │   │       ├── methodology
   │   │       │   ├── clean_up_files_1.py
   │   │       │   ├── clean_up_files_2.py
   │   │       │   ├── clean_up_files_3.py
   │   │       │   ├── create_docx_file_1.py
   │   │       │   ├── create_docx_file_2.py
   │   │       │   ├── create_docx_file_3.py
   │   │       │   ├── file_from_path_provider.py
   │   │       │   └── rand_file_from_dir_provider.py
   │   │       ├── quick_start
   │   │       │   ├── factory_import_and_init_1.py
   │   │       │   ├── factory_models_1.py
   │   │       │   └── import_and_init_1.py
   │   │       └── recipes
   │   │           ├── augment_file_from_dir_1.py
   │   │           ├── augment_file_from_dir_2.py
   │   │           ├── augment_file_from_dir_3.py
   │   │           ├── augment_file_from_dir_4.py
   │   │           ├── aws_s3_storage_1.py
   │   │           ├── aws_s3_storage_2.py
   │   │           ├── aws_s3_storage_3.py
   │   │           ├── aws_s3_storage_4.py
   │   │           ├── docx_file_1.py
   │   │           ├── docx_file_mixed_1.py
   │   │           ├── eml_file_1.py
   │   │           ├── eml_file_2.py
   │   │           ├── eml_file_3.py
   │   │           ├── eml_file_4.py
   │   │           ├── eml_file_5.py
   │   │           ├── factory_boy_factory_1.py
   │   │           ├── factory_boy_factory_2.py
   │   │           ├── factory_boy_factory_3.py
   │   │           ├── factory_boy_models_1.py
   │   │           ├── file_from_path_1.py
   │   │           ├── file_of_size_bin_1.py
   │   │           ├── file_of_size_txt_1.py
   │   │           ├── files_multiprocessing_1.py
   │   │           ├── files_multiprocessing_2.py
   │   │           ├── flexible_storage_1.py
   │   │           ├── generic_file_1.py
   │   │           ├── google_cloud_storage_1.py
   │   │           ├── google_cloud_storage_2.py
   │   │           ├── graphic_ico_file_1.py
   │   │           ├── graphic_jpeg_file_1.py
   │   │           ├── graphic_png_file_1.py
   │   │           ├── graphic_webp_file_1.py
   │   │           ├── imports_and_init_1.py
   │   │           ├── imports_and_init_2.py
   │   │           ├── mp3_file_1.py
   │   │           ├── mp3_file_custom_1.py
   │   │           ├── mp3_file_edge_tts_1.py
   │   │           ├── mp3_file_edge_tts_2.py
   │   │           ├── mp3_file_gtts_1.py
   │   │           ├── mp3_file_gtts_2.py
   │   │           ├── odt_file_mixed_1.py
   │   │           ├── pdf_file_1.py
   │   │           ├── pdf_file_pdfkit_1.py
   │   │           ├── pdf_file_pillow_1.py
   │   │           ├── pdf_file_pillow_2.py
   │   │           ├── pdf_file_reportlab_1.py
   │   │           ├── random_file_from_dir_1.py
   │   │           ├── raw_1.py
   │   │           ├── sftp_storage_1.py
   │   │           ├── txt_file_1.py
   │   │           ├── zip_file_1.py
   │   │           ├── zip_file_2.py
   │   │           ├── zip_file_3.py
   │   │           ├── zip_file_4.py
   │   │           ├── zip_file_5.py
   │   │           └── zip_file_6.py
   │   ├── talks
   │   │   └── pygrunn_2023.rst
   │   ├── changelog.rst
   │   ├── cli.rst
   │   ├── code_of_conduct.rst
   │   ├── concepts.rst
   │   ├── conf.py
   │   ├── conf.py.distrib
   │   ├── conftest.py
   │   ├── contributor_guidelines.rst
   │   ├── creating_docx.rst
   │   ├── creating_images.rst
   │   ├── creating_odt.rst
   │   ├── creating_pdf.rst
   │   ├── documentation.rst
   │   ├── faker_file.cli.rst
   │   ├── faker_file.contrib.pdf_file.rst
   │   ├── faker_file.contrib.rst
   │   ├── faker_file.providers.augment_file_from_dir.augmenters.rst
   │   ├── faker_file.providers.augment_file_from_dir.extractors.rst
   │   ├── faker_file.providers.augment_file_from_dir.rst
   │   ├── faker_file.providers.base.rst
   │   ├── faker_file.providers.helpers.rst
   │   ├── faker_file.providers.image.rst
   │   ├── faker_file.providers.mixins.rst
   │   ├── faker_file.providers.mp3_file.generators.rst
   │   ├── faker_file.providers.mp3_file.rst
   │   ├── faker_file.providers.pdf_file.generators.rst
   │   ├── faker_file.providers.pdf_file.rst
   │   ├── faker_file.providers.rst
   │   ├── faker_file.rst
   │   ├── faker_file.storages.rst
   │   ├── faker_file.tests.rst
   │   ├── index.rst
   │   ├── index.rst.distrib
   │   ├── llms.rst
   │   ├── make.bat
   │   ├── Makefile
   │   ├── marytts.py
   │   ├── methodology.rst
   │   ├── package.rst
   │   ├── quick_start.rst
   │   ├── readme.rst
   │   ├── recipes.rst
   │   ├── security.rst
   │   ├── source_tree.rst
   │   └── test_docs.py
   ├── examples
   │   ├── customizations
   │   │   ├── marytts_mp3_generator
   │   │   │   ├── __init__.py
   │   │   │   └── README.rst
   │   │   └── __init__.py
   │   ├── django_example
   │   │   ├── factories
   │   │   │   ├── __init__.py
   │   │   │   ├── auth_user.py
   │   │   │   └── upload_upload.py
   │   │   ├── project
   │   │   │   ├── settings
   │   │   │   │   ├── __init__.py
   │   │   │   │   ├── base.py
   │   │   │   │   ├── core.py
   │   │   │   │   ├── dev.py
   │   │   │   │   ├── docs.py
   │   │   │   │   ├── local_settings.example
   │   │   │   │   └── testing.py
   │   │   │   ├── __init__.py
   │   │   │   ├── urls.py
   │   │   │   └── wsgi.py
   │   │   ├── upload
   │   │   │   ├── api
   │   │   │   │   ├── __init__.py
   │   │   │   │   ├── serializers.py
   │   │   │   │   ├── tests.py
   │   │   │   │   ├── urls.py
   │   │   │   │   └── views.py
   │   │   │   ├── migrations
   │   │   │   │   ├── 0001_initial.py
   │   │   │   │   └── __init__.py
   │   │   │   ├── __init__.py
   │   │   │   ├── admin.py
   │   │   │   └── models.py
   │   │   ├── __init__.py
   │   │   ├── manage.py
   │   │   └── README.rst
   │   ├── requirements
   │   │   ├── common.in
   │   │   ├── common.txt
   │   │   ├── debug.in
   │   │   ├── debug.txt
   │   │   ├── deployment.in
   │   │   ├── deployment.txt
   │   │   ├── dev.in
   │   │   ├── dev.txt
   │   │   ├── django_4_2.in
   │   │   ├── django_4_2.txt
   │   │   ├── django_4_2_and_flask.in
   │   │   ├── django_4_2_and_flask.txt
   │   │   ├── django_5_0.in
   │   │   ├── django_5_0.txt
   │   │   ├── django_5_0_and_flask.in
   │   │   ├── django_5_0_and_flask.txt
   │   │   ├── django_5_1.in
   │   │   ├── django_5_1.txt
   │   │   ├── django_5_1_and_flask.in
   │   │   ├── django_5_1_and_flask.txt
   │   │   ├── docs.in
   │   │   ├── docs.txt
   │   │   ├── flask.in
   │   │   ├── flask.txt
   │   │   ├── ml.in
   │   │   ├── ml.txt
   │   │   ├── style_checkers.in
   │   │   ├── style_checkers.txt
   │   │   ├── test.in
   │   │   ├── test.txt
   │   │   ├── testing.in
   │   │   └── testing.txt
   │   ├── sqlalchemy_example
   │   │   ├── faker_file_admin
   │   │   │   ├── alembic
   │   │   │   │   ├── versions
   │   │   │   │   │   ├── 2695cb77cdf2_create_product_table.py
   │   │   │   │   │   └── __init__.py
   │   │   │   │   ├── __init__.py
   │   │   │   │   ├── env.py
   │   │   │   │   ├── README
   │   │   │   │   └── script.py.mako
   │   │   │   ├── static
   │   │   │   │   └── favicon.ico
   │   │   │   ├── templates
   │   │   │   │   ├── admin
   │   │   │   │   │   └── index.html
   │   │   │   │   └── tree_list.html
   │   │   │   ├── __init__.py
   │   │   │   ├── alembic.ini
   │   │   │   ├── config.py
   │   │   │   ├── config_test.py
   │   │   │   ├── data.py
   │   │   │   ├── main.py
   │   │   │   └── models.py
   │   │   ├── sqlalchemy_factories
   │   │   │   ├── __init__.py
   │   │   │   └── faker_file_admin_upload.py
   │   │   ├── README.rst
   │   │   └── run_server.py
   │   └── __init__.py
   ├── scripts
   │   └── generate_project_source_tree.py
   ├── src
   │   ├── faker_file
   │   │   ├── cli
   │   │   │   ├── __init__.py
   │   │   │   ├── command.py
   │   │   │   └── helpers.py
   │   │   ├── contrib
   │   │   │   ├── image
   │   │   │   │   ├── __init__.py
   │   │   │   │   ├── imgkit_snippets.py
   │   │   │   │   ├── pil_snippets.py
   │   │   │   │   └── weasyprint_snippets.py
   │   │   │   ├── pdf_file
   │   │   │   │   ├── __init__.py
   │   │   │   │   ├── pdfkit_snippets.py
   │   │   │   │   ├── pil_snippets.py
   │   │   │   │   └── reportlab_snippets.py
   │   │   │   ├── __init__.py
   │   │   │   ├── docx_file.py
   │   │   │   └── odt_file.py
   │   │   ├── providers
   │   │   │   ├── augment_file_from_dir
   │   │   │   │   ├── augmenters
   │   │   │   │   │   ├── __init__.py
   │   │   │   │   │   ├── nlpaug_augmenter.py
   │   │   │   │   │   └── textaugment_augmenter.py
   │   │   │   │   ├── extractors
   │   │   │   │   │   ├── __init__.py
   │   │   │   │   │   └── tika_extractor.py
   │   │   │   │   └── __init__.py
   │   │   │   ├── base
   │   │   │   │   ├── __init__.py
   │   │   │   │   ├── image_generator.py
   │   │   │   │   ├── mp3_generator.py
   │   │   │   │   ├── pdf_generator.py
   │   │   │   │   ├── text_augmenter.py
   │   │   │   │   └── text_extractor.py
   │   │   │   ├── helpers
   │   │   │   │   ├── __init__.py
   │   │   │   │   └── inner.py
   │   │   │   ├── image
   │   │   │   │   ├── __init__.py
   │   │   │   │   ├── augment.py
   │   │   │   │   ├── imgkit_generator.py
   │   │   │   │   ├── pil_generator.py
   │   │   │   │   └── weasyprint_generator.py
   │   │   │   ├── mixins
   │   │   │   │   ├── __init__.py
   │   │   │   │   ├── graphic_image_mixin.py
   │   │   │   │   ├── image_mixin.py
   │   │   │   │   └── tablular_data_mixin.py
   │   │   │   ├── mp3_file
   │   │   │   │   ├── generators
   │   │   │   │   │   ├── __init__.py
   │   │   │   │   │   ├── edge_tts_generator.py
   │   │   │   │   │   └── gtts_generator.py
   │   │   │   │   └── __init__.py
   │   │   │   ├── pdf_file
   │   │   │   │   ├── generators
   │   │   │   │   │   ├── __init__.py
   │   │   │   │   │   ├── pdfkit_generator.py
   │   │   │   │   │   ├── pil_generator.py
   │   │   │   │   │   └── reportlab_generator.py
   │   │   │   │   └── __init__.py
   │   │   │   ├── __init__.py
   │   │   │   ├── augment_image_from_path.py
   │   │   │   ├── augment_random_image_from_dir.py
   │   │   │   ├── bin_file.py
   │   │   │   ├── bmp_file.py
   │   │   │   ├── csv_file.py
   │   │   │   ├── docx_file.py
   │   │   │   ├── eml_file.py
   │   │   │   ├── epub_file.py
   │   │   │   ├── file_from_path.py
   │   │   │   ├── file_from_url.py
   │   │   │   ├── generic_file.py
   │   │   │   ├── gif_file.py
   │   │   │   ├── ico_file.py
   │   │   │   ├── jpeg_file.py
   │   │   │   ├── json_file.py
   │   │   │   ├── odp_file.py
   │   │   │   ├── ods_file.py
   │   │   │   ├── odt_file.py
   │   │   │   ├── png_file.py
   │   │   │   ├── pptx_file.py
   │   │   │   ├── random_file_from_dir.py
   │   │   │   ├── rtf_file.py
   │   │   │   ├── svg_file.py
   │   │   │   ├── tar_file.py
   │   │   │   ├── tiff_file.py
   │   │   │   ├── txt_file.py
   │   │   │   ├── webp_file.py
   │   │   │   ├── xlsx_file.py
   │   │   │   ├── xml_file.py
   │   │   │   └── zip_file.py
   │   │   ├── storages
   │   │   │   ├── pathy_based
   │   │   │   │   ├── __init__.py
   │   │   │   │   ├── aws_s3.py
   │   │   │   │   ├── azure_cloud_storage.py
   │   │   │   │   ├── cloud.py
   │   │   │   │   ├── google_cloud_storage.py
   │   │   │   │   └── helpers.py
   │   │   │   ├── __init__.py
   │   │   │   ├── aws_s3.py
   │   │   │   ├── azure_cloud_storage.py
   │   │   │   ├── base.py
   │   │   │   ├── cloud.py
   │   │   │   ├── filesystem.py
   │   │   │   ├── google_cloud_storage.py
   │   │   │   └── sftp_storage.py
   │   │   ├── tests
   │   │   │   ├── __init__.py
   │   │   │   ├── _conftest.py
   │   │   │   ├── data.py
   │   │   │   ├── sftp_server.py
   │   │   │   ├── test_augment.py
   │   │   │   ├── test_augment_file_from_dir_provider.py
   │   │   │   ├── test_base.py
   │   │   │   ├── test_cli.py
   │   │   │   ├── test_data_integrity.py
   │   │   │   ├── test_django_integration.py
   │   │   │   ├── test_helpers.py
   │   │   │   ├── test_providers.py
   │   │   │   ├── test_registry.py
   │   │   │   ├── test_sftp_server.py
   │   │   │   ├── test_sftp_storage.py
   │   │   │   ├── test_sqlalchemy_integration.py
   │   │   │   ├── test_storages.py
   │   │   │   ├── texts.py
   │   │   │   └── utils.py
   │   │   ├── __init__.py
   │   │   ├── base.py
   │   │   ├── constants.py
   │   │   ├── helpers.py
   │   │   └── registry.py
   │   └── faker_file.egg-info
   │       ├── dependency_links.txt
   │       ├── entry_points.txt
   │       ├── PKG-INFO
   │       ├── requires.txt
   │       ├── SOURCES.txt
   │       └── top_level.txt

docs/_static/examples/creating_docx/docx_1.py
---------------------------------------------

.. literalinclude:: _static/examples/creating_docx/docx_1.py
   :language: python
   :caption: docs/_static/examples/creating_docx/docx_1.py

docs/_static/examples/creating_docx/docx_2.py
---------------------------------------------

.. literalinclude:: _static/examples/creating_docx/docx_2.py
   :language: python
   :caption: docs/_static/examples/creating_docx/docx_2.py

docs/_static/examples/creating_docx/docx_3.py
---------------------------------------------

.. literalinclude:: _static/examples/creating_docx/docx_3.py
   :language: python
   :caption: docs/_static/examples/creating_docx/docx_3.py

docs/_static/examples/creating_docx/docx_4.py
---------------------------------------------

.. literalinclude:: _static/examples/creating_docx/docx_4.py
   :language: python
   :caption: docs/_static/examples/creating_docx/docx_4.py

docs/_static/examples/creating_images/augment_1.py
--------------------------------------------------

.. literalinclude:: _static/examples/creating_images/augment_1.py
   :language: python
   :caption: docs/_static/examples/creating_images/augment_1.py

docs/_static/examples/creating_images/imgkit_1.py
-------------------------------------------------

.. literalinclude:: _static/examples/creating_images/imgkit_1.py
   :language: python
   :caption: docs/_static/examples/creating_images/imgkit_1.py

docs/_static/examples/creating_images/imgkit_2.py
-------------------------------------------------

.. literalinclude:: _static/examples/creating_images/imgkit_2.py
   :language: python
   :caption: docs/_static/examples/creating_images/imgkit_2.py

docs/_static/examples/creating_images/imgkit_3.py
-------------------------------------------------

.. literalinclude:: _static/examples/creating_images/imgkit_3.py
   :language: python
   :caption: docs/_static/examples/creating_images/imgkit_3.py

docs/_static/examples/creating_images/imgkit_4.py
-------------------------------------------------

.. literalinclude:: _static/examples/creating_images/imgkit_4.py
   :language: python
   :caption: docs/_static/examples/creating_images/imgkit_4.py

docs/_static/examples/creating_images/pillow_1.py
-------------------------------------------------

.. literalinclude:: _static/examples/creating_images/pillow_1.py
   :language: python
   :caption: docs/_static/examples/creating_images/pillow_1.py

docs/_static/examples/creating_images/pillow_2.py
-------------------------------------------------

.. literalinclude:: _static/examples/creating_images/pillow_2.py
   :language: python
   :caption: docs/_static/examples/creating_images/pillow_2.py

docs/_static/examples/creating_images/pillow_3.py
-------------------------------------------------

.. literalinclude:: _static/examples/creating_images/pillow_3.py
   :language: python
   :caption: docs/_static/examples/creating_images/pillow_3.py

docs/_static/examples/creating_images/pillow_4.py
-------------------------------------------------

.. literalinclude:: _static/examples/creating_images/pillow_4.py
   :language: python
   :caption: docs/_static/examples/creating_images/pillow_4.py

docs/_static/examples/creating_images/pillow_5.py
-------------------------------------------------

.. literalinclude:: _static/examples/creating_images/pillow_5.py
   :language: python
   :caption: docs/_static/examples/creating_images/pillow_5.py

docs/_static/examples/creating_images/weasyprint_1.py
-----------------------------------------------------

.. literalinclude:: _static/examples/creating_images/weasyprint_1.py
   :language: python
   :caption: docs/_static/examples/creating_images/weasyprint_1.py

docs/_static/examples/creating_images/weasyprint_2.py
-----------------------------------------------------

.. literalinclude:: _static/examples/creating_images/weasyprint_2.py
   :language: python
   :caption: docs/_static/examples/creating_images/weasyprint_2.py

docs/_static/examples/creating_odt/odt_1.py
-------------------------------------------

.. literalinclude:: _static/examples/creating_odt/odt_1.py
   :language: python
   :caption: docs/_static/examples/creating_odt/odt_1.py

docs/_static/examples/creating_odt/odt_2.py
-------------------------------------------

.. literalinclude:: _static/examples/creating_odt/odt_2.py
   :language: python
   :caption: docs/_static/examples/creating_odt/odt_2.py

docs/_static/examples/creating_odt/odt_3.py
-------------------------------------------

.. literalinclude:: _static/examples/creating_odt/odt_3.py
   :language: python
   :caption: docs/_static/examples/creating_odt/odt_3.py

docs/_static/examples/creating_odt/odt_4.py
-------------------------------------------

.. literalinclude:: _static/examples/creating_odt/odt_4.py
   :language: python
   :caption: docs/_static/examples/creating_odt/odt_4.py

docs/_static/examples/creating_pdf/pdfkit_1.py
----------------------------------------------

.. literalinclude:: _static/examples/creating_pdf/pdfkit_1.py
   :language: python
   :caption: docs/_static/examples/creating_pdf/pdfkit_1.py

docs/_static/examples/creating_pdf/pdfkit_2.py
----------------------------------------------

.. literalinclude:: _static/examples/creating_pdf/pdfkit_2.py
   :language: python
   :caption: docs/_static/examples/creating_pdf/pdfkit_2.py

docs/_static/examples/creating_pdf/pdfkit_3.py
----------------------------------------------

.. literalinclude:: _static/examples/creating_pdf/pdfkit_3.py
   :language: python
   :caption: docs/_static/examples/creating_pdf/pdfkit_3.py

docs/_static/examples/creating_pdf/pdfkit_4.py
----------------------------------------------

.. literalinclude:: _static/examples/creating_pdf/pdfkit_4.py
   :language: python
   :caption: docs/_static/examples/creating_pdf/pdfkit_4.py

docs/_static/examples/creating_pdf/pillow_1.py
----------------------------------------------

.. literalinclude:: _static/examples/creating_pdf/pillow_1.py
   :language: python
   :caption: docs/_static/examples/creating_pdf/pillow_1.py

docs/_static/examples/creating_pdf/pillow_2.py
----------------------------------------------

.. literalinclude:: _static/examples/creating_pdf/pillow_2.py
   :language: python
   :caption: docs/_static/examples/creating_pdf/pillow_2.py

docs/_static/examples/creating_pdf/pillow_3.py
----------------------------------------------

.. literalinclude:: _static/examples/creating_pdf/pillow_3.py
   :language: python
   :caption: docs/_static/examples/creating_pdf/pillow_3.py

docs/_static/examples/creating_pdf/pillow_4.py
----------------------------------------------

.. literalinclude:: _static/examples/creating_pdf/pillow_4.py
   :language: python
   :caption: docs/_static/examples/creating_pdf/pillow_4.py

docs/_static/examples/creating_pdf/pillow_5.py
----------------------------------------------

.. literalinclude:: _static/examples/creating_pdf/pillow_5.py
   :language: python
   :caption: docs/_static/examples/creating_pdf/pillow_5.py

docs/_static/examples/creating_pdf/reportlab_1.py
-------------------------------------------------

.. literalinclude:: _static/examples/creating_pdf/reportlab_1.py
   :language: python
   :caption: docs/_static/examples/creating_pdf/reportlab_1.py

docs/_static/examples/creating_pdf/reportlab_2.py
-------------------------------------------------

.. literalinclude:: _static/examples/creating_pdf/reportlab_2.py
   :language: python
   :caption: docs/_static/examples/creating_pdf/reportlab_2.py

docs/_static/examples/methodology/clean_up_files_1.py
-----------------------------------------------------

.. literalinclude:: _static/examples/methodology/clean_up_files_1.py
   :language: python
   :caption: docs/_static/examples/methodology/clean_up_files_1.py

docs/_static/examples/methodology/clean_up_files_2.py
-----------------------------------------------------

.. literalinclude:: _static/examples/methodology/clean_up_files_2.py
   :language: python
   :caption: docs/_static/examples/methodology/clean_up_files_2.py

docs/_static/examples/methodology/clean_up_files_3.py
-----------------------------------------------------

.. literalinclude:: _static/examples/methodology/clean_up_files_3.py
   :language: python
   :caption: docs/_static/examples/methodology/clean_up_files_3.py

docs/_static/examples/methodology/create_docx_file_1.py
-------------------------------------------------------

.. literalinclude:: _static/examples/methodology/create_docx_file_1.py
   :language: python
   :caption: docs/_static/examples/methodology/create_docx_file_1.py

docs/_static/examples/methodology/create_docx_file_2.py
-------------------------------------------------------

.. literalinclude:: _static/examples/methodology/create_docx_file_2.py
   :language: python
   :caption: docs/_static/examples/methodology/create_docx_file_2.py

docs/_static/examples/methodology/create_docx_file_3.py
-------------------------------------------------------

.. literalinclude:: _static/examples/methodology/create_docx_file_3.py
   :language: python
   :caption: docs/_static/examples/methodology/create_docx_file_3.py

docs/_static/examples/methodology/file_from_path_provider.py
------------------------------------------------------------

.. literalinclude:: _static/examples/methodology/file_from_path_provider.py
   :language: python
   :caption: docs/_static/examples/methodology/file_from_path_provider.py

docs/_static/examples/methodology/rand_file_from_dir_provider.py
----------------------------------------------------------------

.. literalinclude:: _static/examples/methodology/rand_file_from_dir_provider.py
   :language: python
   :caption: docs/_static/examples/methodology/rand_file_from_dir_provider.py

docs/_static/examples/quick_start/factory_import_and_init_1.py
--------------------------------------------------------------

.. literalinclude:: _static/examples/quick_start/factory_import_and_init_1.py
   :language: python
   :caption: docs/_static/examples/quick_start/factory_import_and_init_1.py

docs/_static/examples/quick_start/factory_models_1.py
-----------------------------------------------------

.. literalinclude:: _static/examples/quick_start/factory_models_1.py
   :language: python
   :caption: docs/_static/examples/quick_start/factory_models_1.py

docs/_static/examples/quick_start/import_and_init_1.py
------------------------------------------------------

.. literalinclude:: _static/examples/quick_start/import_and_init_1.py
   :language: python
   :caption: docs/_static/examples/quick_start/import_and_init_1.py

docs/_static/examples/recipes/augment_file_from_dir_1.py
--------------------------------------------------------

.. literalinclude:: _static/examples/recipes/augment_file_from_dir_1.py
   :language: python
   :caption: docs/_static/examples/recipes/augment_file_from_dir_1.py

docs/_static/examples/recipes/augment_file_from_dir_2.py
--------------------------------------------------------

.. literalinclude:: _static/examples/recipes/augment_file_from_dir_2.py
   :language: python
   :caption: docs/_static/examples/recipes/augment_file_from_dir_2.py

docs/_static/examples/recipes/augment_file_from_dir_3.py
--------------------------------------------------------

.. literalinclude:: _static/examples/recipes/augment_file_from_dir_3.py
   :language: python
   :caption: docs/_static/examples/recipes/augment_file_from_dir_3.py

docs/_static/examples/recipes/augment_file_from_dir_4.py
--------------------------------------------------------

.. literalinclude:: _static/examples/recipes/augment_file_from_dir_4.py
   :language: python
   :caption: docs/_static/examples/recipes/augment_file_from_dir_4.py

docs/_static/examples/recipes/aws_s3_storage_1.py
-------------------------------------------------

.. literalinclude:: _static/examples/recipes/aws_s3_storage_1.py
   :language: python
   :caption: docs/_static/examples/recipes/aws_s3_storage_1.py

docs/_static/examples/recipes/aws_s3_storage_2.py
-------------------------------------------------

.. literalinclude:: _static/examples/recipes/aws_s3_storage_2.py
   :language: python
   :caption: docs/_static/examples/recipes/aws_s3_storage_2.py

docs/_static/examples/recipes/aws_s3_storage_3.py
-------------------------------------------------

.. literalinclude:: _static/examples/recipes/aws_s3_storage_3.py
   :language: python
   :caption: docs/_static/examples/recipes/aws_s3_storage_3.py

docs/_static/examples/recipes/aws_s3_storage_4.py
-------------------------------------------------

.. literalinclude:: _static/examples/recipes/aws_s3_storage_4.py
   :language: python
   :caption: docs/_static/examples/recipes/aws_s3_storage_4.py

docs/_static/examples/recipes/docx_file_1.py
--------------------------------------------

.. literalinclude:: _static/examples/recipes/docx_file_1.py
   :language: python
   :caption: docs/_static/examples/recipes/docx_file_1.py

docs/_static/examples/recipes/docx_file_mixed_1.py
--------------------------------------------------

.. literalinclude:: _static/examples/recipes/docx_file_mixed_1.py
   :language: python
   :caption: docs/_static/examples/recipes/docx_file_mixed_1.py

docs/_static/examples/recipes/eml_file_1.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/eml_file_1.py
   :language: python
   :caption: docs/_static/examples/recipes/eml_file_1.py

docs/_static/examples/recipes/eml_file_2.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/eml_file_2.py
   :language: python
   :caption: docs/_static/examples/recipes/eml_file_2.py

docs/_static/examples/recipes/eml_file_3.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/eml_file_3.py
   :language: python
   :caption: docs/_static/examples/recipes/eml_file_3.py

docs/_static/examples/recipes/eml_file_4.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/eml_file_4.py
   :language: python
   :caption: docs/_static/examples/recipes/eml_file_4.py

docs/_static/examples/recipes/eml_file_5.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/eml_file_5.py
   :language: python
   :caption: docs/_static/examples/recipes/eml_file_5.py

docs/_static/examples/recipes/factory_boy_factory_1.py
------------------------------------------------------

.. literalinclude:: _static/examples/recipes/factory_boy_factory_1.py
   :language: python
   :caption: docs/_static/examples/recipes/factory_boy_factory_1.py

docs/_static/examples/recipes/factory_boy_factory_2.py
------------------------------------------------------

.. literalinclude:: _static/examples/recipes/factory_boy_factory_2.py
   :language: python
   :caption: docs/_static/examples/recipes/factory_boy_factory_2.py

docs/_static/examples/recipes/factory_boy_factory_3.py
------------------------------------------------------

.. literalinclude:: _static/examples/recipes/factory_boy_factory_3.py
   :language: python
   :caption: docs/_static/examples/recipes/factory_boy_factory_3.py

docs/_static/examples/recipes/factory_boy_models_1.py
-----------------------------------------------------

.. literalinclude:: _static/examples/recipes/factory_boy_models_1.py
   :language: python
   :caption: docs/_static/examples/recipes/factory_boy_models_1.py

docs/_static/examples/recipes/file_from_path_1.py
-------------------------------------------------

.. literalinclude:: _static/examples/recipes/file_from_path_1.py
   :language: python
   :caption: docs/_static/examples/recipes/file_from_path_1.py

docs/_static/examples/recipes/file_of_size_bin_1.py
---------------------------------------------------

.. literalinclude:: _static/examples/recipes/file_of_size_bin_1.py
   :language: python
   :caption: docs/_static/examples/recipes/file_of_size_bin_1.py

docs/_static/examples/recipes/file_of_size_txt_1.py
---------------------------------------------------

.. literalinclude:: _static/examples/recipes/file_of_size_txt_1.py
   :language: python
   :caption: docs/_static/examples/recipes/file_of_size_txt_1.py

docs/_static/examples/recipes/files_multiprocessing_1.py
--------------------------------------------------------

.. literalinclude:: _static/examples/recipes/files_multiprocessing_1.py
   :language: python
   :caption: docs/_static/examples/recipes/files_multiprocessing_1.py

docs/_static/examples/recipes/files_multiprocessing_2.py
--------------------------------------------------------

.. literalinclude:: _static/examples/recipes/files_multiprocessing_2.py
   :language: python
   :caption: docs/_static/examples/recipes/files_multiprocessing_2.py

docs/_static/examples/recipes/flexible_storage_1.py
---------------------------------------------------

.. literalinclude:: _static/examples/recipes/flexible_storage_1.py
   :language: python
   :caption: docs/_static/examples/recipes/flexible_storage_1.py

docs/_static/examples/recipes/generic_file_1.py
-----------------------------------------------

.. literalinclude:: _static/examples/recipes/generic_file_1.py
   :language: python
   :caption: docs/_static/examples/recipes/generic_file_1.py

docs/_static/examples/recipes/google_cloud_storage_1.py
-------------------------------------------------------

.. literalinclude:: _static/examples/recipes/google_cloud_storage_1.py
   :language: python
   :caption: docs/_static/examples/recipes/google_cloud_storage_1.py

docs/_static/examples/recipes/google_cloud_storage_2.py
-------------------------------------------------------

.. literalinclude:: _static/examples/recipes/google_cloud_storage_2.py
   :language: python
   :caption: docs/_static/examples/recipes/google_cloud_storage_2.py

docs/_static/examples/recipes/graphic_ico_file_1.py
---------------------------------------------------

.. literalinclude:: _static/examples/recipes/graphic_ico_file_1.py
   :language: python
   :caption: docs/_static/examples/recipes/graphic_ico_file_1.py

docs/_static/examples/recipes/graphic_jpeg_file_1.py
----------------------------------------------------

.. literalinclude:: _static/examples/recipes/graphic_jpeg_file_1.py
   :language: python
   :caption: docs/_static/examples/recipes/graphic_jpeg_file_1.py

docs/_static/examples/recipes/graphic_png_file_1.py
---------------------------------------------------

.. literalinclude:: _static/examples/recipes/graphic_png_file_1.py
   :language: python
   :caption: docs/_static/examples/recipes/graphic_png_file_1.py

docs/_static/examples/recipes/graphic_webp_file_1.py
----------------------------------------------------

.. literalinclude:: _static/examples/recipes/graphic_webp_file_1.py
   :language: python
   :caption: docs/_static/examples/recipes/graphic_webp_file_1.py

docs/_static/examples/recipes/imports_and_init_1.py
---------------------------------------------------

.. literalinclude:: _static/examples/recipes/imports_and_init_1.py
   :language: python
   :caption: docs/_static/examples/recipes/imports_and_init_1.py

docs/_static/examples/recipes/imports_and_init_2.py
---------------------------------------------------

.. literalinclude:: _static/examples/recipes/imports_and_init_2.py
   :language: python
   :caption: docs/_static/examples/recipes/imports_and_init_2.py

docs/_static/examples/recipes/mp3_file_1.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/mp3_file_1.py
   :language: python
   :caption: docs/_static/examples/recipes/mp3_file_1.py

docs/_static/examples/recipes/mp3_file_custom_1.py
--------------------------------------------------

.. literalinclude:: _static/examples/recipes/mp3_file_custom_1.py
   :language: python
   :caption: docs/_static/examples/recipes/mp3_file_custom_1.py

docs/_static/examples/recipes/mp3_file_edge_tts_1.py
----------------------------------------------------

.. literalinclude:: _static/examples/recipes/mp3_file_edge_tts_1.py
   :language: python
   :caption: docs/_static/examples/recipes/mp3_file_edge_tts_1.py

docs/_static/examples/recipes/mp3_file_edge_tts_2.py
----------------------------------------------------

.. literalinclude:: _static/examples/recipes/mp3_file_edge_tts_2.py
   :language: python
   :caption: docs/_static/examples/recipes/mp3_file_edge_tts_2.py

docs/_static/examples/recipes/mp3_file_gtts_1.py
------------------------------------------------

.. literalinclude:: _static/examples/recipes/mp3_file_gtts_1.py
   :language: python
   :caption: docs/_static/examples/recipes/mp3_file_gtts_1.py

docs/_static/examples/recipes/mp3_file_gtts_2.py
------------------------------------------------

.. literalinclude:: _static/examples/recipes/mp3_file_gtts_2.py
   :language: python
   :caption: docs/_static/examples/recipes/mp3_file_gtts_2.py

docs/_static/examples/recipes/odt_file_mixed_1.py
-------------------------------------------------

.. literalinclude:: _static/examples/recipes/odt_file_mixed_1.py
   :language: python
   :caption: docs/_static/examples/recipes/odt_file_mixed_1.py

docs/_static/examples/recipes/pdf_file_1.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/pdf_file_1.py
   :language: python
   :caption: docs/_static/examples/recipes/pdf_file_1.py

docs/_static/examples/recipes/pdf_file_pdfkit_1.py
--------------------------------------------------

.. literalinclude:: _static/examples/recipes/pdf_file_pdfkit_1.py
   :language: python
   :caption: docs/_static/examples/recipes/pdf_file_pdfkit_1.py

docs/_static/examples/recipes/pdf_file_pillow_1.py
--------------------------------------------------

.. literalinclude:: _static/examples/recipes/pdf_file_pillow_1.py
   :language: python
   :caption: docs/_static/examples/recipes/pdf_file_pillow_1.py

docs/_static/examples/recipes/pdf_file_pillow_2.py
--------------------------------------------------

.. literalinclude:: _static/examples/recipes/pdf_file_pillow_2.py
   :language: python
   :caption: docs/_static/examples/recipes/pdf_file_pillow_2.py

docs/_static/examples/recipes/pdf_file_reportlab_1.py
-----------------------------------------------------

.. literalinclude:: _static/examples/recipes/pdf_file_reportlab_1.py
   :language: python
   :caption: docs/_static/examples/recipes/pdf_file_reportlab_1.py

docs/_static/examples/recipes/random_file_from_dir_1.py
-------------------------------------------------------

.. literalinclude:: _static/examples/recipes/random_file_from_dir_1.py
   :language: python
   :caption: docs/_static/examples/recipes/random_file_from_dir_1.py

docs/_static/examples/recipes/raw_1.py
--------------------------------------

.. literalinclude:: _static/examples/recipes/raw_1.py
   :language: python
   :caption: docs/_static/examples/recipes/raw_1.py

docs/_static/examples/recipes/sftp_storage_1.py
-----------------------------------------------

.. literalinclude:: _static/examples/recipes/sftp_storage_1.py
   :language: python
   :caption: docs/_static/examples/recipes/sftp_storage_1.py

docs/_static/examples/recipes/txt_file_1.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/txt_file_1.py
   :language: python
   :caption: docs/_static/examples/recipes/txt_file_1.py

docs/_static/examples/recipes/zip_file_1.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/zip_file_1.py
   :language: python
   :caption: docs/_static/examples/recipes/zip_file_1.py

docs/_static/examples/recipes/zip_file_2.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/zip_file_2.py
   :language: python
   :caption: docs/_static/examples/recipes/zip_file_2.py

docs/_static/examples/recipes/zip_file_3.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/zip_file_3.py
   :language: python
   :caption: docs/_static/examples/recipes/zip_file_3.py

docs/_static/examples/recipes/zip_file_4.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/zip_file_4.py
   :language: python
   :caption: docs/_static/examples/recipes/zip_file_4.py

docs/_static/examples/recipes/zip_file_5.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/zip_file_5.py
   :language: python
   :caption: docs/_static/examples/recipes/zip_file_5.py

docs/_static/examples/recipes/zip_file_6.py
-------------------------------------------

.. literalinclude:: _static/examples/recipes/zip_file_6.py
   :language: python
   :caption: docs/_static/examples/recipes/zip_file_6.py

docs/changelog.rst
------------------

.. literalinclude:: changelog.rst
   :language: rst
   :caption: docs/changelog.rst

docs/cli.rst
------------

.. literalinclude:: cli.rst
   :language: rst
   :caption: docs/cli.rst

docs/code_of_conduct.rst
------------------------

.. literalinclude:: code_of_conduct.rst
   :language: rst
   :caption: docs/code_of_conduct.rst

docs/concepts.rst
-----------------

.. literalinclude:: concepts.rst
   :language: rst
   :caption: docs/concepts.rst

docs/conf.py
------------

.. literalinclude:: conf.py
   :language: python
   :caption: docs/conf.py

docs/conftest.py
----------------

.. literalinclude:: conftest.py
   :language: python
   :caption: docs/conftest.py

docs/contributor_guidelines.rst
-------------------------------

.. literalinclude:: contributor_guidelines.rst
   :language: rst
   :caption: docs/contributor_guidelines.rst

docs/creating_docx.rst
----------------------

.. literalinclude:: creating_docx.rst
   :language: rst
   :caption: docs/creating_docx.rst

docs/creating_images.rst
------------------------

.. literalinclude:: creating_images.rst
   :language: rst
   :caption: docs/creating_images.rst

docs/creating_odt.rst
---------------------

.. literalinclude:: creating_odt.rst
   :language: rst
   :caption: docs/creating_odt.rst

docs/creating_pdf.rst
---------------------

.. literalinclude:: creating_pdf.rst
   :language: rst
   :caption: docs/creating_pdf.rst

docs/documentation.rst
----------------------

.. literalinclude:: documentation.rst
   :language: rst
   :caption: docs/documentation.rst

docs/faker_file.cli.rst
-----------------------

.. literalinclude:: faker_file.cli.rst
   :language: rst
   :caption: docs/faker_file.cli.rst

docs/faker_file.contrib.pdf_file.rst
------------------------------------

.. literalinclude:: faker_file.contrib.pdf_file.rst
   :language: rst
   :caption: docs/faker_file.contrib.pdf_file.rst

docs/faker_file.contrib.rst
---------------------------

.. literalinclude:: faker_file.contrib.rst
   :language: rst
   :caption: docs/faker_file.contrib.rst

docs/faker_file.providers.augment_file_from_dir.augmenters.rst
--------------------------------------------------------------

.. literalinclude:: faker_file.providers.augment_file_from_dir.augmenters.rst
   :language: rst
   :caption: docs/faker_file.providers.augment_file_from_dir.augmenters.rst

docs/faker_file.providers.augment_file_from_dir.extractors.rst
--------------------------------------------------------------

.. literalinclude:: faker_file.providers.augment_file_from_dir.extractors.rst
   :language: rst
   :caption: docs/faker_file.providers.augment_file_from_dir.extractors.rst

docs/faker_file.providers.augment_file_from_dir.rst
---------------------------------------------------

.. literalinclude:: faker_file.providers.augment_file_from_dir.rst
   :language: rst
   :caption: docs/faker_file.providers.augment_file_from_dir.rst

docs/faker_file.providers.base.rst
----------------------------------

.. literalinclude:: faker_file.providers.base.rst
   :language: rst
   :caption: docs/faker_file.providers.base.rst

docs/faker_file.providers.helpers.rst
-------------------------------------

.. literalinclude:: faker_file.providers.helpers.rst
   :language: rst
   :caption: docs/faker_file.providers.helpers.rst

docs/faker_file.providers.image.rst
-----------------------------------

.. literalinclude:: faker_file.providers.image.rst
   :language: rst
   :caption: docs/faker_file.providers.image.rst

docs/faker_file.providers.mixins.rst
------------------------------------

.. literalinclude:: faker_file.providers.mixins.rst
   :language: rst
   :caption: docs/faker_file.providers.mixins.rst

docs/faker_file.providers.mp3_file.generators.rst
-------------------------------------------------

.. literalinclude:: faker_file.providers.mp3_file.generators.rst
   :language: rst
   :caption: docs/faker_file.providers.mp3_file.generators.rst

docs/faker_file.providers.mp3_file.rst
--------------------------------------

.. literalinclude:: faker_file.providers.mp3_file.rst
   :language: rst
   :caption: docs/faker_file.providers.mp3_file.rst

docs/faker_file.providers.pdf_file.generators.rst
-------------------------------------------------

.. literalinclude:: faker_file.providers.pdf_file.generators.rst
   :language: rst
   :caption: docs/faker_file.providers.pdf_file.generators.rst

docs/faker_file.providers.pdf_file.rst
--------------------------------------

.. literalinclude:: faker_file.providers.pdf_file.rst
   :language: rst
   :caption: docs/faker_file.providers.pdf_file.rst

docs/faker_file.providers.rst
-----------------------------

.. literalinclude:: faker_file.providers.rst
   :language: rst
   :caption: docs/faker_file.providers.rst

docs/faker_file.rst
-------------------

.. literalinclude:: faker_file.rst
   :language: rst
   :caption: docs/faker_file.rst

docs/faker_file.storages.rst
----------------------------

.. literalinclude:: faker_file.storages.rst
   :language: rst
   :caption: docs/faker_file.storages.rst

docs/faker_file.tests.rst
-------------------------

.. literalinclude:: faker_file.tests.rst
   :language: rst
   :caption: docs/faker_file.tests.rst

docs/index.rst
--------------

.. literalinclude:: index.rst
   :language: rst
   :caption: docs/index.rst

docs/llms.rst
-------------

.. literalinclude:: llms.rst
   :language: rst
   :caption: docs/llms.rst

docs/marytts.py
---------------

.. literalinclude:: marytts.py
   :language: python
   :caption: docs/marytts.py

docs/methodology.rst
--------------------

.. literalinclude:: methodology.rst
   :language: rst
   :caption: docs/methodology.rst

docs/package.rst
----------------

.. literalinclude:: package.rst
   :language: rst
   :caption: docs/package.rst

docs/quick_start.rst
--------------------

.. literalinclude:: quick_start.rst
   :language: rst
   :caption: docs/quick_start.rst

docs/readme.rst
---------------

.. literalinclude:: readme.rst
   :language: rst
   :caption: docs/readme.rst

docs/recipes.rst
----------------

.. literalinclude:: recipes.rst
   :language: rst
   :caption: docs/recipes.rst

docs/security.rst
-----------------

.. literalinclude:: security.rst
   :language: rst
   :caption: docs/security.rst

docs/source_tree.rst
--------------------

.. literalinclude:: source_tree.rst
   :language: rst
   :caption: docs/source_tree.rst

docs/talks/pygrunn_2023.rst
---------------------------

.. literalinclude:: talks/pygrunn_2023.rst
   :language: rst
   :caption: docs/talks/pygrunn_2023.rst

docs/test_docs.py
-----------------

.. literalinclude:: test_docs.py
   :language: python
   :caption: docs/test_docs.py

examples/__init__.py
--------------------

.. literalinclude:: ../examples/__init__.py
   :language: python
   :caption: examples/__init__.py

examples/customizations/__init__.py
-----------------------------------

.. literalinclude:: ../examples/customizations/__init__.py
   :language: python
   :caption: examples/customizations/__init__.py

examples/customizations/marytts_mp3_generator/README.rst
--------------------------------------------------------

.. literalinclude:: ../examples/customizations/marytts_mp3_generator/README.rst
   :language: rst
   :caption: examples/customizations/marytts_mp3_generator/README.rst

examples/customizations/marytts_mp3_generator/__init__.py
---------------------------------------------------------

.. literalinclude:: ../examples/customizations/marytts_mp3_generator/__init__.py
   :language: python
   :caption: examples/customizations/marytts_mp3_generator/__init__.py

examples/django_example/README.rst
----------------------------------

.. literalinclude:: ../examples/django_example/README.rst
   :language: rst
   :caption: examples/django_example/README.rst

examples/django_example/__init__.py
-----------------------------------

.. literalinclude:: ../examples/django_example/__init__.py
   :language: python
   :caption: examples/django_example/__init__.py

examples/django_example/factories/__init__.py
---------------------------------------------

.. literalinclude:: ../examples/django_example/factories/__init__.py
   :language: python
   :caption: examples/django_example/factories/__init__.py

examples/django_example/factories/auth_user.py
----------------------------------------------

.. literalinclude:: ../examples/django_example/factories/auth_user.py
   :language: python
   :caption: examples/django_example/factories/auth_user.py

examples/django_example/factories/upload_upload.py
--------------------------------------------------

.. literalinclude:: ../examples/django_example/factories/upload_upload.py
   :language: python
   :caption: examples/django_example/factories/upload_upload.py

examples/django_example/manage.py
---------------------------------

.. literalinclude:: ../examples/django_example/manage.py
   :language: python
   :caption: examples/django_example/manage.py

examples/django_example/project/__init__.py
-------------------------------------------

.. literalinclude:: ../examples/django_example/project/__init__.py
   :language: python
   :caption: examples/django_example/project/__init__.py

examples/django_example/project/settings/__init__.py
----------------------------------------------------

.. literalinclude:: ../examples/django_example/project/settings/__init__.py
   :language: python
   :caption: examples/django_example/project/settings/__init__.py

examples/django_example/project/settings/base.py
------------------------------------------------

.. literalinclude:: ../examples/django_example/project/settings/base.py
   :language: python
   :caption: examples/django_example/project/settings/base.py

examples/django_example/project/settings/core.py
------------------------------------------------

.. literalinclude:: ../examples/django_example/project/settings/core.py
   :language: python
   :caption: examples/django_example/project/settings/core.py

examples/django_example/project/settings/dev.py
-----------------------------------------------

.. literalinclude:: ../examples/django_example/project/settings/dev.py
   :language: python
   :caption: examples/django_example/project/settings/dev.py

examples/django_example/project/settings/docs.py
------------------------------------------------

.. literalinclude:: ../examples/django_example/project/settings/docs.py
   :language: python
   :caption: examples/django_example/project/settings/docs.py

examples/django_example/project/settings/testing.py
---------------------------------------------------

.. literalinclude:: ../examples/django_example/project/settings/testing.py
   :language: python
   :caption: examples/django_example/project/settings/testing.py

examples/django_example/project/urls.py
---------------------------------------

.. literalinclude:: ../examples/django_example/project/urls.py
   :language: python
   :caption: examples/django_example/project/urls.py

examples/django_example/project/wsgi.py
---------------------------------------

.. literalinclude:: ../examples/django_example/project/wsgi.py
   :language: python
   :caption: examples/django_example/project/wsgi.py

examples/django_example/upload/__init__.py
------------------------------------------

.. literalinclude:: ../examples/django_example/upload/__init__.py
   :language: python
   :caption: examples/django_example/upload/__init__.py

examples/django_example/upload/admin.py
---------------------------------------

.. literalinclude:: ../examples/django_example/upload/admin.py
   :language: python
   :caption: examples/django_example/upload/admin.py

examples/django_example/upload/api/__init__.py
----------------------------------------------

.. literalinclude:: ../examples/django_example/upload/api/__init__.py
   :language: python
   :caption: examples/django_example/upload/api/__init__.py

examples/django_example/upload/api/serializers.py
-------------------------------------------------

.. literalinclude:: ../examples/django_example/upload/api/serializers.py
   :language: python
   :caption: examples/django_example/upload/api/serializers.py

examples/django_example/upload/api/tests.py
-------------------------------------------

.. literalinclude:: ../examples/django_example/upload/api/tests.py
   :language: python
   :caption: examples/django_example/upload/api/tests.py

examples/django_example/upload/api/urls.py
------------------------------------------

.. literalinclude:: ../examples/django_example/upload/api/urls.py
   :language: python
   :caption: examples/django_example/upload/api/urls.py

examples/django_example/upload/api/views.py
-------------------------------------------

.. literalinclude:: ../examples/django_example/upload/api/views.py
   :language: python
   :caption: examples/django_example/upload/api/views.py

examples/django_example/upload/migrations/0001_initial.py
---------------------------------------------------------

.. literalinclude:: ../examples/django_example/upload/migrations/0001_initial.py
   :language: python
   :caption: examples/django_example/upload/migrations/0001_initial.py

examples/django_example/upload/migrations/__init__.py
-----------------------------------------------------

.. literalinclude:: ../examples/django_example/upload/migrations/__init__.py
   :language: python
   :caption: examples/django_example/upload/migrations/__init__.py

examples/django_example/upload/models.py
----------------------------------------

.. literalinclude:: ../examples/django_example/upload/models.py
   :language: python
   :caption: examples/django_example/upload/models.py

examples/sqlalchemy_example/README.rst
--------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/README.rst
   :language: rst
   :caption: examples/sqlalchemy_example/README.rst

examples/sqlalchemy_example/faker_file_admin/__init__.py
--------------------------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/faker_file_admin/__init__.py
   :language: python
   :caption: examples/sqlalchemy_example/faker_file_admin/__init__.py

examples/sqlalchemy_example/faker_file_admin/alembic/__init__.py
----------------------------------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/faker_file_admin/alembic/__init__.py
   :language: python
   :caption: examples/sqlalchemy_example/faker_file_admin/alembic/__init__.py

examples/sqlalchemy_example/faker_file_admin/alembic/env.py
-----------------------------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/faker_file_admin/alembic/env.py
   :language: python
   :caption: examples/sqlalchemy_example/faker_file_admin/alembic/env.py

examples/sqlalchemy_example/faker_file_admin/alembic/versions/2695cb77cdf2_create_product_table.py
--------------------------------------------------------------------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/faker_file_admin/alembic/versions/2695cb77cdf2_create_product_table.py
   :language: python
   :caption: examples/sqlalchemy_example/faker_file_admin/alembic/versions/2695cb77cdf2_create_product_table.py

examples/sqlalchemy_example/faker_file_admin/alembic/versions/__init__.py
-------------------------------------------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/faker_file_admin/alembic/versions/__init__.py
   :language: python
   :caption: examples/sqlalchemy_example/faker_file_admin/alembic/versions/__init__.py

examples/sqlalchemy_example/faker_file_admin/config.py
------------------------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/faker_file_admin/config.py
   :language: python
   :caption: examples/sqlalchemy_example/faker_file_admin/config.py

examples/sqlalchemy_example/faker_file_admin/config_test.py
-----------------------------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/faker_file_admin/config_test.py
   :language: python
   :caption: examples/sqlalchemy_example/faker_file_admin/config_test.py

examples/sqlalchemy_example/faker_file_admin/data.py
----------------------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/faker_file_admin/data.py
   :language: python
   :caption: examples/sqlalchemy_example/faker_file_admin/data.py

examples/sqlalchemy_example/faker_file_admin/main.py
----------------------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/faker_file_admin/main.py
   :language: python
   :caption: examples/sqlalchemy_example/faker_file_admin/main.py

examples/sqlalchemy_example/faker_file_admin/models.py
------------------------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/faker_file_admin/models.py
   :language: python
   :caption: examples/sqlalchemy_example/faker_file_admin/models.py

examples/sqlalchemy_example/run_server.py
-----------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/run_server.py
   :language: python
   :caption: examples/sqlalchemy_example/run_server.py

examples/sqlalchemy_example/sqlalchemy_factories/__init__.py
------------------------------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/sqlalchemy_factories/__init__.py
   :language: python
   :caption: examples/sqlalchemy_example/sqlalchemy_factories/__init__.py

examples/sqlalchemy_example/sqlalchemy_factories/faker_file_admin_upload.py
---------------------------------------------------------------------------

.. literalinclude:: ../examples/sqlalchemy_example/sqlalchemy_factories/faker_file_admin_upload.py
   :language: python
   :caption: examples/sqlalchemy_example/sqlalchemy_factories/faker_file_admin_upload.py

scripts/generate_project_source_tree.py
---------------------------------------

.. literalinclude:: ../scripts/generate_project_source_tree.py
   :language: python
   :caption: scripts/generate_project_source_tree.py

src/faker_file/__init__.py
--------------------------

.. literalinclude:: ../src/faker_file/__init__.py
   :language: python
   :caption: src/faker_file/__init__.py

src/faker_file/base.py
----------------------

.. literalinclude:: ../src/faker_file/base.py
   :language: python
   :caption: src/faker_file/base.py

src/faker_file/cli/__init__.py
------------------------------

.. literalinclude:: ../src/faker_file/cli/__init__.py
   :language: python
   :caption: src/faker_file/cli/__init__.py

src/faker_file/cli/command.py
-----------------------------

.. literalinclude:: ../src/faker_file/cli/command.py
   :language: python
   :caption: src/faker_file/cli/command.py

src/faker_file/cli/helpers.py
-----------------------------

.. literalinclude:: ../src/faker_file/cli/helpers.py
   :language: python
   :caption: src/faker_file/cli/helpers.py

src/faker_file/constants.py
---------------------------

.. literalinclude:: ../src/faker_file/constants.py
   :language: python
   :caption: src/faker_file/constants.py

src/faker_file/contrib/__init__.py
----------------------------------

.. literalinclude:: ../src/faker_file/contrib/__init__.py
   :language: python
   :caption: src/faker_file/contrib/__init__.py

src/faker_file/contrib/docx_file.py
-----------------------------------

.. literalinclude:: ../src/faker_file/contrib/docx_file.py
   :language: python
   :caption: src/faker_file/contrib/docx_file.py

src/faker_file/contrib/image/__init__.py
----------------------------------------

.. literalinclude:: ../src/faker_file/contrib/image/__init__.py
   :language: python
   :caption: src/faker_file/contrib/image/__init__.py

src/faker_file/contrib/image/imgkit_snippets.py
-----------------------------------------------

.. literalinclude:: ../src/faker_file/contrib/image/imgkit_snippets.py
   :language: python
   :caption: src/faker_file/contrib/image/imgkit_snippets.py

src/faker_file/contrib/image/pil_snippets.py
--------------------------------------------

.. literalinclude:: ../src/faker_file/contrib/image/pil_snippets.py
   :language: python
   :caption: src/faker_file/contrib/image/pil_snippets.py

src/faker_file/contrib/image/weasyprint_snippets.py
---------------------------------------------------

.. literalinclude:: ../src/faker_file/contrib/image/weasyprint_snippets.py
   :language: python
   :caption: src/faker_file/contrib/image/weasyprint_snippets.py

src/faker_file/contrib/odt_file.py
----------------------------------

.. literalinclude:: ../src/faker_file/contrib/odt_file.py
   :language: python
   :caption: src/faker_file/contrib/odt_file.py

src/faker_file/contrib/pdf_file/__init__.py
-------------------------------------------

.. literalinclude:: ../src/faker_file/contrib/pdf_file/__init__.py
   :language: python
   :caption: src/faker_file/contrib/pdf_file/__init__.py

src/faker_file/contrib/pdf_file/pdfkit_snippets.py
--------------------------------------------------

.. literalinclude:: ../src/faker_file/contrib/pdf_file/pdfkit_snippets.py
   :language: python
   :caption: src/faker_file/contrib/pdf_file/pdfkit_snippets.py

src/faker_file/contrib/pdf_file/pil_snippets.py
-----------------------------------------------

.. literalinclude:: ../src/faker_file/contrib/pdf_file/pil_snippets.py
   :language: python
   :caption: src/faker_file/contrib/pdf_file/pil_snippets.py

src/faker_file/contrib/pdf_file/reportlab_snippets.py
-----------------------------------------------------

.. literalinclude:: ../src/faker_file/contrib/pdf_file/reportlab_snippets.py
   :language: python
   :caption: src/faker_file/contrib/pdf_file/reportlab_snippets.py

src/faker_file/helpers.py
-------------------------

.. literalinclude:: ../src/faker_file/helpers.py
   :language: python
   :caption: src/faker_file/helpers.py

src/faker_file/providers/__init__.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/__init__.py
   :language: python
   :caption: src/faker_file/providers/__init__.py

src/faker_file/providers/augment_file_from_dir/__init__.py
----------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/augment_file_from_dir/__init__.py
   :language: python
   :caption: src/faker_file/providers/augment_file_from_dir/__init__.py

src/faker_file/providers/augment_file_from_dir/augmenters/__init__.py
---------------------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/augment_file_from_dir/augmenters/__init__.py
   :language: python
   :caption: src/faker_file/providers/augment_file_from_dir/augmenters/__init__.py

src/faker_file/providers/augment_file_from_dir/augmenters/nlpaug_augmenter.py
-----------------------------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/augment_file_from_dir/augmenters/nlpaug_augmenter.py
   :language: python
   :caption: src/faker_file/providers/augment_file_from_dir/augmenters/nlpaug_augmenter.py

src/faker_file/providers/augment_file_from_dir/augmenters/textaugment_augmenter.py
----------------------------------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/augment_file_from_dir/augmenters/textaugment_augmenter.py
   :language: python
   :caption: src/faker_file/providers/augment_file_from_dir/augmenters/textaugment_augmenter.py

src/faker_file/providers/augment_file_from_dir/extractors/__init__.py
---------------------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/augment_file_from_dir/extractors/__init__.py
   :language: python
   :caption: src/faker_file/providers/augment_file_from_dir/extractors/__init__.py

src/faker_file/providers/augment_file_from_dir/extractors/tika_extractor.py
---------------------------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/augment_file_from_dir/extractors/tika_extractor.py
   :language: python
   :caption: src/faker_file/providers/augment_file_from_dir/extractors/tika_extractor.py

src/faker_file/providers/augment_image_from_path.py
---------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/augment_image_from_path.py
   :language: python
   :caption: src/faker_file/providers/augment_image_from_path.py

src/faker_file/providers/augment_random_image_from_dir.py
---------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/augment_random_image_from_dir.py
   :language: python
   :caption: src/faker_file/providers/augment_random_image_from_dir.py

src/faker_file/providers/base/__init__.py
-----------------------------------------

.. literalinclude:: ../src/faker_file/providers/base/__init__.py
   :language: python
   :caption: src/faker_file/providers/base/__init__.py

src/faker_file/providers/base/image_generator.py
------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/base/image_generator.py
   :language: python
   :caption: src/faker_file/providers/base/image_generator.py

src/faker_file/providers/base/mp3_generator.py
----------------------------------------------

.. literalinclude:: ../src/faker_file/providers/base/mp3_generator.py
   :language: python
   :caption: src/faker_file/providers/base/mp3_generator.py

src/faker_file/providers/base/pdf_generator.py
----------------------------------------------

.. literalinclude:: ../src/faker_file/providers/base/pdf_generator.py
   :language: python
   :caption: src/faker_file/providers/base/pdf_generator.py

src/faker_file/providers/base/text_augmenter.py
-----------------------------------------------

.. literalinclude:: ../src/faker_file/providers/base/text_augmenter.py
   :language: python
   :caption: src/faker_file/providers/base/text_augmenter.py

src/faker_file/providers/base/text_extractor.py
-----------------------------------------------

.. literalinclude:: ../src/faker_file/providers/base/text_extractor.py
   :language: python
   :caption: src/faker_file/providers/base/text_extractor.py

src/faker_file/providers/bin_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/bin_file.py
   :language: python
   :caption: src/faker_file/providers/bin_file.py

src/faker_file/providers/bmp_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/bmp_file.py
   :language: python
   :caption: src/faker_file/providers/bmp_file.py

src/faker_file/providers/csv_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/csv_file.py
   :language: python
   :caption: src/faker_file/providers/csv_file.py

src/faker_file/providers/docx_file.py
-------------------------------------

.. literalinclude:: ../src/faker_file/providers/docx_file.py
   :language: python
   :caption: src/faker_file/providers/docx_file.py

src/faker_file/providers/eml_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/eml_file.py
   :language: python
   :caption: src/faker_file/providers/eml_file.py

src/faker_file/providers/epub_file.py
-------------------------------------

.. literalinclude:: ../src/faker_file/providers/epub_file.py
   :language: python
   :caption: src/faker_file/providers/epub_file.py

src/faker_file/providers/file_from_path.py
------------------------------------------

.. literalinclude:: ../src/faker_file/providers/file_from_path.py
   :language: python
   :caption: src/faker_file/providers/file_from_path.py

src/faker_file/providers/file_from_url.py
-----------------------------------------

.. literalinclude:: ../src/faker_file/providers/file_from_url.py
   :language: python
   :caption: src/faker_file/providers/file_from_url.py

src/faker_file/providers/generic_file.py
----------------------------------------

.. literalinclude:: ../src/faker_file/providers/generic_file.py
   :language: python
   :caption: src/faker_file/providers/generic_file.py

src/faker_file/providers/gif_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/gif_file.py
   :language: python
   :caption: src/faker_file/providers/gif_file.py

src/faker_file/providers/helpers/__init__.py
--------------------------------------------

.. literalinclude:: ../src/faker_file/providers/helpers/__init__.py
   :language: python
   :caption: src/faker_file/providers/helpers/__init__.py

src/faker_file/providers/helpers/inner.py
-----------------------------------------

.. literalinclude:: ../src/faker_file/providers/helpers/inner.py
   :language: python
   :caption: src/faker_file/providers/helpers/inner.py

src/faker_file/providers/ico_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/ico_file.py
   :language: python
   :caption: src/faker_file/providers/ico_file.py

src/faker_file/providers/image/__init__.py
------------------------------------------

.. literalinclude:: ../src/faker_file/providers/image/__init__.py
   :language: python
   :caption: src/faker_file/providers/image/__init__.py

src/faker_file/providers/image/augment.py
-----------------------------------------

.. literalinclude:: ../src/faker_file/providers/image/augment.py
   :language: python
   :caption: src/faker_file/providers/image/augment.py

src/faker_file/providers/image/imgkit_generator.py
--------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/image/imgkit_generator.py
   :language: python
   :caption: src/faker_file/providers/image/imgkit_generator.py

src/faker_file/providers/image/pil_generator.py
-----------------------------------------------

.. literalinclude:: ../src/faker_file/providers/image/pil_generator.py
   :language: python
   :caption: src/faker_file/providers/image/pil_generator.py

src/faker_file/providers/image/weasyprint_generator.py
------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/image/weasyprint_generator.py
   :language: python
   :caption: src/faker_file/providers/image/weasyprint_generator.py

src/faker_file/providers/jpeg_file.py
-------------------------------------

.. literalinclude:: ../src/faker_file/providers/jpeg_file.py
   :language: python
   :caption: src/faker_file/providers/jpeg_file.py

src/faker_file/providers/json_file.py
-------------------------------------

.. literalinclude:: ../src/faker_file/providers/json_file.py
   :language: python
   :caption: src/faker_file/providers/json_file.py

src/faker_file/providers/mixins/__init__.py
-------------------------------------------

.. literalinclude:: ../src/faker_file/providers/mixins/__init__.py
   :language: python
   :caption: src/faker_file/providers/mixins/__init__.py

src/faker_file/providers/mixins/graphic_image_mixin.py
------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/mixins/graphic_image_mixin.py
   :language: python
   :caption: src/faker_file/providers/mixins/graphic_image_mixin.py

src/faker_file/providers/mixins/image_mixin.py
----------------------------------------------

.. literalinclude:: ../src/faker_file/providers/mixins/image_mixin.py
   :language: python
   :caption: src/faker_file/providers/mixins/image_mixin.py

src/faker_file/providers/mixins/tablular_data_mixin.py
------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/mixins/tablular_data_mixin.py
   :language: python
   :caption: src/faker_file/providers/mixins/tablular_data_mixin.py

src/faker_file/providers/mp3_file/__init__.py
---------------------------------------------

.. literalinclude:: ../src/faker_file/providers/mp3_file/__init__.py
   :language: python
   :caption: src/faker_file/providers/mp3_file/__init__.py

src/faker_file/providers/mp3_file/generators/__init__.py
--------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/mp3_file/generators/__init__.py
   :language: python
   :caption: src/faker_file/providers/mp3_file/generators/__init__.py

src/faker_file/providers/mp3_file/generators/edge_tts_generator.py
------------------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/mp3_file/generators/edge_tts_generator.py
   :language: python
   :caption: src/faker_file/providers/mp3_file/generators/edge_tts_generator.py

src/faker_file/providers/mp3_file/generators/gtts_generator.py
--------------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/mp3_file/generators/gtts_generator.py
   :language: python
   :caption: src/faker_file/providers/mp3_file/generators/gtts_generator.py

src/faker_file/providers/odp_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/odp_file.py
   :language: python
   :caption: src/faker_file/providers/odp_file.py

src/faker_file/providers/ods_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/ods_file.py
   :language: python
   :caption: src/faker_file/providers/ods_file.py

src/faker_file/providers/odt_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/odt_file.py
   :language: python
   :caption: src/faker_file/providers/odt_file.py

src/faker_file/providers/pdf_file/__init__.py
---------------------------------------------

.. literalinclude:: ../src/faker_file/providers/pdf_file/__init__.py
   :language: python
   :caption: src/faker_file/providers/pdf_file/__init__.py

src/faker_file/providers/pdf_file/generators/__init__.py
--------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/pdf_file/generators/__init__.py
   :language: python
   :caption: src/faker_file/providers/pdf_file/generators/__init__.py

src/faker_file/providers/pdf_file/generators/pdfkit_generator.py
----------------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/pdf_file/generators/pdfkit_generator.py
   :language: python
   :caption: src/faker_file/providers/pdf_file/generators/pdfkit_generator.py

src/faker_file/providers/pdf_file/generators/pil_generator.py
-------------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/pdf_file/generators/pil_generator.py
   :language: python
   :caption: src/faker_file/providers/pdf_file/generators/pil_generator.py

src/faker_file/providers/pdf_file/generators/reportlab_generator.py
-------------------------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/pdf_file/generators/reportlab_generator.py
   :language: python
   :caption: src/faker_file/providers/pdf_file/generators/reportlab_generator.py

src/faker_file/providers/png_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/png_file.py
   :language: python
   :caption: src/faker_file/providers/png_file.py

src/faker_file/providers/pptx_file.py
-------------------------------------

.. literalinclude:: ../src/faker_file/providers/pptx_file.py
   :language: python
   :caption: src/faker_file/providers/pptx_file.py

src/faker_file/providers/random_file_from_dir.py
------------------------------------------------

.. literalinclude:: ../src/faker_file/providers/random_file_from_dir.py
   :language: python
   :caption: src/faker_file/providers/random_file_from_dir.py

src/faker_file/providers/rtf_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/rtf_file.py
   :language: python
   :caption: src/faker_file/providers/rtf_file.py

src/faker_file/providers/svg_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/svg_file.py
   :language: python
   :caption: src/faker_file/providers/svg_file.py

src/faker_file/providers/tar_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/tar_file.py
   :language: python
   :caption: src/faker_file/providers/tar_file.py

src/faker_file/providers/tiff_file.py
-------------------------------------

.. literalinclude:: ../src/faker_file/providers/tiff_file.py
   :language: python
   :caption: src/faker_file/providers/tiff_file.py

src/faker_file/providers/txt_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/txt_file.py
   :language: python
   :caption: src/faker_file/providers/txt_file.py

src/faker_file/providers/webp_file.py
-------------------------------------

.. literalinclude:: ../src/faker_file/providers/webp_file.py
   :language: python
   :caption: src/faker_file/providers/webp_file.py

src/faker_file/providers/xlsx_file.py
-------------------------------------

.. literalinclude:: ../src/faker_file/providers/xlsx_file.py
   :language: python
   :caption: src/faker_file/providers/xlsx_file.py

src/faker_file/providers/xml_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/xml_file.py
   :language: python
   :caption: src/faker_file/providers/xml_file.py

src/faker_file/providers/zip_file.py
------------------------------------

.. literalinclude:: ../src/faker_file/providers/zip_file.py
   :language: python
   :caption: src/faker_file/providers/zip_file.py

src/faker_file/registry.py
--------------------------

.. literalinclude:: ../src/faker_file/registry.py
   :language: python
   :caption: src/faker_file/registry.py

src/faker_file/storages/__init__.py
-----------------------------------

.. literalinclude:: ../src/faker_file/storages/__init__.py
   :language: python
   :caption: src/faker_file/storages/__init__.py

src/faker_file/storages/aws_s3.py
---------------------------------

.. literalinclude:: ../src/faker_file/storages/aws_s3.py
   :language: python
   :caption: src/faker_file/storages/aws_s3.py

src/faker_file/storages/azure_cloud_storage.py
----------------------------------------------

.. literalinclude:: ../src/faker_file/storages/azure_cloud_storage.py
   :language: python
   :caption: src/faker_file/storages/azure_cloud_storage.py

src/faker_file/storages/base.py
-------------------------------

.. literalinclude:: ../src/faker_file/storages/base.py
   :language: python
   :caption: src/faker_file/storages/base.py

src/faker_file/storages/cloud.py
--------------------------------

.. literalinclude:: ../src/faker_file/storages/cloud.py
   :language: python
   :caption: src/faker_file/storages/cloud.py

src/faker_file/storages/filesystem.py
-------------------------------------

.. literalinclude:: ../src/faker_file/storages/filesystem.py
   :language: python
   :caption: src/faker_file/storages/filesystem.py

src/faker_file/storages/google_cloud_storage.py
-----------------------------------------------

.. literalinclude:: ../src/faker_file/storages/google_cloud_storage.py
   :language: python
   :caption: src/faker_file/storages/google_cloud_storage.py

src/faker_file/storages/pathy_based/__init__.py
-----------------------------------------------

.. literalinclude:: ../src/faker_file/storages/pathy_based/__init__.py
   :language: python
   :caption: src/faker_file/storages/pathy_based/__init__.py

src/faker_file/storages/pathy_based/aws_s3.py
---------------------------------------------

.. literalinclude:: ../src/faker_file/storages/pathy_based/aws_s3.py
   :language: python
   :caption: src/faker_file/storages/pathy_based/aws_s3.py

src/faker_file/storages/pathy_based/azure_cloud_storage.py
----------------------------------------------------------

.. literalinclude:: ../src/faker_file/storages/pathy_based/azure_cloud_storage.py
   :language: python
   :caption: src/faker_file/storages/pathy_based/azure_cloud_storage.py

src/faker_file/storages/pathy_based/cloud.py
--------------------------------------------

.. literalinclude:: ../src/faker_file/storages/pathy_based/cloud.py
   :language: python
   :caption: src/faker_file/storages/pathy_based/cloud.py

src/faker_file/storages/pathy_based/google_cloud_storage.py
-----------------------------------------------------------

.. literalinclude:: ../src/faker_file/storages/pathy_based/google_cloud_storage.py
   :language: python
   :caption: src/faker_file/storages/pathy_based/google_cloud_storage.py

src/faker_file/storages/pathy_based/helpers.py
----------------------------------------------

.. literalinclude:: ../src/faker_file/storages/pathy_based/helpers.py
   :language: python
   :caption: src/faker_file/storages/pathy_based/helpers.py

src/faker_file/storages/sftp_storage.py
---------------------------------------

.. literalinclude:: ../src/faker_file/storages/sftp_storage.py
   :language: python
   :caption: src/faker_file/storages/sftp_storage.py

src/faker_file/tests/__init__.py
--------------------------------

.. literalinclude:: ../src/faker_file/tests/__init__.py
   :language: python
   :caption: src/faker_file/tests/__init__.py

src/faker_file/tests/_conftest.py
---------------------------------

.. literalinclude:: ../src/faker_file/tests/_conftest.py
   :language: python
   :caption: src/faker_file/tests/_conftest.py

src/faker_file/tests/data.py
----------------------------

.. literalinclude:: ../src/faker_file/tests/data.py
   :language: python
   :caption: src/faker_file/tests/data.py

src/faker_file/tests/sftp_server.py
-----------------------------------

.. literalinclude:: ../src/faker_file/tests/sftp_server.py
   :language: python
   :caption: src/faker_file/tests/sftp_server.py

src/faker_file/tests/test_augment.py
------------------------------------

.. literalinclude:: ../src/faker_file/tests/test_augment.py
   :language: python
   :caption: src/faker_file/tests/test_augment.py

src/faker_file/tests/test_augment_file_from_dir_provider.py
-----------------------------------------------------------

.. literalinclude:: ../src/faker_file/tests/test_augment_file_from_dir_provider.py
   :language: python
   :caption: src/faker_file/tests/test_augment_file_from_dir_provider.py

src/faker_file/tests/test_base.py
---------------------------------

.. literalinclude:: ../src/faker_file/tests/test_base.py
   :language: python
   :caption: src/faker_file/tests/test_base.py

src/faker_file/tests/test_cli.py
--------------------------------

.. literalinclude:: ../src/faker_file/tests/test_cli.py
   :language: python
   :caption: src/faker_file/tests/test_cli.py

src/faker_file/tests/test_data_integrity.py
-------------------------------------------

.. literalinclude:: ../src/faker_file/tests/test_data_integrity.py
   :language: python
   :caption: src/faker_file/tests/test_data_integrity.py

src/faker_file/tests/test_django_integration.py
-----------------------------------------------

.. literalinclude:: ../src/faker_file/tests/test_django_integration.py
   :language: python
   :caption: src/faker_file/tests/test_django_integration.py

src/faker_file/tests/test_helpers.py
------------------------------------

.. literalinclude:: ../src/faker_file/tests/test_helpers.py
   :language: python
   :caption: src/faker_file/tests/test_helpers.py

src/faker_file/tests/test_providers.py
--------------------------------------

.. literalinclude:: ../src/faker_file/tests/test_providers.py
   :language: python
   :caption: src/faker_file/tests/test_providers.py

src/faker_file/tests/test_registry.py
-------------------------------------

.. literalinclude:: ../src/faker_file/tests/test_registry.py
   :language: python
   :caption: src/faker_file/tests/test_registry.py

src/faker_file/tests/test_sftp_server.py
----------------------------------------

.. literalinclude:: ../src/faker_file/tests/test_sftp_server.py
   :language: python
   :caption: src/faker_file/tests/test_sftp_server.py

src/faker_file/tests/test_sftp_storage.py
-----------------------------------------

.. literalinclude:: ../src/faker_file/tests/test_sftp_storage.py
   :language: python
   :caption: src/faker_file/tests/test_sftp_storage.py

src/faker_file/tests/test_sqlalchemy_integration.py
---------------------------------------------------

.. literalinclude:: ../src/faker_file/tests/test_sqlalchemy_integration.py
   :language: python
   :caption: src/faker_file/tests/test_sqlalchemy_integration.py

src/faker_file/tests/test_storages.py
-------------------------------------

.. literalinclude:: ../src/faker_file/tests/test_storages.py
   :language: python
   :caption: src/faker_file/tests/test_storages.py

src/faker_file/tests/texts.py
-----------------------------

.. literalinclude:: ../src/faker_file/tests/texts.py
   :language: python
   :caption: src/faker_file/tests/texts.py

src/faker_file/tests/utils.py
-----------------------------

.. literalinclude:: ../src/faker_file/tests/utils.py
   :language: python
   :caption: src/faker_file/tests/utils.py
