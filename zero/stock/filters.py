from datetime import datetime, timedelta
from django.utils.encoding import force_text
from django.contrib.admin.filters import SimpleListFilter


class DateFilter(SimpleListFilter):
    title = 'Date'
    parameter_name = 'date'

    def lookups(self, request, model_admin):
        return(
            ('last_day', 'Last day'),
            ('last_9_days', 'Last 9 days'),
            ('last_21_days', 'Last 21 days'),
        )

    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == force_text(lookup),
                'query_string': changelist.get_query_string({self.parameter_name: lookup}, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        today = datetime.now()
        weekday = today.weekday()

        last_day = today
        last_9_days = today - timedelta(days=9)
        last_21_days = today - timedelta(days=21)

        # If today is saturday or sunday
        if weekday > 4:
            last_day = today - timedelta(weekday-4)

        if self.value() == 'last_9_days':
            return queryset.filter(date__gte=last_9_days)
        elif self.value() == 'last_21_days':
            return queryset.filter(date__gte=last_21_days)
        return queryset.filter(date=last_day)
