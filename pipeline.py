from abc import abstractmethod

from pygame import mixer


class GitBuilder:
    @staticmethod
    def get_class_by_name(name):
        if name.lower() == "bitbucket":
            return BitbucketPipeline


class BasePipeline:
    config = None
    mixer = None

    def __init__(self, config):
        self.config = config

        self._load_mixer()

    @abstractmethod
    def is_build_broken(self):
        pass

    def _load_mixer(self):
        self.mixer = mixer.init()

        sound_path = self.config.get_sound_path()
        mixer.music.load(sound_path)

    def check_build(self):
        if self.is_build_broken():
            self.play_sound()

    def play_sound(self):
        mixer.music.play()


class BitbucketPipeline(BasePipeline):
    pass
