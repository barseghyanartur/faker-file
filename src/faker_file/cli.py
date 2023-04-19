import argparse
import inspect
import sys
import typing
from copy import deepcopy
from typing import Any, Dict, Tuple, Type

from faker import Faker

from .base import FileMixin, StringValue
from .providers.bin_file import BinFileProvider
from .providers.csv_file import CsvFileProvider
from .providers.docx_file import DocxFileProvider
from .providers.eml_file import EmlFileProvider
from .providers.epub_file import EpubFileProvider
from .providers.ico_file import IcoFileProvider
from .providers.jpeg_file import JpegFileProvider
from .providers.mp3_file import Mp3FileProvider
from .providers.odp_file import OdpFileProvider
from .providers.ods_file import OdsFileProvider
from .providers.odt_file import OdtFileProvider
from .providers.pdf_file import PdfFileProvider
from .providers.png_file import PngFileProvider
from .providers.pptx_file import PptxFileProvider
from .providers.rtf_file import RtfFileProvider
from .providers.svg_file import SvgFileProvider
from .providers.tar_file import TarFileProvider
from .providers.txt_file import TxtFileProvider
from .providers.webp_file import WebpFileProvider
from .providers.xlsx_file import XlsxFileProvider
from .providers.zip_file import ZipFileProvider

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = [
    "main",
    "get_method_kwargs",
    "generate_file",
]

KWARGS_DROP = {
    "self",  # Drop as irrelevant
    "storage",  # Drop as non-supported arg
    "return",  # Drop as irrelevant
    "mp3_generator_cls",  # Drop as non-supported arg
    # "mp3_generator_kwargs",  # Drop as non-supported arg
    "pdf_generator_cls",  # Drop as non-supported arg
    # "pdf_generator_kwargs",  # Drop as non-supported arg
    "raw",  # Drop `raw`, because we will be forcing raw=True for streaming
}
PROVIDERS = {
    BinFileProvider.bin_file.__name__: BinFileProvider,
    CsvFileProvider.csv_file.__name__: CsvFileProvider,
    DocxFileProvider.docx_file.__name__: DocxFileProvider,
    EmlFileProvider.eml_file.__name__: EmlFileProvider,
    EpubFileProvider.epub_file.__name__: EpubFileProvider,
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
    ZipFileProvider.zip_file.__name__: ZipFileProvider,
}


def get_method_kwargs(
    cls: Type[FileMixin], method_name: str
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    method = getattr(cls, method_name)
    method_specs = inspect.getfullargspec(method)

    kwargs = deepcopy(method_specs.args[1:])  # Omit `self`
    defaults = deepcopy(method_specs.defaults)
    model_props = dict(zip(kwargs, defaults))
    annotations = deepcopy(method_specs.annotations)
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


def main():
    parser = argparse.ArgumentParser(
        description="CLI for the faker-file package."
    )
    subparsers = parser.add_subparsers(
        dest="provider", help="Available file providers."
    )

    for method_name, provider in PROVIDERS.items():
        subparser = subparsers.add_parser(
            method_name,
            help=f"Generate a {method_name.split('_file')[0]} file.",
        )
        method_kwargs, annotations = get_method_kwargs(provider, method_name)
        for arg, default in method_kwargs.items():
            _arg_type = annotations[arg]
            arg_kwargs = {
                "default": default,
                "help": f"{arg} (default: {default})",
                "type": (
                    annotations[arg].__args__[0]
                    if isinstance(_arg_type, typing._GenericAlias)
                    and _arg_type._name == "Optional"
                    else _arg_type
                ),
            }

            subparser.add_argument(f"--{arg}", **arg_kwargs)

    args = parser.parse_args()

    if args.provider:
        kwargs = {k: v for k, v in vars(args).items() if k not in ("provider",)}
        output_file = generate_file(args.provider, **kwargs)
        print(f"Generated {args.provider} file: {output_file}")
    else:
        parser.print_help()
        sys.exit(1)
