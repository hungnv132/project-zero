from django.contrib import admin
from blog.forms import PostForm
from blog.models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'created_by']
    readonly_fields = ['slug', 'created_at', 'modified_at', 'created_by', 'modified_by']
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'), )
        }),
        ('Tracking Time', {
            'fields': (('created_at', 'modified_at'),)
        }),
        ('Tracking User', {
            'fields': (('created_by', 'modified_by'),)
        })
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = False
    form = PostForm
    list_display = ['id', 'category', 'title', 'status', 'created_at', 'created_by']
    readonly_fields = ['slug', 'created_at', 'modified_at', 'created_by', 'modified_by']
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'),  'category', 'thumbnail', 'intro', 'content', 'status')
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
        super(PostAdmin, self).save_model(request, obj, form, change)