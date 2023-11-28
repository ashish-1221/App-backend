from django.contrib import admin
from .models import VillageMappingFile,State
from import_export.admin import ImportExportModelAdmin,ImportMixin
from .forms import *
from .resource import *


# Register your models here.
class VillageMappingFileAdmin(ImportExportModelAdmin,ImportMixin):
    list_display = ["state","ac_no","object_id","name","locality","booth","probable_nearby_vil_voter"]
    list_filter = ["state"]
    # import_form_class = CustomImportForm
    # export_form_class = CustomExportForm
    # confirm_form_class = CustomConfirmImportForm
    resource_classes = [VillageMappingFileResource]
    # print("Inside VillageMappingFileAdmin")
     
    # def get_confirm_form_initial(self, request, import_form):
    #     initial = super().get_confirm_form_initial(request, import_form)
    #     if import_form:
    #         initial['state'] = import_form.cleaned_data['state']
    #     return initial
    

    
    # def get_import_data_kwargs(self, request, *args, **kwargs):
    #     form = kwargs.get('form')
    #     print(form.cleaned_data['state'])
    #     if form:
    #         kwargs.pop('form')
            
    #         if 'state' in form.cleaned_data:
    #             return {"state": form.cleaned_data["state"]}
    #         return kwargs
    #     return {}
    
    # def get_export_resource_kwargs(self, request, *args, **kwargs):
    #         export_form = kwargs["export_form"]
    #         if export_form:
    #             return dict(state_id=export_form.cleaned_data["state"].id)
    #         return {}

    

    
        



    
admin.site.register(VillageMappingFile,VillageMappingFileAdmin)
admin.site.register(State)
admin.site.register(VillageLocalityModel)