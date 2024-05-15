from django.contrib import admin
from .models import Category, Product, User

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)

# class SubcategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug':('name',)}
# admin.site.register(Subcategory, SubcategoryAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','slug', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name']
admin.site.register(User, UserAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'description', 'availabel', 'created', 'updated']
    list_filter = ['availabel', 'created', 'updated']
    list_editable = ['price', 'availabel']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)