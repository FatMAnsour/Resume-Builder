from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from .forms import *
# Create your views here.

class BaseResumeView(View):
    session_key = 'resume'
    def get_session_data(self):
        return self.request.session.get(self.session_key, {})
    
    def save_session_data(self, session_data):
        self.request.session[self.session_key] = session_data
        self.request.session.modified = True

class ProfileView(BaseResumeView):
    template_name = 'resume_builder/profile_form.html'
    form_class = ProfileForm
    success_url = 'education'

    def get(self, request, *args, **kwargs):
        session_data = self.get_session_data()
        profile_data = session_data.get('profile',{})
        form = self.form_class(initial=profile_data)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            session_data = self.get_session_data()            
            session_data['profile'] = form.cleaned_data #save the data in a session
            self.save_session_data(session_data) #save the updated session 
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


class EducationView(BaseResumeView):
    template_name = 'resume_builder/education_form.html'
    formset_class = EducationForm
    success_url = 'experience'
    prefix = 'education'

    def get(self, request, *args, **kwargs):
        session_data = self.get_session_data()
        education_data = session_data.get('education',[])
        formset = self.formset_class(initial=education_data, prefix=self.prefix)
        return render(request, self.template_name, {'formset': formset})
    
    def post(self, request, *args, **kwargs):
        formset = self.formset_class(request.POST, prefix=self.prefix)
        if formset.is_valid():
            session_data = self.get_session_data()
            validated_data = []
            for form in formset:
                data = form.cleaned_data
                if data and not data.get('DELETE', False):
                    validated_data.append(data)
            session_data['education'] = validated_data
            self.save_session_data(session_data)
            return redirect(self.success_url)
        return render(request, self.template_name, {'formset': formset})
class ExperienceView(BaseResumeView):
    template_name='resume_builder/experience_form.html'
    formset_class = ExperienceForm
    success_url = 'skills'
    prefix = 'experience'
    def get(self,request,*args,**kwargs):
        session_data = self.get_session_data()
        experience_data = session_data.get('experience',[])
        formset = self.formset_class(initial=experience_data,prefix=self.prefix)
        return render(request,self.template_name,{'formset':formset})
    def post(self,request,*args,**kwargs):
        formset = self.formset_class(request.POST,prefix=self.prefix)
        if formset.is_valid():
            session_data = self.get_session_data()
            validated_data = []
            for form in formset:
                data = form.cleaned_data
                if data and not data.get('DELETE', False):
                    validated_data.append(data)
            session_data['experience'] = validated_data
            self.save_session_data(session_data)
            return redirect(self.success_url)
        return render(request,self.template_name,{'formset':formset})

class SkillsView(BaseResumeView):
    template_name = 'resume_builder/skills_form.html'
    formset_class = SkillsForm
    success_url = 'projects'
    prefix = 'skills'

    def get(self, request, *args, **kwargs):
        session_data = self.get_session_data()
        skilles_data = session_data.get('skills',[])
        formset = self.formset_class(initial=skilles_data,prefix=self.prefix)
        return render(request, self.template_name, {'formset': formset})
    
    def post(self, request, *args, **kwargs):
        formset = self.formset_class(request.POST, prefix=self.prefix)
        if formset.is_valid():
            session_data = self.get_session_data()
            validated_data = []
            for form in formset:
                data = form.cleaned_data
                if data and not data.get('DELETE', False):
                    validated_data.append(data)
            session_data['skills'] = validated_data
            self.save_session_data(session_data)
            return redirect(self.success_url)
        return render(request, self.template_name, {'formset': formset})
    
class ProjectsView(BaseResumeView):
    template_name = 'resume_builder/projects_form.html'
    formset_class = ProjectsForm
    success_url = 'courses'
    prefix = 'projects'
    def get(self, request, *args, **kwargs):
        session_data = self.get_session_data()
        projects_data = session_data.get('projects',[])
        formset = self.formset_class(initial=projects_data,prefix=self.prefix)
        return render(request, self.template_name, {'formset': formset})
    
    def post(self, request, *args, **kwargs):
        formset = self.formset_class(request.POST, prefix=self.prefix)
        if formset.is_valid():
            session_data = self.get_session_data()
            validated_data = []
            for form in formset:
                data = form.cleaned_data
                if data and not data.get('DELETE', False):
                    validated_data.append(data)
            session_data['projects'] = validated_data
            self.save_session_data(session_data)
            return redirect(self.success_url)
        return render(request, self.template_name, {'formset': formset})

class CoursesView(BaseResumeView):
    template_name = 'resume_builder/courses_form.html'
    formset_class = CoursesForm
    success_url = 'save_resume'
    prefix = 'courses'
    def get(self, request, *args, **kwargs):
        session_data = self.get_session_data()
        projects_data = session_data.get('courses',[])
        formset = self.formset_class(initial=projects_data,prefix=self.prefix)
        return render(request, self.template_name, {'formset': formset})
    
    def post(self, request, *args, **kwargs):
        formset = self.formset_class(request.POST, prefix=self.prefix)
        if formset.is_valid():
            session_data = self.get_session_data()
            validated_data = []
            for form in formset:
                data = form.cleaned_data
                if data and not data.get('DELETE', False):
                    validated_data.append(data)
            session_data['courses'] = validated_data
            self.save_session_data(session_data)
            return redirect(self.success_url)
        return render(request, self.template_name, {'formset': formset})

class SaveResumeView(BaseResumeView):
    template_name = 'resume_builder/save_resume.html'
    def get (self,request,*args,**kwargs):
        session_data = self.get_session_data()
        return render(request,self.template_name,{'session_data':session_data})
    
    def post(self,request,*args,**kwargs):
        session_data = self.get_session_data()
        if 'profile' in session_data:
            Profile.objects.create(**session_data['profile'])
        if 'education' in session_data:
            for edu in session_data['education']:
                edu_data = {k: v for k, v in edu.items() if k != 'is_ongoing'}
                Education.objects.create(**edu_data)
        if 'experience' in session_data:
            for exp in session_data['experience']:
                exp_data = {k: v for k, v in exp.items() if k != 'is_ongoing'}
                exp_data['current_job'] = exp.get('is_ongoing', False)
                Experience.objects.create(**exp_data)
        if 'skills' in session_data:
            for skill in session_data['skills']:
                Skills.objects.create(**skill)
        if 'projects' in session_data:
            for project in session_data['projects']:
                Projects.objects.create(**project)
        if 'courses' in session_data:
            for course in session_data['courses']:
                Courses.objects.create(**course)
        request.session.pop(self.session_key,None)
        return redirect('success')
    
class SuccessView(BaseResumeView):
    template_name = 'resume_builder/success.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)