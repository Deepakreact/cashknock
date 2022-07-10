
from django.contrib import admin

from cash.models import *
#from django.contrib.auth.models import User


# Register your models here.


admin.site.register(Banner)


admin.site.register(Category)

admin.site.register(Products)
admin.site.register(Brand)

admin.site.register(ScoreBoard)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(QuestionCategory)

# admin.site.register(Faq)
admin.site.register(Question)
