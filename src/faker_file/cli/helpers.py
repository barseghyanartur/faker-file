import inspect
import os
import typing
from copy import deepcopy
from typing import Any, Dict, Tuple, Type

from faker import Faker

from ..base import FileMixin, StringValue
from ..providers.bin_file import BinFileProvider
from ..providers.csv_file import CsvFileProvider
from ..providers.docx_file import DocxFileProvider
from ..providers.eml_file import EmlFileProvider
from ..providers.epub_file import EpubFileProvider
from ..providers.generic_file import GenericFileProvider
from ..providers.ico_file import GraphicIcoFileProvider, IcoFileProvider
from ..providers.jpeg_file import GraphicJpegFileProvider, JpegFileProvider
from ..providers.mp3_file import Mp3FileProvider
from ..providers.odp_file import OdpFileProvider
from ..providers.ods_file import OdsFileProvider
from ..providers.odt_file import OdtFileProvider
from ..providers.pdf_file import GraphicPdfFileProvider, PdfFileProvider
from ..providers.png_file import GraphicPngFileProvider, PngFileProvider
from ..providers.pptx_file import PptxFileProvider
from ..providers.rtf_file import RtfFileProvider
from ..providers.svg_file import SvgFileProvider
from ..providers.tar_file import TarFileProvider
from ..providers.txt_file import TxtFileProvider
from ..providers.webp_file import GraphicWebpFileProvider, WebpFileProvider
from ..providers.xlsx_file import XlsxFileProvider
from ..providers.xml_file import XmlFileProvider
from ..providers.zip_file import ZipFileProvider

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "generate_completion_file",
    "generate_file",
    "get_method_kwargs",
    "is_optional_type",
    "PROVIDERS",
)

KWARGS_DROP = {
    "self",  # Drop as irrelevant
    "storage",  # Drop as non-supported arg
    "return",  # Drop as irrelevant
    # "mp3_generator_cls",  # Drop as non-supported arg
    # "mp3_generator_kwargs",  # Drop as non-supported arg
    # "pdf_generator_cls",  # Drop as non-supported arg
    # "pdf_generator_kwargs",  # Drop as non-supported arg
    "format_func",  # Drop as non-supported arg
    "raw",  # Drop `raw`, because we will be forcing raw=True for streaming
}
OVERRIDES = {
    "DocxFileProvider.docx_file": {
        "annotations": {
            "content": str,
        },
        "model_props": {
            "content": None,
        },
    },
    "GenericFileProvider.generic_file": {
        "annotations": {
            "content": str,
        },
        "model_props": {},
    },
    "Mp3FileProvider.mp3_file": {
        "annotations": {
            "mp3_generator_cls": str,
        },
        "model_props": {
            "mp3_generator_cls": (
                "faker_file.providers.mp3_file.generators"
                ".gtts_generator.GttsMp3Generator"
            ),
        },
    },
    "OdtFileProvider.odt_file": {
        "annotations": {
            "content": str,
        },
        "model_props": {
            "content": None,
        },
    },
    "PdfFileProvider.pdf_file": {
        "annotations": {
            "pdf_generator_cls": str,
        },
        "model_props": {
            "pdf_generator_cls": (
                "faker_file.providers.pdf_file.generators"
                ".pdfkit_generator.PdfkitPdfGenerator"
            ),
        },
    },
}
PROVIDERS = {
    BinFileProvider.bin_file.__name__: BinFileProvider,
    CsvFileProvider.csv_file.__name__: CsvFileProvider,
    DocxFileProvider.docx_file.__name__: DocxFileProvider,
    EmlFileProvider.eml_file.__name__: EmlFileProvider,
    EpubFileProvider.epub_file.__name__: EpubFileProvider,
    GenericFileProvider.generic_file.__name__: GenericFileProvider,
    GraphicIcoFileProvider.graphic_ico_file.__name__: GraphicIcoFileProvider,
    GraphicJpegFileProvider.graphic_jpeg_file.__name__: (
        GraphicJpegFileProvider
    ),
    GraphicPdfFileProvider.graphic_pdf_file.__name__: GraphicPdfFileProvider,
    GraphicPngFileProvider.graphic_png_file.__name__: GraphicPngFileProvider,
    GraphicWebpFileProvider.graphic_webp_file.__name__: (
        GraphicWebpFileProvider
    ),
    IcoFileProvider.ico_file.__name__: IcoFileProvider,
    JpegFileProvider.jpeg_file.__name__: JpegFileProvider,
    Mp3FileProvider.mp3_file.__name__: Mp3FileProvider,
    OdpFileProvider.odp_file.__name__: OdpFileProvider,
    OdsFileProvider.ods_file.__name__: OdsFileProvider,
    OdtFileProvider.odt_file.__name__: OdtFileProvider,
    PdfFileProvider.pdf_file.__name__: PdfFileProvider,
    PngFileProvider.png_file.__name__: PngFileProvider,
    PptxFileProvider.pptx_file.__name__: PptxFileProvider,
    RtfFileProvider.rtf_file.__name__: RtfFileProvider,
    SvgFileProvider.svg_file.__name__: SvgFileProvider,
    TarFileProvider.tar_file.__name__: TarFileProvider,
    TxtFileProvider.txt_file.__name__: TxtFileProvider,
    WebpFileProvider.webp_file.__name__: WebpFileProvider,
    XlsxFileProvider.xlsx_file.__name__: XlsxFileProvider,
    XmlFileProvider.xml_file.__name__: XmlFileProvider,
    ZipFileProvider.zip_file.__name__: ZipFileProvider,
}


def get_method_kwargs(
    cls: Type[FileMixin], method_name: str
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    method = getattr(cls, method_name)
    method_specs = inspect.getfullargspec(method)

    kwargs = deepcopy(method_specs.args[1:])  # Omit `self`
    defaults = deepcopy(method_specs.defaults if method_specs.defaults else [])
    model_props = dict(zip(kwargs, defaults))
    annotations = deepcopy(method_specs.annotations)

    # Override the type definition for mp3_generator_cls
    override = OVERRIDES.get(f"{cls.__name__}.{method_name}", None)
    if override:
        annotations.update(override["annotations"])
        model_props.update(override["model_props"])

    for kwarg_name in KWARGS_DROP:
        annotations.pop(kwarg_name, None)
        model_props.pop(kwarg_name, None)

    return model_props, annotations


def generate_file(method_name: str, **kwargs) -> StringValue:
    faker = Faker()
    cls = PROVIDERS[method_name]
    method = getattr(cls(faker), method_name)
    value = method(**kwargs)
    return value


def is_optional_type(t: Any) -> bool:
    if getattr(t, "__origin__", None) is typing.Union:
        return any(arg is type(None) for arg in t.__args__)  # noqa
    return False


def generate_completion_file():
    completion_script = f"""#!/bin/bash

_faker_file_completion() {{
    local cur prev providers commands
    cur="${{COMP_WORDS[COMP_CWORD]}}"
    prev="${{COMP_WORDS[COMP_CWORD - 1]}}"
    providers="{(' '.join(PROVIDERS.keys()))}"
    commands="generate-completion version"  # Add the commands here

    case $prev in"""

    for method_name, provider in PROVIDERS.items():
        method_kwargs, _ = get_method_kwargs(provider, method_name)
        completion_script += f"""
        {method_name})
            COMPREPLY=($(compgen -W "{(' '.join('--' + k for k in method_kwargs.keys()))} --nb_files" -- "$cur"))
            ;;
        """  # noqa

    # Add the case for commands
    completion_script += """
        generate-completion|version)
            COMPREPLY=()
            ;;
    """

    completion_script += """
        *)
            COMPREPLY=($(compgen -W "$providers $commands" -- "$cur"))
            ;;
    esac

    return 0
}

complete -F _faker_file_completion faker-file
"""

    user_home_dir = os.path.expanduser("~")
    file_path = os.path.join(user_home_dir, "faker_file_completion.sh")
    with open(file_path, "w") as f:
        f.write(completion_script)

    print(f"Generated bash completion file: {file_path}")
