# Django Searchable List Filter

This is a Django application that provides a generic searchable filter for `list_filter` in the admin.

## Installation

Install the package via pip:

```bash
pip install git+https://github.com/tuhbiev/django_searchable_list_filter
```

## Usage 

**1. Configure Installed Apps.**

Add the application to INSTALLED_APPS in settings.py:
```
INSTALLED_APPS = [
    # other installed apps
    'django_searchable_list_filter',
]
```

**2. Create a Searchable Filter.**

To use a searchable filter, create a class that inherits from SearchableListFilter. For example:

```
from django_searchable_list_filter.admin import SearchableListFilter

class MyFieldSearchFilter(SearchableListFilter):
    title = 'Field name' # Displayed filter name in the admin panel
    parameter_name = 'my_field' # Name of the GET parameter to be used
    lookup_field = 'my_field' # Model field name for filtering
    # By default, the 'icontains' operator is applied. 
```

**3. Integrate the Filter in the Admin.**

In your admin class, add the new filter to the list_filter attribute:

```
from django.contrib import admin
from .models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_filter = (MyFieldSearchFilter, )
```

**4. Template Configuration.**

The filter template is already included in the package and is located at:
`templates/admin/searchable_list_filter.html`

Make sure your Django settings have template discovery enabled (i.e., APP_DIRS=True).
If you need to customize the template, you can copy it into your project and modify it as required.

**Summary**

Installation: Use pip to install from GitHub.
Configuration: Add 'django_searchable_list_filter' to INSTALLED_APPS.
Customization:
Create your own searchable filter by inheriting from SearchableListFilter and add it to your admin's list_filter.