from django.shortcuts import redirect


def authenticated_user(view_fun):
    def wrapper(request):
        if not request.user.is_authenticated:
            return view_fun(request)
        else:
            return redirect('/')
    return wrapper;

def admin_only(view_fun):
    def wrapper(request):
        if request.user.groups.first().name=='admin':
            return view_fun(request)

        if request.user.groups.first().name=='customer':
            return redirect('/customer_profile')
    return wrapper
        