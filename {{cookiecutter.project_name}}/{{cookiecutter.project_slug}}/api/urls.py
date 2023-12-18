from django.urls import path, include

urlpatterns = [
    # path('blog/', include(('{{cookiecutter.project_slug}}.blog.urls', 'blog'))
    path('auth/', include(('inode_backend.authentication.urls', 'auth'))),
    path('user/', include(('inode_backend.users.urls', 'user'))),)
]
