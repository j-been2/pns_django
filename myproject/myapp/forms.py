from django import forms
from .models import PnsBigo, PnsModel, PnsCombi, PnsManager

# PnsBigo 폼
class PnsBigoForm(forms.ModelForm):
    class Meta:
        model = PnsBigo
        fields = ['type', 'content']

# PnsModel 폼
class PnsModelForm(forms.ModelForm):
    class Meta:
        model = PnsModel
        fields = ['type', 'type1', 'name', 'price', 'price_info', 'oneshot_price', 'oneshot_info', 'image_url', 'charge_info']

# PnsCombi 폼
class PnsCombiForm(forms.ModelForm):
    class Meta:
        model = PnsCombi
        fields = ['type', 'name', 'price', 'price_info', 'oneshot_price', 'oneshot_info', 
                  'm_charge_info', 'i_charge_info', 't_charge_info', 'image_url', 'charge_info', 'bigo']

# PnsManager 폼
class PnsManagerForm(forms.ModelForm):
    class Meta:
        model = PnsManager
        fields = ['type', 'jisa', 'agency_name', 'link_url', 'kc_manager_name', 'kc_manager_phone', 
                  'kt_manager_name1', 'kt_manager_phone1', 'kt_manager_name2', 'kt_manager_phone2']