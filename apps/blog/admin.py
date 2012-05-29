from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'slug', 'location', 'trip', 'date_created', 'allow_comments', 'published')
    search_fields = ['title', 'slug', 'location', 'trip']
    date_hierarchy = 'date_created'
    readonly_fields = ('slug',)
    fields = (('title', 'tag_line', 'published'), 'content', 'synopsis', ('trip', 'location'), ('tags', 'date_created', 'allow_comments'), 'images')
    actions = ['publish']

    def publish(self, request, queryset):
        rows = queryset.update(published=True)
        if rows == 1:
            message_bit = "1 blog post was"
        else:
            message_bit = "%s blog posts were" % rows
        self.message_user(request, "%s successfully published." % message_bit)


admin.site.register(Post, PostAdmin)