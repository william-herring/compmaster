from django.contrib import admin
from .models import Competition, Round, Group, Station

# Register your models here.
admin.site.register(Competition)
admin.site.register(Round)
admin.site.register(Group)
admin.site.register(Station)