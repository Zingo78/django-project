from django.contrib import admin
from .models import Book, Author
# Register your models here.


class BookManager(admin.ModelAdmin):
    #列表页里现实哪些字段的列
    list_display = ['id','title','pub','price']
    #控制list_display中的字段 那些可以连接到修改页
    list_display_links = ['title']
    #添加过滤器
    list_filter = ['pub']
    #添加搜索框[模糊查询]
    search_fields = ['title']
    #添加可在列表页编辑的字段
    list_editable = ['price']

class AuthorManager(admin.ModelAdmin):
    list_display = ['id','name','age']

admin.site.register(Book,BookManager)
admin.site.register(Author,AuthorManager)