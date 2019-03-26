# -*- coding: utf-8 -*-
from time import sleep

from config import ConfigLoader
from pipeline import GitBuilder


class App:
    config = None
    git_class = None

    def start(self):
        self.config = ConfigLoader()

        git_class = GitBuilder.get_class_by_name(self.config.get_git_service_name())
        self.git_class = git_class(self.config.get_sound_file_path(), self.config)

        self.watch_pipeline()

    def watch_pipeline(self):
        while True:
            self.git_class.check_build()

            sleep(self.config.get_check_sleep_time())


if __name__ == '__main__':
    App().start()
