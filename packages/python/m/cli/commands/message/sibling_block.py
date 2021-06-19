import inspect


def add_parser(sub_parser, raw):
    desc = """close and immediately open another block"""
    parser = sub_parser.add_parser(
        'sibling_block',
        help='close and open a sibling block',
        formatter_class=raw,
        description=inspect.cleandoc(desc)
    )
    add = parser.add_argument
    add('to_close', type=str, help='block name to close')
    add('name', type=str, help='block name to open')
    add('description', type=str, help='new block description')


def run(arg):
    # pylint: disable=import-outside-toplevel
    from m.core.io import CiTool
    CiTool.close_block(arg.to_close)
    CiTool.open_block(arg.name, arg.description)
    return 0
