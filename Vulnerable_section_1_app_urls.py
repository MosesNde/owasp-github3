 handler500 = 'app.views.custom_error'
 
 
api_schema_view = get_swagger_view(title='PatrOwl Manager REST-API')
 
 urlpatterns = [
     url(r'^apis-doc', api_schema_view),