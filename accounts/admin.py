from django.contrib import admin

from accounts.models import Account, AccountSource


admin.site.register(Account)
admin.site.register(AccountSource)
