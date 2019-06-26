from django import forms
from .models import User, Prac_icf
from .models import Prac_MMT_shoulder_right, Prac_MMT_shoulder_left

class NewInputIcf(forms.ModelForm):
    class Meta():
        model = Prac_icf

        fields = ('body', 'activity')


class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        #モデルのインスタンスを生成

        fields = ('diagnosis_name', 'filler', 'date')
        #fieldsに__all__をセットすると，モデル内の全てのフィールドが用いられる

class PracMmtShoulderRight(forms.ModelForm):
    class Meta():
        model=Prac_MMT_shoulder_right

        fields=('flexion', 'extension', 'abduction', 'adduction', 'lateral_rotation', 'medial_rotation')

class PracMmtShoulderLeft(forms.ModelForm):
    class Meta():
        model=Prac_MMT_shoulder_left

        fields=('flexion', 'extension', 'abduction', 'adduction', 'lateral_rotation', 'medial_rotation')
