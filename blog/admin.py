from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','author','counted_view','status','login_requires','published_date','created_date')
    list_filter=('status','author')
    #ordering=['-created_date']
    search_fields=['title','content']
    summernote_fields =('content',)
    
    
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('name','post','approved','created_date')
    list_filter=('post','approved')
    #ordering=['-created_date']
    search_fields=['name','post']
    





admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)