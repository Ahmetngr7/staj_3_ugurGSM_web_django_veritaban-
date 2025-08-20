from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def kayit(request):
    if request.user.is_authenticated:
        return redirect('anasayfa')  # Veya istediğin başka bir sayfaya yönlendir
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kayıt başarılı! Giriş yapabilirsiniz.')
            return redirect('accounts:giris')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


