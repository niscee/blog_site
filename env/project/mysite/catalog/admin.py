from django.contrib import admin
from .models import Book,Author,Genre,BookInstance

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','isBn')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth')
    fields = ['first_name','last_name',('date_of_birth','date_of_death')]


admin.site.register(Genre)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status','due_back')
    list_display = ('id','book','imprint')
    fieldsets = (
        (None,{
            'fields':('id','book','imprint')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )