from django.contrib import admin

# Register your models here.
from .models import Composite,ProblemRecord,Problem,User,GoodAnswer

admin.site.register(Composite)
admin.site.register(ProblemRecord)
admin.site.register(Problem)
admin.site.register(User)
admin.site.register(GoodAnswer)