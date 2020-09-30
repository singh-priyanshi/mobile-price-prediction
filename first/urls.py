from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.home,name="first_home"),
    path('show_head/', views.showhead, name="show_head"),
    path('jqueryserver/',views.jqueryserver),
    path('predict_price_lr/',views.predict_price_lr,name='predict_price_lr'),
    path('predict_price_nbc/',views.predict_price_nbc,name='predict_price_nbc'),
    path('predict_price_lr/predictlr/', views.predictlr, name='predictlr'),
    path('predict_price_nbc/predictnbc/', views.predictnbc, name='predictnbc'),

    #  url(r'plot.png',views.plot),
]