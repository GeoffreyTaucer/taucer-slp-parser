import json
import csv


class App:

    def __init__(self):  # initialize
        self.current_replay = None
        self.settings_path = "settings/settings.csv"
        self.replay_path = ""
        self.set_of_games = []

        self.settings = {
            'Settings path': self.settings_path,
            'Replay path': self.replay_path
        }

    def main(self):
        pass

    def import_saved_settings(self):
        with open(self.settings_path, "r+") as f:
            self.settings = csv.DictReader(f)

    @staticmethod
    def export_settings(settings, location):
        with open(location, "w+") as f:
            w = csv.writer(f)
            for key, value in settings.items():
                w.writerow([key, value])

    def generate_gui(self):  # generate gui
        pass

    @staticmethod
    def import_slp(path):  # import Slippi replay file
        try:
            with open(path, 'r') as f:
                game = f
            return game

        except FileNotFoundError:
            print('Replay file not found')
            return None

    def export_to_slp_parser(self):  # export file to slp-parser-js
        # pass imported file to slp-parser-js
        # import results as json file
        pass

    def parse_json(self):  # parse stats from json file into python-readable format
        pass


if __name__ == '__main__':
    smash = App()
