from pdb import post_mortem
from socket import fromshare
from django import forms

from taskapp.models import Info
class profileForm(forms.Form):
    class Meta:
        model=Info
        fields='__all__'
    def clean(self):
        super(profileForm,self).clean()

        firstname=self.cleaned_data.get("firstname")
        lastname=self.cleaned_data.get("lastname")
        Relatioship=self.cleaned_data.get("Relationship")
        gender=self.cleaned_data.get("gender")
        lang=self.cleaned_data.get("lang")
        hobbies=self.cleaned_data.get("hobbies")
        picture=self.cleaned_data.get("picture")
        email=self.cleaned_data.get("email")
        phone=self.cleaned_data.get("phone")
        door=self.cleaned_data.get("door")
        street=self.cleaned_data.get("street")
        city=self.cleaned_data.get("city")
        dist=self.cleaned_data.get("dist")
        state=self.cleaned_data.get("state")

        country=self.cleaned_data.get("country")
        code=self.cleaned_data.get("code")
        course=self.cleaned_data.get("course")
        institute=self.cleaned_data.get("institute")
        address=self.cleaned_data.get("address")
        started=self.cleaned_data.get("started")
        passed=self.cleaned_data.get("passed")
        gpa=self.cleaned_data.get("gpa")
        resume=self.cleaned_data.get("resume")

        
        return self.cleaned_data

    
    
