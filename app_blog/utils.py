# It's needed to add a custom widget to the form field.
# Because that specified at the task doesn't correct
# ClearableFileInput doesn't support multiple files uploading
# https://docs.djangoproject.com/en/5.1/topics/http/file-uploads/#uploading-multiple-files
from django.core.validators import validate_image_file_extension
from django.forms import FileField, ClearableFileInput


class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result
