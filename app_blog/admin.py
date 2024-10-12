from django.contrib import admin
from django.shortcuts import get_object_or_404

from .models import ArticleImage, Category, Article
from .forms import ArticleImageForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category",)
    fieldsets = (("", {"fields": ("category", "slug",),
                       }),
                 )
    prepopulated_fields = {"slug": ("category",)}


admin.site.register(Category, CategoryAdmin)


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0
    fieldsets = (("", {"fields": ("title", "image",), }),
                 )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date", "slug", "main_page")
    inlines = [ArticleImageInline]
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("category",)
    fieldsets = (
        ("", {
            "fields": (
                "pub_date",
                "title",
                "description",
                "main_page"
            ),
        }),
        (u"Додатково", {
            "classes": ("grp-collapse grp-closed",),
            "fields": ("slug",),
        }),
    )



admin.site.register(Article, ArticleAdmin)
