from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin

# Unregister the User model from the default admin
admin.site.unregister(User)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ImportExportModelAdmin):
    pass



# Post
admin.site.register(PostComment)


@admin.register(PostCategory)
class PostCategoryIMportExport(ImportExportModelAdmin):
    pass


@admin.register(PostList)
class PostListIMportExport(ImportExportModelAdmin):
    pass



@admin.register(Post)
class PostIMportExport(ImportExportModelAdmin):
    pass

@admin.register(Book)
class BookIMportExport(ImportExportModelAdmin):
    pass


@admin.register(Subscribe)
class SubscribeIMportExport(ImportExportModelAdmin):
    pass


@admin.register(Template)
class TemplateIMportExport(ImportExportModelAdmin):
    pass






# Book

@admin.register(BookCategory)
class BookCategoryIMportExport(ImportExportModelAdmin):
    pass


admin.site.register(BookList)
admin.site.register(CommentBook)

# other Tols
admin.site.register(Contact)
admin.site.register(IpModel)


# Tempate 
admin.site.register(TemplateImages)
admin.site.register(TemplateLanguage)
admin.site.register(TemplateOrder)
admin.site.register(TemplatesCategory)
admin.site.register(TemplateTols)
admin.site.register(TemplateType)


# Page
@admin.register(Page)
class PageIMportExport(ImportExportModelAdmin):
    pass


# Language
@admin.register(Language)
class LanguageIMportExport(ImportExportModelAdmin):
    pass





