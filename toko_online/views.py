from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk
from .forms import PostForm

# Create your views here.
def home_toko(request):
    produk = Produk.objects.all().order_by('-update_at')
    return render(request, 'toko_online/index.html', {'product': produk})

def input_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home_toko')
    else:
        form = PostForm()
    return render(request, 'toko_online/post_new.html', {'form': form})

def post_detail(request, post_id):
    post_num = get_object_or_404(Produk, id=post_id)
    return render(request, 'toko_online/detail.html', {'product': post_num})