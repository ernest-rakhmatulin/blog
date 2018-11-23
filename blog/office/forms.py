from .models import Profile, Request, Rule
from django import forms
import datetime


class CreateRequestForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = ['request_type', 'start_date', 'end_date', 'message']

    def __init__(self, request, *args, **kwargs):
        super(CreateRequestForm, self).__init__(*args, **kwargs)
        self.request = request

    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']

        if start_date < datetime.date.today():
            raise forms.ValidationError("Слишком рано в отпуск собрались.")

        return start_date

    def clean(self):
        cleaned_data = super(CreateRequestForm, self).clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:

            if start_date > end_date:
                raise forms.ValidationError('Проверьте даты начала и конца отпуска.')

            delta = end_date - start_date
            vacation_days_left = self.request.user.profile.vacation_days_left()
            if vacation_days_left < delta.days:
                raise forms.ValidationError('Запрос привышает доступный лимит дней: %s' % vacation_days_left)

        self.instance.profile = self.request.user.profile
        return cleaned_data




