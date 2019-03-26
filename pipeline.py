from abc import abstractmethod

from pygame import mixer


class GitBuilder:
    @staticmethod
    def get_class_by_name(name):
        if name.lower() == "bitbucket":
            return BitbucketPipeline


class BasePipeline:
    mixer = None
    is_broken = False
    played_sound = False

    def __init__(self, sound_file_path):
        self.mixer = mixer.init()
        mixer.music.load(sound_file_path)

    @abstractmethod
    def check_pipeline_is_broken(self):
        pass

    def is_build_broken(self):
        if self.check_pipeline_is_broken():
            self.is_broken = True
        else:
            self.is_broken = self.played_sound = False

    def check_build(self):
        if self.is_build_broken():
            self.play_sound()

    def play_sound(self):
        if not self.played_sound:
            self.played_sound = True
            mixer.music.play()


class BitbucketPipeline(BasePipeline):
    pass
