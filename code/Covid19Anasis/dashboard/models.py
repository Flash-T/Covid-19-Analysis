from django.db import models

# Create your models here.
class CovidData(models.Model):
    date = models.DateField()
    # 省份
    province = models.CharField(max_length=100)
    # 城市
    city = models.CharField(max_length=100)
    # 确诊人数
    confirmed = models.IntegerField(default=0)
    # 死亡人数
    deaths = models.IntegerField(default=0)
    # 治愈人数
    recovered = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.country} - {self.province} - {self.city} - {self.confirmed} - {self.deaths} - {self.recovered}"

