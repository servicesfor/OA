import xadmin as admin
from user.models import User,Patient
from user.forms import UserForm
# Register your models here.

class UserAdmin():
    form = UserForm
    list_display = ['phone','create_time','update_time']
    list_per_page = 20
    site_title = '用户管理'

admin.site.register(User,UserAdmin)


class PatAdmin():
    list_display = ['p_user','p_name','p_ID_number','p_sex','date_birth','p_weight','is_allergy','medical_history','is_normal_liver','is_normal_kidney','is_pregnancy_preparation']
    search_fields =['p_user','p_name','p_ID_number','p_sex','date_birth','p_weight','is_allergy','medical_history','is_normal_liver','is_normal_kidney','is_pregnancy_preparation']
    list_filter = ['p_user','p_name','p_ID_number','p_sex','date_birth','p_weight','is_allergy','medical_history','is_normal_liver','is_normal_kidney','is_pregnancy_preparation']
    list_per_page = 20
    site_title = '患者管理'

admin.site.register(Patient,PatAdmin)