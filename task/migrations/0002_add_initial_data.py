from django.db import migrations

def add_initial_data(apps, schema_editor):
    Country = apps.get_model('task', 'Country')
    # state = apps.get_model('task', 'state')
    City = apps.get_model('task', 'City')


    # india = Country.objects.create(name='India')
    # City.objects.create(name='Bengaluru', country=india)
    # City.objects.create(name='Mumbai', country=india)
    # City.objects.create(name='Chennai', country=india)
    # City.objects.create(name='Hyderabad', country=india)
    # City.objects.create(name='New Delhi', country=india)

    # usa = Country.objects.create(name='United States')
    # City.objects.create(name='New York', country=usa)
    # City.objects.create(name='San Francisco', country=usa)
    # City.objects.create(name='Los Angeles', country=usa)
    # City.objects.create(name='Chicago', country=usa)
    # City.objects.create(name='Seattle', country=usa)

    # russia = Country.objects.create(name='Russia')
    # City.objects.create(name='Moscow', country=russia)
    # City.objects.create(name='Saint Petersburg', country=russia)
    # City.objects.create(name='Yekaterinburg', country=russia)
    # City.objects.create(name='Kazan', country=russia)
    # City.objects.create(name='Krasnodar', country=russia)

    # brazil = Country.objects.create(name='Brazil')
    # City.objects.create(name='Sao Paulo', country=brazil)
    # City.objects.create(name='Rio de Janeiro', country=brazil)
    # City.objects.create(name='Belo Horizonte', country=brazil)
    # City.objects.create(name='Curitiba', country=brazil)
    # City.objects.create(name='Recife', country=brazil)


    # india = Country.objects.create(name='India')
    # City.objects.create(name='MP', country=india)
    # City.objects.create(name='UP', country=india)
   
    
    # MP= State.objects.create(name='indore', country=india)
    # MP= State.objects.create(name='Bhopal', country=india)

    # UP= State.objects.create(name='A', country=india)
    # UP= State.objects.create(name='B', country=india)

    # usa = Country.objects.create(name='United States')
    # City.objects.create(name='New York', country=usa)
    # City.objects.create(name='San Francisco', country=usa)

    # New_York= State.objects.create(name='p', country=usa)
    # New_York= State.objects.create(name='q', country=usa)

    # San_Francisco= State.objects.create(name='r', country=usa)
    # San_Francisco= State.objects.create(name='s', country=usa)


    # russia = Country.objects.create(name='Russia')
    # City.objects.create(name='Moscow', country=russia)
    # City.objects.create(name='Saint Petersburg', country=russia)
   
class Migration(migrations.Migration):
    dependencies = [
        ('task', '0001_initial'),
    ]
   #  operations = [
   #      migrations.RunPython(add_initial_data),
   #  ]
   # 