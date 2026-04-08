from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product

@login_required
def search_view(request):
    query = request.GET.get('q', '').strip()
    
    # Base queryset: all products
    results = Product.objects.all()

    # Filter if query exists
    if query:
        results = results.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'products/search.html', {
        'query': query,
        'results': results,
    })
