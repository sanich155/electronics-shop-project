import pathlib

BASE_PATH = pathlib.Path(__file__).parent.resolve()

ITEMS_PATH = pathlib.Path(BASE_PATH).joinpath('src', 'items.csv')
