from django.contrib import admin
from . models import Movie
from .models import Genre

admin.site.register(Genre)
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date','description','poster','actors','category','youtube_trailer_link','director']
    list_editable = ['poster','description','actors','director']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20
admin.site.register(Movie,MovieAdmin)


from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.urls import reverse

def view_users_redirect(request):
    return HttpResponseRedirect(reverse('view_users'))

class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('view-users/', self.admin_view(view_users_redirect), name='view_users_redirect'),
        ]
        return custom_urls + urls

admin_site = CustomAdminSite(name='custom_admin')


from django.contrib.auth.models import User
admin_site.register(User)