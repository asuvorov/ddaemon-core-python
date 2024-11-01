# Generated by Django 4.2.13 on 2024-09-07 14:52

import ckeditor_uploader.fields
import ddcore.Serializers
import ddcore.models.Attachment
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import django_extensions.db.fields
import django_extensions.db.fields.json
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('custom_data', models.JSONField(blank=True, encoder=ddcore.Serializers.JSONEncoder, null=True, verbose_name='Custom Data')),
                ('is_hidden', models.BooleanField(default=False, help_text='Is Object hidden?', verbose_name='Is hidden?')),
                ('is_private', models.BooleanField(default=False, help_text='Is Object private?', verbose_name='Is private?')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Object deleted?', verbose_name='Is deleted?')),
                ('deleted', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='deleted')),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('created_by', models.ForeignKey(blank=True, help_text='User, created the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deleted_by', models.ForeignKey(blank=True, help_text='User, deleted the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleted_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='User, modified the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
                ('viewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'view',
                'verbose_name_plural': 'views',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('ip', models.CharField(db_index=True, help_text='User IP Address', max_length=16, verbose_name='IP')),
                ('user_agent', models.CharField(blank=True, help_text='User Agent', max_length=128, null=True, verbose_name='User Agent')),
                ('provider', models.CharField(blank=True, help_text='User Internet Provider', max_length=128, null=True, verbose_name='Provider')),
                ('geo_data', django_extensions.db.fields.json.JSONField(blank=True, default=dict, null=True)),
                ('user', models.ForeignKey(help_text='User', on_delete=django.db.models.deletion.CASCADE, related_name='user_login', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'user login',
                'verbose_name_plural': 'user logins',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='TemporaryFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('custom_data', models.JSONField(blank=True, encoder=ddcore.Serializers.JSONEncoder, null=True, verbose_name='Custom Data')),
                ('is_hidden', models.BooleanField(default=False, help_text='Is Object hidden?', verbose_name='Is hidden?')),
                ('is_private', models.BooleanField(default=False, help_text='Is Object private?', verbose_name='Is private?')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Object deleted?', verbose_name='Is deleted?')),
                ('deleted', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='deleted')),
                ('file', models.FileField(upload_to=ddcore.models.Attachment.tmp_directory_path)),
                ('name', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(blank=True, help_text='User, created the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deleted_by', models.ForeignKey(blank=True, help_text='User, deleted the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleted_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='User, modified the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'temporary file',
                'verbose_name_plural': 'temporary files',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('custom_data', models.JSONField(blank=True, encoder=ddcore.Serializers.JSONEncoder, null=True, verbose_name='Custom Data')),
                ('is_hidden', models.BooleanField(default=False, help_text='Is Object hidden?', verbose_name='Is hidden?')),
                ('is_private', models.BooleanField(default=False, help_text='Is Object private?', verbose_name='Is private?')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Object deleted?', verbose_name='Is deleted?')),
                ('deleted', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='deleted')),
                ('social_app', models.CharField(choices=[('--------', '--------'), ('0', 'Facebook'), ('1', 'Twitter'), ('2', 'Linked In'), ('4', 'Google +'), ('8', 'Pinterest'), ('16', 'Instagram'), ('32', 'Tumblr'), ('64', 'YouTube')], default='--------', help_text='Social App', max_length=16, verbose_name='Social App')),
                ('url', models.URLField(blank=True, db_index=True, help_text='Social Link', null=True, verbose_name='url')),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_type_social_links', to='contenttypes.contenttype')),
                ('created_by', models.ForeignKey(blank=True, help_text='User, created the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deleted_by', models.ForeignKey(blank=True, help_text='User, deleted the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleted_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='User, modified the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'social link',
                'verbose_name_plural': 'social links',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('custom_data', models.JSONField(blank=True, encoder=ddcore.Serializers.JSONEncoder, null=True, verbose_name='Custom Data')),
                ('is_hidden', models.BooleanField(default=False, help_text='Is Object hidden?', verbose_name='Is hidden?')),
                ('is_private', models.BooleanField(default=False, help_text='Is Object private?', verbose_name='Is private?')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Object deleted?', verbose_name='Is deleted?')),
                ('deleted', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='deleted')),
                ('rating', models.PositiveIntegerField(db_index=True, default=0)),
                ('review_text', models.TextField(blank=True, help_text='Review Text', null=True, verbose_name='Review Text')),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('created_by', models.ForeignKey(blank=True, help_text='User, created the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deleted_by', models.ForeignKey(blank=True, help_text='User, deleted the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleted_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='User, modified the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'rating',
                'verbose_name_plural': 'ratings',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('custom_data', models.JSONField(blank=True, encoder=ddcore.Serializers.JSONEncoder, null=True, verbose_name='Custom Data')),
                ('is_hidden', models.BooleanField(default=False, help_text='Is Object hidden?', verbose_name='Is hidden?')),
                ('is_private', models.BooleanField(default=False, help_text='Is Object private?', verbose_name='Is private?')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Object deleted?', verbose_name='Is deleted?')),
                ('deleted', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='deleted')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, help_text='Please, use the International Format, e.g. +1-202-555-0114.', max_length=128, null=True, region=None, verbose_name='Phone Number')),
                ('phone_number_ext', models.CharField(blank=True, help_text='Ext.', max_length=8, null=True, verbose_name='Ext.')),
                ('phone_type', models.CharField(blank=True, choices=[('--------', '--------'), ('0', 'Home'), ('1', 'Work'), ('2', 'Mobile'), ('4', 'Google Voice'), ('8', 'Fax')], default='--------', help_text='Phone Type', max_length=16, null=True, verbose_name='Phone Type')),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('created_by', models.ForeignKey(blank=True, help_text='User, created the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deleted_by', models.ForeignKey(blank=True, help_text='User, deleted the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleted_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='User, modified the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'phone number',
                'verbose_name_plural': 'phone numbers',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('custom_data', models.JSONField(blank=True, encoder=ddcore.Serializers.JSONEncoder, null=True, verbose_name='Custom Data')),
                ('is_hidden', models.BooleanField(default=False, help_text='Is Object hidden?', verbose_name='Is hidden?')),
                ('is_private', models.BooleanField(default=False, help_text='Is Object private?', verbose_name='Is private?')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Object deleted?', verbose_name='Is deleted?')),
                ('deleted', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='deleted')),
                ('title', models.CharField(db_index=True, help_text='Newsletter Title', max_length=80, verbose_name='Title')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='Newsletter Content', null=True, verbose_name='Content')),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('author', models.ForeignKey(help_text='Newsletter Author', on_delete=django.db.models.deletion.CASCADE, related_name='sent_newsletters', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('created_by', models.ForeignKey(blank=True, help_text='User, created the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deleted_by', models.ForeignKey(blank=True, help_text='User, deleted the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleted_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='User, modified the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
                ('recipients', models.ManyToManyField(blank=True, related_name='newsletter_recipients', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'newsletter',
                'verbose_name_plural': 'newsletters',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('custom_data', models.JSONField(blank=True, encoder=ddcore.Serializers.JSONEncoder, null=True, verbose_name='Custom Data')),
                ('is_hidden', models.BooleanField(default=False, help_text='Is Object hidden?', verbose_name='Is hidden?')),
                ('is_private', models.BooleanField(default=False, help_text='Is Object private?', verbose_name='Is private?')),
                ('deleted', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='deleted')),
                ('text', models.TextField(help_text='Complaint Text', verbose_name='Text')),
                ('is_processed', models.BooleanField(default=False, help_text='Is Complaint processed?', verbose_name='Is processed?')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Complaint deleted?', verbose_name='Is deleted?')),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('created_by', models.ForeignKey(blank=True, help_text='User, created the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deleted_by', models.ForeignKey(blank=True, help_text='User, deleted the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleted_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='User, modified the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'complaint',
                'verbose_name_plural': 'complaints',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('custom_data', models.JSONField(blank=True, encoder=ddcore.Serializers.JSONEncoder, null=True, verbose_name='Custom Data')),
                ('is_hidden', models.BooleanField(default=False, help_text='Is Object hidden?', verbose_name='Is hidden?')),
                ('is_private', models.BooleanField(default=False, help_text='Is Object private?', verbose_name='Is private?')),
                ('deleted', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='deleted')),
                ('text', models.TextField(help_text='Comment Text', verbose_name='Text')),
                ('is_deleted', models.BooleanField(default=False)),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('created_by', models.ForeignKey(blank=True, help_text='User, created the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deleted_by', models.ForeignKey(blank=True, help_text='User, deleted the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleted_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='User, modified the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='AttachedVideoUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('custom_data', models.JSONField(blank=True, encoder=ddcore.Serializers.JSONEncoder, null=True, verbose_name='Custom Data')),
                ('is_hidden', models.BooleanField(default=False, help_text='Is Object hidden?', verbose_name='Is hidden?')),
                ('is_private', models.BooleanField(default=False, help_text='Is Object private?', verbose_name='Is private?')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Object deleted?', verbose_name='Is deleted?')),
                ('deleted', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='deleted')),
                ('url', models.URLField()),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('created_by', models.ForeignKey(blank=True, help_text='User, created the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deleted_by', models.ForeignKey(blank=True, help_text='User, deleted the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleted_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='User, modified the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'attached video url',
                'verbose_name_plural': 'attached video urls',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='AttachedUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('custom_data', models.JSONField(blank=True, encoder=ddcore.Serializers.JSONEncoder, null=True, verbose_name='Custom Data')),
                ('is_hidden', models.BooleanField(default=False, help_text='Is Object hidden?', verbose_name='Is hidden?')),
                ('is_private', models.BooleanField(default=False, help_text='Is Object private?', verbose_name='Is private?')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Object deleted?', verbose_name='Is deleted?')),
                ('deleted', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='deleted')),
                ('url', models.URLField()),
                ('title', models.CharField(blank=True, db_index=True, help_text='URL Title', max_length=255, null=True, verbose_name='Title')),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('created_by', models.ForeignKey(blank=True, help_text='User, created the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deleted_by', models.ForeignKey(blank=True, help_text='User, deleted the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleted_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='User, modified the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'attached url',
                'verbose_name_plural': 'attached urls',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='AttachedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('custom_data', models.JSONField(blank=True, encoder=ddcore.Serializers.JSONEncoder, null=True, verbose_name='Custom Data')),
                ('is_hidden', models.BooleanField(default=False, help_text='Is Object hidden?', verbose_name='Is hidden?')),
                ('is_private', models.BooleanField(default=False, help_text='Is Object private?', verbose_name='Is private?')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Object deleted?', verbose_name='Is deleted?')),
                ('deleted', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='deleted')),
                ('name', models.CharField(blank=True, db_index=True, help_text='File Name', max_length=255, null=True, verbose_name='Name')),
                ('image', models.ImageField(upload_to=ddcore.models.Attachment.attachment_image_directory_path)),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('created_by', models.ForeignKey(blank=True, help_text='User, created the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deleted_by', models.ForeignKey(blank=True, help_text='User, deleted the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleted_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='User, modified the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'attached image',
                'verbose_name_plural': 'attached images',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='AttachedDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('custom_data', models.JSONField(blank=True, encoder=ddcore.Serializers.JSONEncoder, null=True, verbose_name='Custom Data')),
                ('is_hidden', models.BooleanField(default=False, help_text='Is Object hidden?', verbose_name='Is hidden?')),
                ('is_private', models.BooleanField(default=False, help_text='Is Object private?', verbose_name='Is private?')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Object deleted?', verbose_name='Is deleted?')),
                ('deleted', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='deleted')),
                ('name', models.CharField(blank=True, db_index=True, help_text='File Name', max_length=255, null=True, verbose_name='Name')),
                ('document', models.FileField(upload_to=ddcore.models.Attachment.attachment_document_directory_path)),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('created_by', models.ForeignKey(blank=True, help_text='User, created the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deleted_by', models.ForeignKey(blank=True, help_text='User, deleted the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleted_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='User, modified the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'attached document',
                'verbose_name_plural': 'attached documents',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('custom_data', models.JSONField(blank=True, encoder=ddcore.Serializers.JSONEncoder, null=True, verbose_name='Custom Data')),
                ('is_hidden', models.BooleanField(default=False, help_text='Is Object hidden?', verbose_name='Is hidden?')),
                ('is_private', models.BooleanField(default=False, help_text='Is Object private?', verbose_name='Is private?')),
                ('is_deleted', models.BooleanField(default=False, help_text='Is Object deleted?', verbose_name='Is deleted?')),
                ('deleted', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, null=True, verbose_name='deleted')),
                ('address_1', models.CharField(blank=True, db_index=True, help_text='Address Line #1', max_length=80, null=True, verbose_name='Address Line #1')),
                ('address_2', models.CharField(blank=True, db_index=True, help_text='Address Line #2', max_length=80, null=True, verbose_name='Address Line #2')),
                ('city', models.CharField(blank=True, db_index=True, help_text='City', max_length=80, null=True, verbose_name='City')),
                ('zip_code', models.CharField(blank=True, db_index=True, help_text='Zip/Postal Code', max_length=80, null=True, verbose_name='Zip/Postal Code')),
                ('province', models.CharField(blank=True, db_index=True, help_text='State/Province', max_length=80, null=True, verbose_name='State/Province')),
                ('country', django_countries.fields.CountryField(db_index=True, help_text='Country', max_length=2, verbose_name='Country')),
                ('notes', models.TextField(blank=True, help_text='Here you can provide additional Notes, Directions, and any other Advice, regarding the Location.', null=True, verbose_name='Notes')),
                ('object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('content_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('created_by', models.ForeignKey(blank=True, help_text='User, created the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('deleted_by', models.ForeignKey(blank=True, help_text='User, deleted the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_deleted_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by')),
                ('modified_by', models.ForeignKey(blank=True, help_text='User, modified the Object.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_modified_%(class)s', to=settings.AUTH_USER_MODEL, verbose_name='Modified by')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
                'ordering': ['-id'],
            },
        ),
    ]
