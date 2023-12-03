# from django.contrib import messages
# from django.contrib import auth, messages
# from django.contrib.auth.forms import AuthenticationForm
# from django.shortcuts import redirect, render

# def login_view(request):
    
#     form = AuthenticationForm(request)

#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)

#         if form.is_valid():
#             user = form.get_user()
#             print(user)

#     return render(
#         request,
#         'contact/login.html',
#         {
#             'form': form
#         }
#     )