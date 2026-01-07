import csv
from django.core.management.base import BaseCommand
from dataentry.models import Students,Customer
import datetime

#proposed command =python manage.py exportdata

class Command(BaseCommand):
    help="Export Data from Student model to a CSV file"
    def handle(self,*args,**kwargs):
        #fetch the data from the database
         students=Students.objects.all()
        #  print(students)
        #generate the timestamp of current date and time
         timestamp=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")





        #define the CSV file name/path
         file_path=f'exported_students_data_{timestamp}.csv'
         print(file_path)



        # Open the CSV file and write the Data 
         with open(file_path,'w',newline='') as file:
                  writer=csv.writer(file)
                  #write the CSV header
                  writer.writerow(['Roll No','Name','Age'])

                  # wrute datarows
                  for student in students:
                        writer.writerow([student.roll_no,student.name,student.age])
         self.stdout.write(self.style.SUCCESS('Data exported Successfully!'))                
