
##dfffff
import datetime
from django import template
from myproject.models import WikiArticleread as articleread

register = template.Library()

@register.assignment_tag(takes_context=True)
def current_read(request):
    user= articleread.objects.create(read='True',user=request.user.id,article=article.id, paid='False',readed=datetime.datetime.now())    
    user.save()
    return datetime.datetime.now()

register.simple_tag(current_read)
