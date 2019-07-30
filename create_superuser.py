import django
import os
#os.environ.setdefault('DJANGO_SETTING_MODULE', 'CopositionServer.settings')
django.setup()

from django.contrib.auth.models import User

u = User(username='ws')
u.set_password('ws1234')
u.is_superuser = True
u.is_staff = True
u.save()