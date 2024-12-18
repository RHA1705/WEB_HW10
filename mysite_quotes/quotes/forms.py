from django.forms import ModelForm, CharField, TextInput, DateField, DateInput, ModelMultipleChoiceField, ModelChoiceField, Select, SelectMultiple
from .models import Tag, Author, Quotes
from mysite_quotes.settings import DATE_INPUT_FORMATS

DATE_INPUT_FORMATS = ['%d.%m.%Y']
class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=50, required=True, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Tag
        fields = ['name']

class AuthorForm(ModelForm):
    fullname = CharField(max_length=200, required=True, widget=TextInput(attrs={"class": "form-control"}))
    born_date = DateField(input_formats=DATE_INPUT_FORMATS, widget=DateInput(attrs={"class": "form-control"}))
    born_location = CharField(max_length=200, required=True, widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(required=True, widget=TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class QuoteForm(ModelForm):
    quote = CharField(required=True, widget=TextInput(attrs={"class": "form-control"}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by('fullname'), widget=Select(attrs={'class': 'form-select'}))
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('name'), widget=SelectMultiple(attrs={'class': 'form-select', 'size': '5'}))
    class Meta:
        model = Quotes
        fields = ['quote', 'author', 'tags']
