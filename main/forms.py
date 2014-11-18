from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div, \
    MultiField

class ContactForm(forms.Form):

    name = forms.CharField(
        label = "Full Name",
        required = True
    )
    email = forms.EmailField()
    company = forms.CharField(
        required=False
    )
    message = forms.CharField(
        widget = forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Contact me and let\'s get started.',
                Div(
                    'name',
                    'email',
                    'company',
                    css_class="col-md-4"
                ),
                Div(
                    'message',
                    ButtonHolder(
                        Div(
                            Submit('submit', 'Send', css_class='btn-lg'),
                            css_class="text-center"
                        )
                    ),
                    css_class="col-md-8",
                )
            ),
        )

