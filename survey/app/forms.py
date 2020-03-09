from django import forms
from app.models import KhaoSat



class KhaoSatForm(forms.ModelForm):
    Cau1 = forms.TypedChoiceField(coerce=lambda x: x =='True',
                                   choices=((False, 'No'), (True, 'Yes')), initial = False, label='Tháng này bạn đã update file Nhật ký Mentor-Mentee chưa?')

    Cau2 = forms.TypedChoiceField(coerce=lambda x: x =='True',
                                   choices=((False, 'No'), (True, 'Yes')), initial = False, label = "Tháng này bạn có gặp mentor không?")

    Lydo_Cau2 = forms.CharField(label="Lý do không gặp mentor:", max_length=256, required = False)

    Cau3 = forms.TypedChoiceField(coerce=lambda x: x =='True',
                                   choices=((False, 'No'), (True, 'Yes')), initial = False, label="Tháng này bạn đã viết email cho sponsor chưa?")
    Lydo_Cau3 = forms.CharField(label="Lý do không viết email cho sponsor:", max_length=256, required = False)

    Cau4 = forms.TypedChoiceField(coerce=lambda x: x =='True',
                                   choices=((False, 'No'), (True, 'Yes')), initial = False, label="Tháng này nhóm bạn có tổ chức họp nhóm không?")

    field_order = ['Cau1', 'Cau2', 'Lydo_Cau2', 'Cau3', 'Lydo_Cau3', 'Cau4']

    class Meta:
        model = KhaoSat
        fields = ['Cau1', 'Cau2', 'Cau3', 'Cau4',]
    def save(self, user_fake):
        if self.is_valid():
            data = self.cleaned_data
            if data['Cau2'] == True:
                data['Lydo_Cau2'] = 'null'
            if data['Cau3'] == True:
                data['Lydo_Cau3'] = 'null'
            var = KhaoSat(Cau1=data['Cau1'], Cau2=data['Cau2'], Lydo_Cau2 = data['Lydo_Cau2'], Cau3=data['Cau3'], Lydo_Cau3 = data['Lydo_Cau3'], Cau4=data['Cau4'], user=user_fake)
            var.save()
