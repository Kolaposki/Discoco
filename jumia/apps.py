from django.apps import AppConfig


class JumiaConfig(AppConfig):
    name = 'jumia'

    def ready(self):
        from .scraper_tools import updater
        updater.start()
