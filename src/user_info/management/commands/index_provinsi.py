import os
import json
from django.core.management.base import BaseCommand
from user_info.models import Provinsi, KabupatenKota


class Command(BaseCommand):
    help = 'Index Provinsi'

    def handle(self, *args, **options):
        print(f'indexing provinsi... at [{os.getcwd()}]')
        with open(os.path.join(os.getcwd(), 'provinsi.json')) as jsonFile:
            data_provinsi = json.loads(jsonFile.read(), encoding='utf-8').values()
            for _provinsi in data_provinsi:
                provinsi = [x for x in _provinsi.keys()][0]
                provinsi_object = Provinsi.objects.create(text=provinsi)
                provinsi_object.save()
                print('** Provinsi: ', provinsi)
                for _kabupaten in [y for y in _provinsi.values()][0]:
                    kabupaten = _kabupaten if type(_kabupaten) == str else [z for z in _kabupaten.keys()][0]
                    kabupaten_object = KabupatenKota.objects.create(text=kabupaten, provinsi=provinsi_object)
                    kabupaten_object.save()
                    print('-', kabupaten)
