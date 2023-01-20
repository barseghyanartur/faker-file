from io import BytesIO
from typing import Optional

from faker.providers import BaseProvider
from odf import draw, style
from odf.opendocument import OpenDocumentPresentation
from odf.text import P

from ..base import FileMixin, StringValue
from ..constants import DEFAULT_TEXT_MAX_NB_CHARS
from ..storages.base import BaseStorage
from ..storages.filesystem import FileSystemStorage

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("OdpFileProvider",)


class OdpFileProvider(BaseProvider, FileMixin):
    """ODP file provider.

    Usage example:

        from faker import Faker
        from faker_file.providers.odp_file import OdpFileProvider

        FAKER = Faker()

        file = OdpFileProvider(FAKER).odp_file()

    Usage example with options:

        file = OdpFileProvider(FAKER).odp_file(
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )

    Usage example with `FileSystemStorage` storage (for `Django`):

        from django.conf import settings
        from faker_file.storages.filesystem import FileSystemStorage

        file = OdpFileProvider(FAKER).odp_file(
            storage=FileSystemStorage(
                root_path=settings.MEDIA_ROOT,
                rel_path="tmp",
            ),
            prefix="zzz",
            max_nb_chars=100_000,
            wrap_chars_after=80,
        )
    """

    extension: str = "odp"

    def odp_file(
        self: "OdpFileProvider",
        storage: BaseStorage = None,
        prefix: Optional[str] = None,
        max_nb_chars: int = DEFAULT_TEXT_MAX_NB_CHARS,
        wrap_chars_after: Optional[int] = None,
        content: Optional[str] = None,
        **kwargs,
    ) -> StringValue:
        """Generate an ODP file with random text.

        :param storage: Storage. Defaults to `FileSystemStorage`.
        :param prefix: File name prefix.
        :param max_nb_chars: Max number of chars for the content.
        :param wrap_chars_after: If given, the output string would be separated
             by line breaks after the given position.
        :param content: File content. Might contain dynamic elements, which
            are then replaced by correspondent fixtures.
        :return: Relative path (from root directory) of the generated file.
        """
        # Generic
        if storage is None:
            storage = FileSystemStorage()

        filename = storage.generate_filename(
            prefix=prefix,
            extension=self.extension,
        )

        content = self._generate_text_content(
            max_nb_chars=max_nb_chars,
            wrap_chars_after=wrap_chars_after,
            content=content,
        )

        with BytesIO() as _fake_file:
            pres_doc = OpenDocumentPresentation()
            # We must describe the dimensions of the page
            page_layout = style.PageLayout(name="MyLayout")
            pres_doc.automaticstyles.addElement(page_layout)
            page_layout.addElement(
                style.PageLayoutProperties(
                    margin="0cm",
                    pagewidth="28cm",
                    pageheight="21cm",
                    printorientation="landscape",
                )
            )

            # Every drawing page must have a master page assigned to it.
            master_page = style.MasterPage(
                name="MyMaster", pagelayoutname=page_layout
            )
            pres_doc.masterstyles.addElement(master_page)

            # Style for the title frame of the page
            # We set a centered 34pt font with yellowish background
            title_style = style.Style(
                name="MyMaster-title", family="presentation"
            )
            title_style.addElement(
                style.ParagraphProperties(textalign="center")
            )
            title_style.addElement(style.TextProperties(fontsize="12pt"))
            title_style.addElement(style.GraphicProperties(fillcolor="#ffff99"))
            pres_doc.styles.addElement(title_style)

            # Style for the photo frame
            main_style = style.Style(
                name="MyMaster-main", family="presentation"
            )
            pres_doc.styles.addElement(main_style)

            # Create style for drawing page
            dp_style = style.Style(name="dp1", family="drawing-page")
            pres_doc.automaticstyles.addElement(dp_style)

            page = draw.Page(stylename=dp_style, masterpagename=master_page)
            pres_doc.presentation.addElement(page)

            title_frame = draw.Frame(
                stylename=title_style,
                width="720pt",
                height="56pt",
                x="40pt",
                y="10pt",
            )
            page.addElement(title_frame)
            textbox = draw.TextBox()
            title_frame.addElement(textbox)
            textbox.addElement(P(text=content))
            pres_doc.save(_fake_file)

            storage.write_bytes(filename, _fake_file.getvalue())

        # Generic
        file_name = StringValue(storage.relpath(filename))
        file_name.data = {"content": content}
        return file_name
