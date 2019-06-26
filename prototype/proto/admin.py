from django.contrib import admin

from .models import User
admin.site.register(User)

from .models import Prac_icf
admin.site.register(Prac_icf)

from .models import Prac_MMT_shoulder_right
admin.site.register(Prac_MMT_shoulder_right)

from .models import Prac_MMT_shoulder_left
admin.site.register(Prac_MMT_shoulder_left)
