#!/usr/bin/python3
"""Instantiaites a storage abstraction.

-> if the environmenetal variable 'HBNB_TYPE_STORAGE' is set to 'db'
instantiates a new database storage engine (DBStorage)
-> otherwise, instantiates a file storage engine (FileStorage)
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
