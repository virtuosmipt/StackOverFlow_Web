from django.forms import forms, CharField, Textarea



class AskQuestion(forms.Form):
    title = CharField()
    text = CharField(widget=Textarea)
    tags = CharField()

    def clean_title(self):
        return self.cleaned_data['title']
    def clean_text(self):
        return self.cleaned_data['text']
    def clean_tags(self):
        return self.cleaned_data['tags']