from django.contrib import admin

# Register your models here.
from myindex.models import Article_my,Article_pl


@admin.register(Article_my)
class Myinfo_admin(admin.ModelAdmin):
    list_per_page = 3
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id', 'article_name', 'article_author', 'article_count', 'article_img', 'article_title']
    list_display_links = ['id', 'article_name', 'article_author', 'article_count', 'article_title']
    list_filter = ['article_name']
    search_fields = ['article_name']

    fieldsets = (
        ('基本信息', {'fields': ('article_name','article_author','article_count','article_img','article_title')}),
    )
