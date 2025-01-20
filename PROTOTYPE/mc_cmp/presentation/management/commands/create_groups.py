from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create user groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Create groups
        caregiver_group, created = Group.objects.get_or_create(name='Caregiver')
        elder_group, created = Group.objects.get_or_create(name='Elder')
        admin_group, created = Group.objects.get_or_create(name='Admin')
        patient_group, created = Group.objects.get_or_create(name='Patient')

        # Assign permissions to groups
        content_type = ContentType.objects.get_for_model(User)
        permission = Permission.objects.get(
            codename='add_user',
            content_type=content_type,
        )
        admin_group.permissions.add(permission)

        permission = Permission.objects.get(
            codename = 'change_user',
            content_type = content_type,
        )
        admin_group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Groups and permissions created successfully'))
