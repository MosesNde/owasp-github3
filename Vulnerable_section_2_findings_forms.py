 # -*- coding: utf-8 -*-
 
 from django import forms
 from .models import Finding, FINDING_SEVERITIES
 
 )
 
 
 class ImportFindingsForm(forms.Form):
     class Meta:
         fields = ['engine', 'min_level', 'file']
         attrs={'class': 'form-control form-control-sm'},
         choices=FINDING_SEVERITIES),
         label='Minimum severity')
    file = forms.FileField()
 
 
 class FindingForm(forms.ModelForm):
     class Meta:
         model = Finding
        fields = ['title', 'type', 'severity', 'status', 'description', 'tags',
            'solution', 'risk_info', 'vuln_refs', 'links', 'comments', 'asset']
         widgets = {
             'description': forms.Textarea(
                 attrs={'class': 'form-control form-control-sm'}),