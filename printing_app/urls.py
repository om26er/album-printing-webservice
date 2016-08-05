from django.conf.urls import url

from printing_app import views as v

urlpatterns = [
    url(r'^api/register$', v.Register.as_view()),
    url(r'^api/activate$', v.Activate.as_view()),
    url(r'^api/request-activation-key$', v.Activate.as_view()),
    url(r'^api/login$', v.Login.as_view()),
    url(r'^api/forgot-password$', v.ForgotPassword.as_view()),
    url(r'^api/change-password$', v.ChangePasswordView.as_view()),
    url(r'^api/me$', v.Profile.as_view()),

    url(r'^api/user/album$', v.ListCreateAlbum.as_view()),
    url(r'^api/user/album/(?P<pk>\d+)$', v.AlbumView.as_view()),
    url(r'^api/user/photo$', v.CreatePhoto.as_view()),
    url(r'^api/user/photo/(?P<pk>\d+)$', v.PhotoView.as_view()),
]
