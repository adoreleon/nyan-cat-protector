# -*- coding: utf-8 -*-
import configparser
import os


class ConfigLoader:
    config_file = ""
    config_data = None

    def __init__(self, config_file="config.ini"):
        self.config_file = config_file

        self._load_configs()

    def _load_configs(self):
        self.config_data = configparser.ConfigParser()
        self.config_data.read_file(open(self.config_file, encoding="utf-8"))

    def get_sound_file_path(self):
        return "audio_file/airport_message.mp3"
        # return self.config_data["AUDIO"]["audio_file"]

    def get_git_service_name(self):
        return self.config_data["BASE"]["git_service"]

    def get_check_sleep_time(self):
        return self.config_data["BASE"]["sleep_time"]

    def get_tts_text(self):
        return self.config_data["TTS"]["speech_text"]

    def get_tts_language(self):
        return self.config_data["TTS"]["language"]

    def get_value(self, block, key):
        return self.config_data[block.upper()][key]
