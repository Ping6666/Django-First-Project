from django.db import models
from django.urls import reverse

# Create your models here.


class companyDataset(models.Model):
    # 尾端有"#"的表示必要，但是因為is_valid過不了，所以才讓blank=True, null=True
    
    # 營業地址
    company_address = models.CharField(max_length=75, blank=True)#

    # 統一編號 Government Uniform Invoice number
    GUI_number = models.CharField(max_length=10, blank=True)#
    # 總機構統一編號 Headquarter
    HQ_GUI_number = models.CharField(max_length=10, blank=True, null=True)

    # 營業人名稱
    company_name = models.CharField(max_length=75, blank=True)#
    # 資本額
    company_capital = models.CharField(max_length=15, blank=True)#

    # 設立日期
    found_date = models.CharField(max_length=10, blank=True)#
    # 組織別名稱
    company_organization_type = models.CharField(max_length=10, blank=True)#
    # 使用統一發票
    company_receipt = models.CharField(max_length=1, blank=True)#

    # 行業代號
    company_type_number_0 = models.CharField(max_length=10, blank=True)#
    # 名稱
    company_type_name_0 = models.CharField(max_length=40, blank=True)#
    # 行業代號1
    company_type_number_1 = models.CharField(max_length=10, blank=True, null=True)
    # 名稱1
    company_type_name_1 = models.CharField(max_length=40, blank=True, null=True)
    # 行業代號2
    company_type_number_2 = models.CharField(max_length=10, blank=True, null=True)
    # 名稱2
    company_type_name_2 = models.CharField(max_length=40, blank=True, null=True)
    # 行業代號3
    company_type_number_3 = models.CharField(max_length=10, blank=True, null=True)
    # 名稱3
    company_type_name_3 = models.CharField(max_length=40, blank=True, null=True)