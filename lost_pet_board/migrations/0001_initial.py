# Generated by Django 3.2.12 on 2022-03-28 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lost_pet_board.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LostPetBoard',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lost_board_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('pet_name', models.CharField(max_length=20)),
                ('breed', models.TextField()),
                ('size', models.CharField(max_length=10)),
                ('lost_location', models.TextField()),
                ('lost_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-lost_board_no'],
            },
        ),
        migrations.CreateModel(
            name='LostPetBoardImage',
            fields=[
                ('lost_image_no', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='', validators=[lost_pet_board.models.validate_image])),
                ('lost_board_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_image', to='lost_pet_board.lostpetboard')),
            ],
            options={
                'ordering': ['-lost_image_no'],
            },
        ),
        migrations.CreateModel(
            name='LostPetBoardComment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lost_comment_no', models.AutoField(primary_key=True, serialize=False)),
                ('comment_content', models.TextField()),
                ('lost_board_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lost_pet_board.lostpetboard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-lost_comment_no'],
            },
        ),
    ]
