from django.contrib import admin

from books.models import AdvUser, Book, Comment


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name'),
    fields = (('username', 'email'), ('first_name', 'last_name'),
              ('send_messages', 'is_active'),
              ('is_staff', 'is_superuser'),
              'groups', 'user_permissions',
              ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('name', )
