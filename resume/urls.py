from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('education/', views.EducationView.as_view(), name='education'),
    path('experience/', views.ExperienceView.as_view(), name='experience'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('courses/', views.CoursesView.as_view(), name='courses'),
    path('save/', views.SaveResumeView.as_view(), name='save_resume'),
    path('success/', views.SuccessView.as_view(), name='success'),
]