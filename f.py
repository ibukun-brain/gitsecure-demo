from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.template import Template

subprocess.call("echo 'hello'", shell=True)

subprocess.call("grep -R {} .".format(sys.argv[1]), shell=True, cwd="/home/user")

def bad3(request):
    response = Template.render(request, 'vulnerable/xss/form.html', globals())
    response.set_cookie(key='monster test', value='omnomnomnomnom!')
    return response

def file_access(request):
    msg = request.GET.get('msg', '')
    return render(request, 'vulnerable/injection/file_access.html',
            {'msg': msg})