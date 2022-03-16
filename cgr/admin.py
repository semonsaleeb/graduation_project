from django.contrib import admin
from .models import Cgr


class CgrAdmin(admin.ModelAdmin):
      list_display = ('id', 'upload_file', 'type_of_file', 'kmer_size', 'img')


# class ImgAdmin(admin.ModelAdmin):
#       list_display = ('id', 'img')


admin.site.register(Cgr, CgrAdmin)
#admin.site.register(Img, ImgAdmin)

