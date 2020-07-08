from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserChangeForm
from .forms import UserForm, UserProfileForm

@login_required
def profile(request):
    context = {'user': request.user}
    return render(request, "account/profile.html", context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        uform = UserForm(request.POST, instance=request.user)
        pform = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            custom_form = pform.save(commit=False)
            custom_form.user = request.user
            custom_form.save()
            return redirect('profile')
    else:
        uform = UserForm(instance=request.user)
        pform = UserProfileForm(instance=request.user.userprofile)
        context = {'uform': uform, 'pform': pform}
        return render(request, "account/profile_edit.html", context)