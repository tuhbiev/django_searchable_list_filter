from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class SearchableListFilter(admin.SimpleListFilter):
    template = 'admin/searchable_list_filter.html'
    title = None
    parameter_name = None
    lookup_field = None
    lookup_expr = 'icontains'

    def lookups(self, request, model_admin):
        return []

    def choices(self, changelist):
        yield {
            'selected': self.value() is None,
            'query_string': changelist.get_query_string({}, [self.parameter_name]),
            'display': _('All'),
        }

    def queryset(self, request, queryset):
        if self.value():
            filter_kwargs = {
                f'{self.lookup_field or self.parameter_name}__{self.lookup_expr}': self.value()
            }
            return queryset.filter(**filter_kwargs)
        return queryset
