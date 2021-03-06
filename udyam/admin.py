from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import * #import models


class ParticipantResource(resources.ModelResource):

    class Meta:
        model = RegistrationInfo

class ParticipantAdmin(ImportExportModelAdmin):
    resource_class = ParticipantResource
    list_filter = ['event_name']
    pass

# class RegisterAdmin(admin.ModelAdmin):
#     model = RegistrationInfo
#     list_filter = ['event_name']

admin.site.register(RegistrationInfo, ParticipantAdmin)
