from django.contrib import admin

# Register your models here.  

from .models import Author,Genre ,Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance) 

#define the admin class 
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ( 'first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] 
# registering the admin classes for book using the decarator(@)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'display_genre')
   inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')


    fieldsets = (
        (None,{
            'fields':('book','imprint','id')
        }),
        ('Availability', {
            'fields': ('status','due_back','borrower')
        }),
    )
