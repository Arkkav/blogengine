from django.shortcuts import redirect


def redirect_blog(request):
    return redirect('posts_list_url', permanent=False)
    # 302 - not a permanent redirect, because of chrome cashing and may be some
    # homepage.html at least for your users

