# Generated by Django 4.2.4 on 2024-06-07 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0002_rename_code_prompt_code_rename_prompt_prompt_prompt_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prompt',
            old_name='code',
            new_name='Code',
        ),
        migrations.RenameField(
            model_name='prompt',
            old_name='prompt',
            new_name='Prompt',
        ),
        migrations.RenameField(
            model_name='prompt',
            old_name='prompt_title',
            new_name='Prompt_title',
        ),
        migrations.RenameField(
            model_name='prompt',
            old_name='summary',
            new_name='Summary',
        ),
        migrations.RenameField(
            model_name='prompt',
            old_name='user',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='prompt',
            old_name='wikipedia_link',
            new_name='Wikipedia_link',
        ),
    ]
