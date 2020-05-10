from django import forms
from blog.models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):  # class forms.Form generates HTML tag for every field (widget in django terms)
    # class ModelForm has its own save method
    # title = forms.CharField(max_length=50)  # input fields in this case
    # slug = forms.CharField(max_length=50)
    #
    # title.widget.attrs.update({'class': "form-control"})  # for Bootstrap style widgets in pattern
    # slug.widget.attrs.update({'class': "form-control"})
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'slug': forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()  # "get" func. in other cases, but here 'slug' key exactly exists

        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. "{}" slug already exists'.format(new_slug))
        return new_slug


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'slug': forms.TextInput(attrs={"class": "form-control"}),
            'body': forms.Textarea(attrs={"class": "form-control"}),
            'tags': forms.SelectMultiple(attrs={"class": "form-control"}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug
