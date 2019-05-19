from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from sesame import utils
from django.core.mail import send_mail


def login_now(request):
    # magic link login
    if request.method == "POST":
        try:
            email = request.POST.get('emailId')
            user = User.objects.get(email=email)
            login_token = utils.get_query_string(user)
            login_link = 'https://admagvgh.herokuapp.com/{}'.format(login_token)
            # login_link = '127.0.0.1:8000/{}'.format(login_token)

            html_message = """
    		<p>Hi there,</p>
    		<p>Here is your <a href="{}">magic link</a></p>
    		<p>Thanks,</p>
    		<p>AdMA Blog</p>
    		""".format(login_link)

            send_mail(
                'AdMA Magic Link',
                html_message,
                'admin@admagvgh.herokuapp.com',
                [email],
                fail_silently=False,
                html_message=html_message
            )
        except User.DoesNotExist:
            raise Http404("Requested user does not exist. Contact site admin.")
        message = "Please check your email for magic link."
        context = {'message': message}
        return render(request, 'accounts/login.html', context)
    return render(request, 'accounts/login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home:index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username:{} and password:{}".format(username, password))
            return HttpResponse("Invalid login details given.")
    else:
        return render(request, 'accounts/login_now.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login_now'))
	# return HttpResponseRedirect(reverse('accounts:login'))