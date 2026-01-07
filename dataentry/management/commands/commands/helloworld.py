from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help="Print Hello World"


    def handle(self,*args,**kwargs):
        # whenever you are creating a function inside a class always try to paass self
        #we write the logic
        #in this way we print the message on terminal
        self.stdout.write("Hello World")
        


