from django import template
from core.admin import views
register = template.Library()


@register.simple_tag
def get_custom_admin_views():
    return views.custom_admin_view_urls()
