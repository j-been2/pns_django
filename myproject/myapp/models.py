from django.db import models

# Create your models here.

class PnsBigo(models.Model):
    de = models.CharField(max_length=10, default='N')
    type = models.CharField(max_length=100) #모바일, 소상공인, 유무선
    content = models.TextField()

    class Meta:
            db_table = "pns_bigo" 

    def __str__(self):
        return self.type
    

class PnsModel(models.Model):
    de = models.CharField(max_length=10, default='N')
    type = models.CharField(max_length=100) #모바일, 소상공인
    type1 = models.IntegerField(blank=True, null=True) 
    name = models.CharField(max_length=100)  # 모델명
    price = models.IntegerField()  # 출고가
    price_info = models.CharField(max_length=100, blank=True, null=True)  # 출고가 뒤 문구
    oneshot_price = models.IntegerField()  # 원샷 지원금
    oneshot_info = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.CharField(max_length=255)  # 이미지 경로
    charge_info = models.CharField(max_length=100, blank=True, null=True) #요금제기준

    class Meta:
            db_table = "pns_model" 

    def __str__(self):
        return self.type
    

class PnsCombi(models.Model):
    de = models.CharField(max_length=10, default='N')
    type = models.CharField(max_length=100) #MIT, IT
    name = models.CharField(max_length=100)  # 모델명
    price = models.IntegerField()  # 월요금금
    price_info = models.CharField(max_length=100, blank=True, null=True)  # 출고가 뒤 문구
    oneshot_price = models.IntegerField()  # 원샷 지원금
    oneshot_info = models.CharField(max_length=100, blank=True, null=True)
    m_charge_info = models.CharField(max_length=100, blank=True, null=True) 
    i_charge_info = models.CharField(max_length=100, blank=True, null=True) 
    t_charge_info = models.CharField(max_length=100, blank=True, null=True) 

    image_url = models.CharField(max_length=255,blank=True, null=True)  # 이미지 경로
    charge_info = models.CharField(max_length=100, blank=True, null=True)
    bigo = models.CharField(max_length=255, blank=True, null=True) 

    class Meta:
            db_table = "pns_combi" 

    def __str__(self):
        return self.type
    
class PnsManager(models.Model):
    de = models.CharField(max_length=10, default='N')
    type = models.CharField(max_length=50) #일반or 소상공인인
    jisa = models.CharField(max_length=50)
    agency_name = models.CharField(max_length=100)  # 대리점명명
    link_url = models.CharField(max_length=255)  
    kc_manager_name = models.CharField(max_length=100, blank=True, null=True)
    kc_manager_phone = models.CharField(max_length=100, blank=True, null=True)

    kt_manager_name1 = models.CharField(max_length=100, blank=True, null=True)
    kt_manager_phone1 = models.CharField(max_length=100, blank=True, null=True)
    kt_manager_name2 = models.CharField(max_length=100, blank=True, null=True)
    kt_manager_phone2 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
            db_table = "pns_manager"  # 원하는 테이블 이름 지정

    def __str__(self):
        return self.type