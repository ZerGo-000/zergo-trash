import os
from queue import Queue


class FileQueue:
    files: Queue[str] = Queue()

    @staticmethod
    def start():
        FileQueue.__create_data()

    @classmethod
    def __create_data(cls):
        with os.scandir(os.path.abspath(".")) as files:
            for file in files:
                cls.files.put(file.name)
