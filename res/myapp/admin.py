from django.contrib import admin
from .models import Person
# Register your models here.
from .models import Details
from .models import Uname

# Register your models here.
admin.site.register(Details)
admin.site.register(Person)
admin.site.register(Uname)