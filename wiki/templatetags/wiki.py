
##dfffff
import datetime
from django import template
from myproject.models import WikiArticleread as articleread

register = template.Library()


def current_read(format_string):
    user= articleread.objects.create(read='True',user=request.user.id,article=article.id, paid='False',readed=datetime.datetime.now())    
    user.save()
    return datetime.datetime.now().strftime(format_string)

register.simple_tag(current_read)
