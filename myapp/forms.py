from django import forms

class PortafolioForm(forms.Form):
    url_image = forms.URLField()
    title_proyecto= forms.CharField(max_length= 50)
    description = forms.CharField(max_length= 500)
    url_github = forms.URLField()
    tag_html = forms.IntegerField()
    tag_css = forms.IntegerField()
    tag_script = forms.IntegerField()
    tag_php = forms.IntegerField()
    tag_python = forms.IntegerField()
    tag_photo = forms.IntegerField()
    
