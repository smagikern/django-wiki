
##dfffff
import datetime
from django import template
from myproject.models import WikiArticleread as articleread

import re

from django.conf import settings as django_settings
from django import template
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model
from django.forms import BaseForm
from django.utils.safestring import mark_safe
from django.template.defaultfilters import striptags
from django.utils.http import urlquote
from django.contrib.auth.models import User
from six.moves import filter

register = template.Library()

@register.assignment_tag(takes_context=True)
def current_read(request):
    user= articleread.objects.create(read='True',user=self.request.user.id,article=article.id, paid='False',readed=datetime.datetime.now())    
    user.save()
    return datetime.datetime.now()

register.simple_tag(current_read)
