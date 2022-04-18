from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from rest_framework.settings import api_settings
from rest_framework import throttling


class RootRateThrottle(throttling.UserRateThrottle):

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)

        self.rate = self.get_rate(request)

        self.num_requests, self.duration = self.parse_rate(self.rate)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

    def get_rate(self, request=None):
        """
        Determine the string representation of the allowed request rate.
        """
        if not getattr(self, 'scope', None):
            msg = ("You must set either `.scope` or `.rate` for '%s' throttle" %
                   self.__class__.__name__)
            raise ImproperlyConfigured(msg)

        if request and request.user.is_superuser:
            throttle_rates = settings.REST_FRAMEWORK["ROOT_THROTTLE_RATES"]
        else:
            throttle_rates = api_settings.DEFAULT_THROTTLE_RATES
        try:
            return throttle_rates[self.scope]
        except KeyError:
            msg = "No default throttle rate set for '%s' scope" % self.scope
            raise ImproperlyConfigured(msg)


class ByHourRateThrottle(RootRateThrottle):
    scope = 'hour'
