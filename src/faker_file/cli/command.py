import argparse
import sys
import typing

from .. import __version__

__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = ("main",)


def main():
    try:
        from .helpers import (
            PROVIDERS,
            generate_completion_file,
            generate_file,
            get_method_kwargs,
            is_optional_type,
        )
    except ImportError:
        print("You need to pip install faker-file[common] to use the CLI")
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description="CLI for the faker-file package."
    )
    subparsers = parser.add_subparsers(
        dest="command", help="Available file providers."
    )

    # Add generate-completion subparser
    __generate_completion_subparser = subparsers.add_parser(
        "generate-completion",
        help="Generate bash completion file.",
    )

    # Add version subparser
    __version_subparser = subparsers.add_parser(
        "version",
        help="Print version.",
    )

    for method_name, provider in PROVIDERS.items():
        subparser = subparsers.add_parser(
            method_name,
            help=f"Generate a {method_name.split('_file')[0]} file.",
        )
        method_kwargs, annotations = get_method_kwargs(provider, method_name)
        for arg, default in method_kwargs.items():
            arg_type = annotations[arg]
            arg_kwargs = {
                "default": default,
                "help": f"{arg} (default: {default})",
                "type": (
                    arg_type.__args__[0]
                    if isinstance(arg_type, typing._GenericAlias)
                    and is_optional_type(arg_type)
                    else arg_type
                ),
            }

            subparser.add_argument(f"--{arg}", **arg_kwargs)

        # Add the optional num_files argument
        subparser.add_argument(
            "--nb_files",
            default=1,
            type=int,
            help="number of files to generate (default: 1)",
        )

    args = parser.parse_args()

    if args.command == "generate-completion":
        generate_completion_file()
    elif args.command == "version":
        print(__version__)
    elif args.command:
        kwargs = {k: v for k, v in vars(args).items() if k not in ("command",)}
        for counter in range(args.nb_files):
            output_file = generate_file(args.command, **kwargs)
            print(
                f"Generated {args.command} file "
                f"({counter+1} of {args.nb_files}): "
                f"{output_file.data['filename']}"
            )
    else:
        parser.print_help()
        sys.exit(1)
