from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post_Band
from .forms import Post_BandForm
from django.contrib.auth.decorators import login_required

def index(request):
    Power_list = Post_Band.objects.order_by('-create_date')
    context = {'Power_list': Power_list}
    return render(request, 'Power/Power_list.html', context)

@login_required(login_url='common:login')
def Band_create(request):
    if request.method == 'POST':
        form = Post_BandForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('Power:index')
    else:
        form = Post_BandForm()
    context = {'form': form}
    return render(request, 'Power/Power_form.html', context)