from django.views.generic import CreateView
from .models import Request, Profile, Rule
from .forms import CreateRequestForm
from django.urls import reverse_lazy


class RequestCreateView(CreateView):
    model = Request
    form_class = CreateRequestForm
    template_name = 'create_request.html'
    success_url = reverse_lazy('request')

    def get_context_data(self, **kwargs):
        context = super(RequestCreateView, self).get_context_data(**kwargs)
        context['vacation_days_left'] = int(self.request.user.profile.vacation_days_left())



        requests = []

        requests.append({
            'title': Request.PENDING,
            'id':  'pending',
            'items': Request.objects.filter(
                profile=self.request.user.profile,
                request_status=Request.PENDING
            )
        })

        requests.append({
            'items': Request.objects.filter(
                profile=self.request.user.profile,
                request_type=Request.VACATION,
                request_status__in=[Request.APPROVED, Request.REJECTED]
            ),
            'id': 'vacation',
            'title': Request.VACATION
        })

        requests.append({
            'items': Request.objects.filter(
                profile=self.request.user.profile,
                request_type=Request.SICK_LEAVE
            ),
            'id': 'sick',
            'title': Request.SICK_LEAVE
        })

        requests.append({
            'items': Request.objects.filter(
                profile=self.request.user.profile,
                request_type=Request.COMPENSATORY_HOLIDAY,
                request_status__in=[Request.APPROVED, Request.REJECTED]
            ),
            'id': 'compensatory_holiday',
            'title': Request.COMPENSATORY_HOLIDAY
        })

        requests.append({
            'items': Request.objects.filter(
                profile=self.request.user.profile,
                request_type=Request.COMPENSATORY_HOLIDAY,
                request_status__in=[Request.APPROVED, Request.REJECTED]
            ),
            'id': 'compensatory_holiday',
            'title': Request.COMPENSATORY_HOLIDAY
        })

        requests.append({
            'items': Request.objects.filter(
                profile=self.request.user.profile,
                request_type=Request.BUSINESS_TRIP,
                request_status__in=[Request.APPROVED, Request.REJECTED]
            ),
            'id': 'business_trip',
            'title': Request.BUSINESS_TRIP
        })

        context['requests'] = requests
        context['profile'] = self.request.user.profile
        return context

    def get_form_kwargs(self):
        form_kwargs = super(RequestCreateView, self).get_form_kwargs()
        form_kwargs['request'] = self.request
        return form_kwargs
