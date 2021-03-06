from django.conf.urls import url
from myBlog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name = 'post_list'),
    #url(r'^about/$', views.AboutView.as_view(), name = 'about'),
    url(r'^contact/$', views.ContactView.as_view(), name = 'contact'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name = 'post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name = 'post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name = 'post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name = 'post_remove'),
    url(r'^drafts/$', views.DraftListView.as_view(), name = 'post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name = 'post_publish'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name = 'comment_remove'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
