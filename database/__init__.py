from . import load
__all__ = ['__database__']
__database__ = load.database(filter=False)
__DB_path__ = "database\\database.csv"