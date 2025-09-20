# I want to add some data to the database using the custom Command
from django.core.management.base import BaseCommand
from dataentry.models import Students
class Command (BaseCommand):
    help="Add some data to the database"

    def handle(self,*args,**kwargs):
        #logic goes here
         #add 1 data
         dataset=[
              {'roll_no':1002,'name':'Sachin','age':21},
              {'roll_no':1003,'name':'Prashant','age':22},
              {'roll_no':1004,'name':'Kaushar','age':23},
              {'roll_no':1005,'name':'joseph','age':23}
         ] 
         for data in dataset:
            #   print(data['name']) 
            roll_no=data['roll_no']
            existing_record=Students.objects.filter(roll_no=roll_no).exists()
            if not existing_record:
                Students.objects.create(roll_no = data['roll_no'],name=data['name'],age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll no {roll_no} Already Exists'))

            
         self.stdout.write(self.style.SUCCESS('Data Inserted Successfully!'))
