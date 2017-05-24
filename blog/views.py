from django.shortcuts import render


# blog post view
def post_list(request):
    return render(request, 'blog/post_list.html', {})