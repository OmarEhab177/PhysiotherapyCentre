from django.http import HttpResponse
from django.http import  HttpResponseRedirect

# not used
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
           return HttpResponseRedirect('index')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None 
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('you are not allowed to access this page')
        return wrapper_func
    return decorator