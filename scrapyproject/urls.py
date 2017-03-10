from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name="mainpage"),
    url(r'^create/$', views.create_new, name="newproject"),
    url(r'^manage/(?P<projectname>[\w]+)/', views.manage_project, name="manageproject"),
    url(r'^delete/(?P<projectname>[\w]+)/', views.delete_project, name="deleteproject"),
    url(r'^createitem/(?P<projectname>[\w]+)/', views.create_item, name="newitem"),
    url(r'^edititems/(?P<projectname>[\w]+)/', views.itemslist, name="listitems"),
    url(r'^deleteitem/(?P<projectname>[\w]+)/(?P<itemname>[\w]+)/', views.deleteitem, name="deleteitem"),
    url(r'^edititem/(?P<projectname>[\w]+)/(?P<itemname>[\w]+)/', views.edititem, name="edititem"),
    url(r'^addpipeline/(?P<projectname>[\w]+)/', views.addpipeline, name="addpipeline"),
    url(r'^editpipelines/(?P<projectname>[\w]+)/', views.pipelinelist, name="listpipelines"),
    url(r'^editpipeline/(?P<projectname>[\w]+)/(?P<pipelinename>[\w]+)/', views.editpipeline, name="editpipeline"),
    url(r'^deletepipeline/(?P<projectname>[\w]+)/(?P<pipelinename>[\w]+)/', views.deletepipeline, name="deletepipeline"),
    url(r'^linkgenerator/(?P<projectname>[\w]+)/', views.linkgenerator, name="linkgenerator"),
    url(r'^scraper/(?P<projectname>[\w]+)/', views.scraper, name="scraper"),
    url(r'^deploy/(?P<projectname>[\w]+)/', views.deploy, name='deploy'),
    url(r'^setdbpass/$', views.create_db_pass, name="setdbpass"),
    url(r'^deploystatus/(?P<projectname>[\w]+)/', views.deployment_status, name="deploystatus"),
    url(r'^startproject/(?P<projectname>[\w]+)/(?P<worker>[\w]+)/', views.start_project, name="startproject"),
    url(r'^stopproject/(?P<projectname>[\w]+)/(?P<worker>[\w]+)/', views.stop_project, name="stopproject"),
    url(r'^allworkerstatus/(?P<projectname>[\w]+)/', views.get_project_status_from_all_workers, name="allworkerstatus"),
    url(r'^getlog/(?P<projectname>[\w]+)/(?P<worker>[\w]+)/', views.see_log_file, name="seelogfile"),
    url(r'^allprojectstatus/', views.gather_status_for_all_projects, name="allprojectstatus"),
    url(r'^editsettings/(?P<settingtype>[\w]+)/(?P<projectname>[\w]+)/', views.editsettings, name="editsettings"),
    url(r'^startonall/(?P<projectname>[\w]+)/', views.start_project_on_all, name="startonall"),
    url(r'^stoponall/(?P<projectname>[\w]+)/', views.stop_project_on_all, name="stoponall"),
    url(r'^globalstatus/', views.get_global_system_status, name="globalstatus"),
]