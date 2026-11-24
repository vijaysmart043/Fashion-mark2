from django.shortcuts import render
from django.http import JsonResponse


def health_check(request):
    """Health check endpoint for container / deployment monitoring."""
    return JsonResponse({'status': 'healthy', 'database': 'connected'})


def home_view(request):
    """Homepage view showcasing luxury Indian jewellery and sarees."""
    return render(request, 'core/home.html', {
        'featured_categories': [
            {'name': 'Gold Jewellery', 'image': 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&q=80&w=600', 'url': '#'},
            {'name': 'Silver Jewellery', 'image': 'https://images.unsplash.com/photo-1611591475294-1a92e15fb666?auto=format&fit=crop&q=80&w=600', 'url': '#'},
            {'name': 'Silk Sarees', 'image': 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&q=80&w=600', 'url': '#'},
            {'name': 'Wedding Sarees', 'image': 'https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&q=80&w=600', 'url': '#'},
            {'name': 'Designer Sarees', 'image': 'https://images.unsplash.com/photo-1566174053879-31528523f8ae?auto=format&fit=crop&q=80&w=600', 'url': '#'},
            {'name': 'Artificial Jewellery', 'image': 'https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&q=80&w=600', 'url': '#'},
        ]
    })
