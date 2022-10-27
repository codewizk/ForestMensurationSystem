
from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import Specie, User, SubCompartmentRegister,PlantingSeason,Project,WorkingCircle,Espacement,Stocking,Specie,FlutterUser
from django.contrib.auth.models import User, Group


class MyUserCreationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    class Meta(UserCreationForm.Meta):
        model = User




class SubCompartmentRegisterAdmin(admin.ModelAdmin):
    model = SubCompartmentRegister
    list_display = ['SubCompartment_Name', 'Compartment_Name','Hectares','Specie','Planting_Year','Project_Name','WorkingCircles','Espacement',]
    search_fields = ('SubCompartment_Name', 'Compartment_Name','Hectares','Specie','Planting_Year','Project_Name','WorkingCircles','Espacement' )
    list_display_links= ('SubCompartment_Name',)
    list_filter= ('Specie','Planting_Year','Project_Name','WorkingCircles')

  

    

class PlantingSeasonAdmin(admin.ModelAdmin):
    model = PlantingSeason
    list_display = ['Planting_Season', ]
    search_fields = ( 'Planting_Season', )

class ProjectsAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['Project_Name',]
    search_fields = ('Project_Name',)

class WorkingCircleAdmin(admin.ModelAdmin):
    model = WorkingCircle
    list_display = ['Usage',]
    search_fields = ('Usage',)

class SpecieAdmin(admin.ModelAdmin):
    model = Specie
    list_display = ['Specie','Vernacular_Name','Standard_Form_Factor', ]
    search_fields = ('Specie','Vernacular_Name','Standard_Form_Factor', )

class EspacementsAdmin(admin.ModelAdmin):
    model = Espacement
    list_display = ['RowSpacing','InterRowSpacing','Espacement', ]
    search_fields = ('RowSpacing','InterRowSpacing','Espacement', )

class StockingAdmin(admin.ModelAdmin):
    model = Stocking
    list_display = ['SubCompartment_Name','Date','Surviving','UserName']
    search_fields = ('SubCompartment_Name', 'Date','Surviving','Dead','UserName')

class StockingReport(SubCompartmentRegister):

    class Meta:
        proxy=True

class filteredlist(admin.SimpleListFilter):
    title ='Blocks Count Filter'
    parameter_name = 'last_Date_Of_Count'
    

    def lookups(self, request,model_admin):

        return (('Blocks Counted','Blocks Counted'),('All Blocks','All Blocks'))

    def queryset(self, request, queryset):
        value = self.value()

        if not self.value():
            return queryset.filter(stocking__gte=0).distinct()

        
        

        elif value == 'Blocks Counted':
            
            
            return queryset.filter(stocking__gte=0).distinct()
        
        

		
    

class StockingReportAdmin(SubCompartmentRegisterAdmin):
    
    list_display = ['SubCompartment_Name','Hectares','Specie','Planting_Year','Stocking_Percentage','last_Date_Of_Count',]
    
     
    search_fields = ('SubCompartment_Name', 'Compartment_Name','Hectares','Specie','Planting_Year','Project_Name','WorkingCircles','Espacement' )
    list_display_links= ('SubCompartment_Name',)
    list_filter= (filteredlist,'Specie','Planting_Year','Project_Name','WorkingCircles',)

    admin_order_field='last_Date_Of_Count'

   
        

    


class UserAdmin(AuthUserAdmin):
    add_form = MyUserCreationForm
    update_form_class = UserChangeForm

class FlutterUserAdmin(admin.ModelAdmin):
    model= FlutterUser
    list_display= ['UserName','Email','Password']

admin.site.register(FlutterUser,FlutterUserAdmin)
admin.site.register(SubCompartmentRegister, SubCompartmentRegisterAdmin,)
admin.site.register(StockingReport, StockingReportAdmin,)
admin.site.register(PlantingSeason,PlantingSeasonAdmin)
admin.site.register(Project,ProjectsAdmin)
admin.site.register(WorkingCircle,WorkingCircleAdmin)
admin.site.register(Espacement,EspacementsAdmin)
admin.site.register(Stocking,StockingAdmin)
admin.site.register(Specie,SpecieAdmin)
admin.site.unregister(Group)