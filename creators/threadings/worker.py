import os
import subprocess
from threading import Lock, Thread

from creators.configs.create_queue import FileQueue
from creators.configs.required_data import CATEGORIES

folder_lock = Lock()


class Worker(Thread):
    def run(self):
        Worker.__move_file()

    @staticmethod
    def __move_file():
        while True:
            if FileQueue.files.empty():
                break

            file = FileQueue.files.get()
            current_extension = os.path.splitext(file)[1]
            path_file = os.path.abspath(file)

            with folder_lock:
                if not current_extension and file in CATEGORIES:
                    if os.path.isdir(file):
                        continue

                elif not current_extension and file not in CATEGORIES:
                    if os.path.isdir(file):
                        command = f"mv {path_file} Dirs"
                        subprocess.run(command.split())
                    else:
                        command = f"mv {path_file} Other"
                        subprocess.run(command.split())
                else:
                    flag = False
                    for category, extension in CATEGORIES.items():
                        if current_extension in extension:
                            command = f"mv {path_file} {os.path.abspath(category)}"
                            subprocess.run(command.split())
                            flag = False
                            break
                        flag = True

                    if flag:
                        name_dir = current_extension.replace(".", "").upper()
                        new_dir = os.path.abspath("Other/" + name_dir)
                        os.makedirs(new_dir, exist_ok=True)
                        command = f"mv {path_file} {new_dir}"
                        subprocess.run(command.split())
