from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
import datetime


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        pass

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    release_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.user.get_full_name()

    def vacation_days_left(self):
        days_in_year = 365.242199

        rule = Rule.objects.last()

        delta = datetime.date.today() - self.release_date
        total_worked_days = delta.days

        vacation_days_accrued = total_worked_days * (rule.vacations_limit / days_in_year)

        all_approved_vacation_requests = Request.objects.filter(
            profile=self,
            request_status=Request.APPROVED,
            request_type=Request.VACATION
        )

        vacation_days_taken = 0
        for request in all_approved_vacation_requests:
            vacation_delta = request.end_date - request.start_date
            vacation_days_taken += vacation_delta.days

        return int(vacation_days_accrued - vacation_days_taken)

    def sick_leave_days_left(self):

        rule = Rule.objects.last()


class Rule(SingletonModel):
    sick_leave_limit = models.IntegerField()
    vacations_limit = models.IntegerField()


class Request(models.Model):
    VACATION = 'Vacation'
    SICK_LEAVE = 'Sick Leave'
    COMPENSATORY_HOLIDAY = 'Compensatory Holiday'
    BUSINESS_TRIP = 'Business Trip'

    REQUEST_TYPE_CHOICES = (
        (VACATION, VACATION),
        (SICK_LEAVE, SICK_LEAVE),
        (COMPENSATORY_HOLIDAY, COMPENSATORY_HOLIDAY),
        (BUSINESS_TRIP, BUSINESS_TRIP)
    )

    APPROVED = 'Approved'
    REJECTED = 'Rejected'
    PENDING = 'Pending'
    REQUEST_STATUS_CHOICES = (
        (APPROVED, APPROVED),
        (REJECTED, REJECTED),
        (PENDING, PENDING)
    )

    request_type = models.CharField(max_length=30, choices=REQUEST_TYPE_CHOICES)
    request_status = models.CharField(max_length=15, choices=REQUEST_STATUS_CHOICES, default=PENDING)
    start_date = models.DateField()
    end_date = models.DateField()
    message = models.TextField(default='')
    profile = models.ForeignKey(Profile, blank=False, null=False, on_delete=models.CASCADE)

    def css_class(self):
        if self.request_status == Request.APPROVED:
            return 'success'
        if self.request_status == Request.REJECTED:
            return 'warning'
        if self.request_status == Request.PENDING:
            return 'info'
        return ''