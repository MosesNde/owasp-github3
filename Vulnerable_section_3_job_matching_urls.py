 urlpatterns = [
     path('admin/', admin.site.urls),
     path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='accounts/login/', permanent=False)),
 ]
 
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)