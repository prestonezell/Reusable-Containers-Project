from django import forms

class ProductStatusForm(forms.Form):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('collector', 'With Collector'),
    ]
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.RadioSelect,
        required=True,
    )