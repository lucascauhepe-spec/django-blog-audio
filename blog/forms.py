from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "status"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 12}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if len(title) < 5:
            raise forms.ValidationError("The title must be at least 5 characters long.")
        return title