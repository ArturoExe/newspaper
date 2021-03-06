# Generated by Django 4.0.4 on 2022-05-11 05:07
from django.db import migrations


def populate_usertype(apps,schemaeditor):
    user_types={
        "reader":"A subscriber",
        "journalist":"A staff member content creator",
        "editor":"A staff member editor"
    }

    UserType = apps.get_model('accounts','UserType')
    for name,desc in user_types.items():
        user_type = UserType(name=name,description=desc)
        user_type.save()




class Migration(migrations.Migration):

    dependencies = [
        
    ]

    operations = [

        migrations.RunPython(populate_usertype),

    ]
