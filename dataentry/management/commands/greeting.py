from django.core.management.base import BaseCommand
#proposed command =python mana
class Command(BaseCommand):
    help="Greets the User"

    def add_arguments(self, parser):
        parser.add_argument('name',type=str,help='Specified user name')
    def handle(self,*args,**kwargs):
        #write the logic
        name=kwargs['name']
        greeting=f'Hi {name},Good Morning'
        self.stdout.write(greeting)
        self.stderr.write(greeting)
        self.stdout.write(self.style.SUCCESS(greeting))
        self.stdout.write(self.style.WARNING(greeting))
        