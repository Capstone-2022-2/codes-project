from django.contrib import admin

# Register your models here.


from boardapp.models import PostCategory
from commentapp.models import Comment
from postapp.models import Post
from practiceapp.models import Practice, Language, Presult
from upracticeapp.models import Upractice, Upresult

admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Upractice)
admin.site.register(Practice)
admin.site.register(Language)
admin.site.register(Presult)
admin.site.register(Upresult)
