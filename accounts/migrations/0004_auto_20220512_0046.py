# Generated by Django 4.0.4 on 2022-05-12 00:46
from django.db import migrations

def populate_language(apps,schemaeditor):
    languages=[
        {
           "key":"EN",
            "name":"English"
        },
        {
           "key":"ES",
            "name":"Espanol"
        },
        {
           "key":"DE",
            "name":"Deutsch"
        },
        {
           "key":"PT",
            "name":"Portuguese"
        }
    ]

    Language = apps.get_model('accounts','Language')
    for lan in languages:
        key=lan.get('key')
        name=lan.get('name')
        la=Language(key=key,name=name)
        la.save()




class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_language_customuser_preferred_language'),
    ]

    operations = [ 
   
        migrations.RunPython(populate_language),
    ]
