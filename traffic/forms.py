# forms.py
from django import forms

class SearchForm(forms.Form):
    driving_date = forms.DateField(required=False, label="行駛日期")
    jurisdiction_unit = forms.CharField(max_length=30, required=False, label="管轄單位")
    route_number = forms.CharField(max_length=5, required=False, label="路線編號")
    outbound_return = forms.CharField(max_length=1, required=False, label="去回程")
