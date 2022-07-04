import zipfile
import pandas as pd
from django.core.management.base import BaseCommand

from api.models import GlucoseLevel


class Command(BaseCommand):
    help = "populate user glucose values"

    def handle(self, *args, **options):
        path = './sample-data.zip'
        df = self.extract_zip_files(path)
        self.save_data(df)

    @staticmethod
    def extract_zip_files(path):
        df = []
        try:
            with zipfile.ZipFile(path, 'r') as files:
                for file_name in files.namelist():
                    with files.open(file_name, 'r') as file:
                        df = pd.read_csv(file, skiprows=[0]) 
                        df['Aufzeichnungstyp'] = df['Aufzeichnungstyp'].fillna(0).astype(int)
                        df['Glukosewert_verlauf'] = df['Glukosewert-Verlauf mg/dL'].fillna(0).astype(int)
                        df['Glukose_scan'] = df['Glukose-Scan mg/dL'].fillna(0).astype(int)
                        df['Gerätezeitstempel'] = pd.to_datetime(df['Gerätezeitstempel'])
                        df['user_id'] = file_name.split('.')[0]
        except zipfile.BadZipfile as error:
            print(error)
        return df

    @staticmethod
    def save_data(data_frame):
        """
        Save info to database
        """
        df = data_frame.to_dict('records')

        instances = [
            GlucoseLevel(
                user_id=record['user_id'],
                seriennummer=record['Seriennummer'],
                gerätezeitstempel=record['Gerätezeitstempel'],
                aufzeichnungstyp=record['Aufzeichnungstyp'],
                glukosewert_verlauf=record['Glukosewert_verlauf'],
                glukose_scan=record['Glukose_scan'],
            ) 
            for record in df
        ]
        try:
            print('-----inserting data-------')
            GlucoseLevel.objects.bulk_create(instances)
            print('---done------')
        except Exception as error:
            print(f'process terminated -- {error}')
        return
