from django.contrib import admin
from product.models import Product, Publication, Article, Student, ProductDetails


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'price_in_dollars')
    search_fields = ['name', 'description', 'manufacturer', 'price_in_dollars', ]
    list_filter = ('name', 'manufacturer')


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']
    list_filter = ('title',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline',)
    search_fields = ['headline', 'publications']
    list_filter = ('headline',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','age','roll','city')
    search_fields = ['name', 'city']
    list_filter = ('name',)
from django.utils.safestring import mark_safe
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ('product_name','model_name','serial_no','mobile','status','embed_pdf_file',)
    search_fields = ['serial_no','mobile','model_name']
    list_filter = ('product_name','model_name','serial_no','mobile')

    def embed_pdf_file(self, obj):
        return mark_safe("<a href='view/%d/'>View</a>" % (obj.id))

    embed_pdf_file.allow_tags = True

    embed_pdf_file.short_description = 'Invoice'




admin.site.register(Product, ProductAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(ProductDetails, ProductDetailsAdmin)
