import os
from pathlib import Path
from queue import Queue
from typing import List

from creators.threadings.pool import PoolWorkers
from creators.configs.create_queue import FileQueue


class SystemConfiguration:
    files: Queue[str]
    dir_list: List[str]

    @staticmethod
    def start():
        SystemConfiguration.__change_dir()
        FileQueue.start()
        SystemConfiguration.__create_pool_worker()

    @staticmethod
    def __change_dir():
        os.chdir(f"{Path.home()}/Trash/")

    @classmethod
    def __create_pool_worker(cls):
        PoolWorkers.start()
