# Generated by Django 2.2.6 on 2019-11-26 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_cms_images', '0001_initial'),
        ('a4_candy_cms_pages', '0004_auto_20191112_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='image',
        ),
        migrations.AddField(
            model_name='homepage',
            name='image_1',
            field=models.ForeignKey(blank=True, help_text='The Image that is shown on top of the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='a4_candy_cms_images.CustomImage', verbose_name='Header Image 1'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image_2',
            field=models.ForeignKey(blank=True, help_text='The Image that is shown on top of the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='a4_candy_cms_images.CustomImage', verbose_name='Header Image 2'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image_3',
            field=models.ForeignKey(blank=True, help_text='The Image that is shown on top of the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='a4_candy_cms_images.CustomImage', verbose_name='Header Image 3'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image_4',
            field=models.ForeignKey(blank=True, help_text='The Image that is shown on top of the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='a4_candy_cms_images.CustomImage', verbose_name='Header Image 4'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image_5',
            field=models.ForeignKey(blank=True, help_text='The Image that is shown on top of the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='a4_candy_cms_images.CustomImage', verbose_name='Header Image 5'),
        ),
    ]
