from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Brand  # <--- Ensure 'Brand' yahan likha ho

# --- HOME VIEW ---
def home_view(request):
    # Line 7 par ab error nahi aayega kyunki Brand import ho chuka hai
    brands = Brand.objects.all()
    featured_phones = Product.objects.filter(category='mobile').order_by('-created_at')[:15]
    
    return render(request, 'home.html', {
        'brands': brands,
        'featured_phones': featured_phones
    })

# --- ALL PRODUCTS LISTING ---
def phone_list_view(request):
    products = Product.objects.all().order_by('-created_at')
    
    # URL se category uthane ke liye (Laptop/TV/Tablet)
    category = request.GET.get('category')
    if category:
        products = products.filter(category=category)

    return render(request, 'listing.html', {'phones': products})

# --- DETAIL VIEW ---
def phone_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'phone_detail.html', {'phone': product})

# --- SIGNUP VIEW ---
def signup_view(request):
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import login
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# --- COMPARE VIEW ---
def compare_phones(request):
    return render(request, 'compare.html')