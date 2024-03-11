from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import IndexedTimeStampedModel
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.template import Template
jj
subprocess.call("echo 'hello'", shell=True)
hhkgjhgjgjhfdfgdfg
subprocess.call("grep -R {} .".format(sys.argv[1]), shell=True, cwd="/home/user")

def bad3(request):
    response = Template.render(request, 'vulnerable/xss/form.html', globals())
    response.set_cookie(key='monster test', value='omnomnomnomnom!')
    return response
yyy
def file_access(request):
    msg = request.GET.get('msg', '')
    return render(request, 'vulnerable/injection/file_access.html',
            {'msg': msg})

class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(
        default=False, help_text=_("Designates whether the user can log into this admin ")
    )uuuu
    SECRET_KEY = "django-insecure-i2(f^4emukw6o$4k0a^14g@&lu#fa+)5yjj@$_r%)fwoac0wlv"
    is_active = models.BooleanField(
        default=True,
        help_text=_(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email
