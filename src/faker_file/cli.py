import argparse
import inspect
import sys
from copy import deepcopy
from typing import Type

from faker import Faker

from faker_file.base import FileMixin
from faker_file.providers.bin_file import BinFileProvider
from faker_file.providers.csv_file import CsvFileProvider
from faker_file.providers.docx_file import DocxFileProvider
from faker_file.providers.eml_file import EmlFileProvider
from faker_file.providers.epub_file import EpubFileProvider
from faker_file.providers.ico_file import IcoFileProvider
from faker_file.providers.jpeg_file import JpegFileProvider
from faker_file.providers.mp3_file import Mp3FileProvider
from faker_file.providers.odp_file import OdpFileProvider
from faker_file.providers.ods_file import OdsFileProvider
from faker_file.providers.odt_file import OdtFileProvider
from faker_file.providers.pdf_file import PdfFileProvider
from faker_file.providers.png_file import PngFileProvider
from faker_file.providers.pptx_file import PptxFileProvider
from faker_file.providers.rtf_file import RtfFileProvider
from faker_file.providers.svg_file import SvgFileProvider
from faker_file.providers.tar_file import TarFileProvider
from faker_file.providers.txt_file import TxtFileProvider
from faker_file.providers.webp_file import WebpFileProvider
from faker_file.providers.xlsx_file import XlsxFileProvider
from faker_file.providers.zip_file import ZipFileProvider

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


def get_method_kwargs(cls: Type[FileMixin], method_name: str):
    method = getattr(cls, method_name)
    method_specs = inspect.getfullargspec(method)

    kwargs = deepcopy(method_specs.args[1:])  # Omit `self`
    defaults = deepcopy(method_specs.defaults)
    model_props = dict(zip(kwargs, defaults))
    # annotations = deepcopy(method_specs.annotations)
    for kwarg_name in KWARGS_DROP:
        # annotations.pop(kwarg_name, None)
        model_props.pop(kwarg_name, None)

    return model_props


def generate_file(method_name: str, output_dir: str, **kwargs):
    faker = Faker()
    cls = PROVIDERS[method_name]
    method = getattr(cls(faker), method_name)
    value = method(**kwargs)
    # output_file = os.path.join(
    #     output_dir, os.path.basename(value.data["filename"])
    # )
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
        method_kwargs = get_method_kwargs(provider, method_name)
        for arg, default in method_kwargs.items():
            arg_kwargs = {
                "default": default,
                "help": f"{arg} (default: {default})",
            }

            if default is not None:
                arg_kwargs["type"] = type(default)

            subparser.add_argument(f"--{arg}", **arg_kwargs)

    parser.add_argument(
        "-o",
        "--output-dir",
        default=".",
        help="Output directory for the generated files.",
    )
    args = parser.parse_args()

    if args.provider:
        kwargs = {
            k: v
            for k, v in vars(args).items()
            if k not in ("provider", "output_dir")
        }
        output_file = generate_file(args.provider, args.output_dir, **kwargs)
        print(f"Generated {args.provider} file: {output_file}")
    else:
        parser.print_help()
        sys.exit(1)
