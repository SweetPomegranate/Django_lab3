from django import forms
from django.utils.text import slugify
from .models import Article, ArticleImage, Category


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'pub_date', 'main_page', 'category']

class ArticleImageForm(forms.ModelForm):
    images = forms.ImageField(
        		widget=forms.ClearableFileInput(attrs={})
    )

    class Meta:
        model = ArticleImage
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category', 'slug']

    def save(self, commit=True):
        category = super().save(commit=False)
        if not category.slug:
            category.slug = slugify(category.category)
        if commit:
            category.save()
        return category



