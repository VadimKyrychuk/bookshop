from django.shortcuts import render, redirect, get_object_or_404
from books.models import Profile
from .forms import ProfileForm


def edit(request):
    if request.method == 'GET':
        current_user = get_object_or_404(pk=request.user.id, klass=Profile)
        form = ProfileForm(instance=current_user)
    else:
        current_user = get_object_or_404(pk=request.user.id, klass=Profile)
        form = ProfileForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
    return render(request, 'edit.html', {'form': form})
