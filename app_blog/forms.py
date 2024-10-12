from django import forms

from .models import ArticleImage
from .utils import MultipleFileField


class ArticleImageForm(forms.ModelForm):
    image = MultipleFileField(label="Зображення")

    def save(self, commit=True):
        instance = super().save(commit=False)
        images = self.cleaned_data.get('image')

        if images:
            for img in images:
                ArticleImage.objects.create(article=instance.article, image=img, title=instance.title)
        return instance

    class Meta:
        model = ArticleImage
        fields = '__all__'
