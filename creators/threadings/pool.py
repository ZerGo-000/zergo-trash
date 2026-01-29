import os

from creators.threadings.worker import Worker


class PoolWorkers:
    count_threads = (os.cpu_count() or 4) * 3

    @staticmethod
    def start():
        PoolWorkers.__create_threads()

    @staticmethod
    def __create_threads():
        threads = []
        for _ in range(PoolWorkers.count_threads):
            w = Worker()
            w.start()
            threads.append(w)

        for thread in threads:
            thread.join()
