from django.core.management.base import BaseCommand,CommandError
# from dataentry.models import Students
from django.apps import apps
import csv

# Proposed Command -Python Manage.py importdata file_path
class Command(BaseCommand):
    help='Import data from CSV file'

    def add_arguments(self,parser):
        parser.add_argument('file_path',type=str,help='Path to the CSV file')
        parser.add_argument('model_name',type=str,help='Name of the model')



    def handle(self,*args,**kwargs):
        #logic goes here
        file_path=kwargs['file_path']
        model_name=kwargs['model_name'].capitalize()

        # Search for the model across all installed apps
        model=None
        for app_config in apps.get_app_configs():
            #Try to search for the model
            try:
                model=apps.get_model(app_config.label,model_name)
                break
            #stop searching once the model is found
            except LookupError:
                continue #searching (model not found in this app, continue searching in this next app)
        if not model:
            raise CommandError(f'Model"{model_name}" not found in any app!')
        







        # print(file_path,'r')
        with open(file_path,'r')as file:
            reader=csv.DictReader(file)
            # print(reader)
            for row in reader:
                print(row)
                model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data inserted Successfully!'))