import inspect
from ...utils import call_main


def add_parser(sub_parser, raw):
    desc = """
        Display the very first commit sha in the repository.

            $ m git first_sha
            bf286e270e13c75dfed289a3921289092477c058
    """
    sub_parser.add_parser(
        'first_sha',
        help='display the first commit sha',
        formatter_class=raw,
        description=inspect.cleandoc(desc)
    )


def run(_arg):
    from m import git
    return call_main(git.get_first_commit_sha, [], print_raw=True)

