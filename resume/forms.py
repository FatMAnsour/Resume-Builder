from django import forms
from django.forms import modelformset_factory
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['objective', 'name', 'email', 'phone', 'address', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'objective': forms.Textarea(attrs={'rows': 3}),
        
        }
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'start_date', 'end_date', 'grade', 'is_ongoing']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        is_going = cleaned_data.get('is_ongoing')
        end_date = cleaned_data.get('end_date')
        if not is_going and end_date is None:
            raise forms.ValidationError("End date is required for ongoing education.")
        if is_going:
            cleaned_data['end_date'] = None
        return cleaned_data

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['position', 'company', 'start_date','is_ongoing', 'end_date', 'description']
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        is_going = cleaned_data.get('is_ongoing')
        end_date = cleaned_data.get('end_date')
        if not is_going and end_date is None:
            raise forms.ValidationError("End date is required for ongoing experience.")
        if is_going:
            cleaned_data['end_date'] = None
        return cleaned_data

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['course_name', 'description', 'duration', 'certificate_link', 'organization']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'description', 'start_date', 'end_date', 'link']
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill', 'level']

EducationFormSet = modelformset_factory(
    Education,
    form=EducationForm,
    extra=1,
    can_delete=True
)

ExperienceFormset = modelformset_factory(
    Experience,
    form=ExperienceForm,
    extra=1,
    can_delete=True
)

CoursesFormset = modelformset_factory(
    Courses,
    form=CoursesForm,
    extra=1,
    can_delete=True
)
ProjectsFormset = modelformset_factory(
    Projects,
    form=ProjectsForm,
    extra=1,
    can_delete=True
)

SkillsFormset = modelformset_factory(
    Skills,
    form=SkillsForm,
    extra=1,
    can_delete=True
)