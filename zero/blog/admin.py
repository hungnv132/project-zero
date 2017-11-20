from django.contrib import admin
from blog.models import Category, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = False
    list_display = ['title', 'content', 'created_at', 'created_by']
    readonly_fields = ['slug', 'created_at', 'modified_at']
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', ('category', 'status'), 'content')
        }),
        ('Tracking Time', {
            'fields': (('created_at', 'modified_at'), )
        }),
        ('Tracking User', {
            'fields': (('created_by', 'modified_by'), )
        })
    )

    def save_model(self, request, obj, form, change):
        if obj.pk:
            obj.modified_by = request.user
        else:
            obj.created_by = request.user
        super(ArticleAdmin, self).save_model(request, obj, form, change)