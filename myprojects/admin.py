from django.contrib import admin
from myprojects.models import myprojects
from myprojects.models import Author
from myprojects.models import comments

admin.site.register(myprojects)
admin.site.register(Author)
admin.site.register(comments)