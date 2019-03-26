# -*- coding: utf-8 -*-
from abc import abstractmethod

import requests
import simplejson
from playsound import playsound


class GitBuilder:
    @staticmethod
    def get_class_by_name(name):
        if name.lower() == "bitbucket":
            return BitbucketPipeline


class BasePipeline:
    sound_file_path = ""
    player = None
    config = None
    is_broken = False
    played_sound = False

    def __init__(self, sound_file_path, config, *args, **kwargs):
        self.config = config
        self.sound_file_path = sound_file_path

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
            playsound(self.sound_file_path)


class BitbucketPipeline(BasePipeline):
    base_url = "https://api.bitbucket.org/2.0/repositories/{repository_username}/{repository_name}/pipelines/?sort=-created_on"
    authorization_token = ""
    repo_username = ""
    repo_name = ""
    blammed = ""

    def __init__(self, *args, **kwargs):
        super(BitbucketPipeline, self).__init__(*args, **kwargs)

        self.authorization_token = self.config.get_value(block="bitbucket", key="authorization_key")
        self.repo_username = self.config.get_value(block="bitbucket", key="repository_username")
        self.repo_name = self.config.get_value(block="bitbucket", key="repository_name")

        self.base_url = self.base_url.format(**{
            "repository_username": self.repo_name,
            "repository_name": self.repo_username
        })

    def fetch_pipeline_from_api(self):
        json_response = {}
        response = requests.get(self.base_url, headers={"Authorization": "Basic " + self.authorization_token})

        if response.status_code == 200:
            json_response = simplejson.loads(response.json())

        return json_response

    def process_pipeline_data(self, pipeline_data_list):
        is_broken = False

        for each_pipeline in pipeline_data_list["values"]:
            if each_pipeline["result"]["name"] == "FAILED":
                self.blammed = each_pipeline["creator"]["display_name"]
                is_broken = True
        return is_broken

    def check_pipeline_is_broken(self):
        pipeline_data_list = self.fetch_pipeline_from_api()
        is_broken = self.process_pipeline_data(pipeline_data_list)

        if not is_broken:
            self.blammed = ""

        return is_broken

    def play_sound(self):
        if not self.played_sound:
            self.played_sound = True
            playsound(self.sound_file_path)
            self.TTS_speak({"name": self.blammed})

    def TTS_speak(self, dict_data):
        from google_speech import Speech
        text = self.config.get_tts_text().format(**dict_data)
        lang = self.config.get_tts_language()
        speech = Speech(text, lang)

        sox_effects = ("speed", "1.3")
        speech.play(sox_effects)