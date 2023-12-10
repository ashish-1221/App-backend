from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.gis.db import models as md
# Create your models here.

# class State(models.Model):
#     state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
#     state_name = models.CharField(choices=state_choices,max_length=255, null=True, blank=True)
#     election_year = models.IntegerField(default=0,null=False,blank=False)
#     election_type_choices = (("LS","Lok Sabha"),("VS","Vidhan Sabha"))
#     election_type = models.CharField(choices=election_type_choices,max_length=255,null=True,blank=True)
    
#     class Meta:
#         ordering = ['state_name']
#     def __str__(self):
#         return self.state_name

class VillageMappingFile(models.Model):
    """
    Model where the village mapping file information is stored after importing from the admin
    """
    state_name = models.CharField(max_length=255, null=True, blank=True)
    ac_no = models.IntegerField(verbose_name=("AC No"),null=False,blank=False,default=99999)
    object_id  = models.IntegerField(verbose_name=("Object Id"),null=True,blank=True)
    name = models.CharField(verbose_name=("Name"),null=True,blank=True,max_length=255)
    locality = models.CharField(verbose_name=("Locality"),null=True,blank=True,max_length=255)
    booth = models.CharField(verbose_name=("Booth"),null=True,blank=True,max_length=255)
    probable_nearby_vil_voter = models.CharField(verbose_name=("Probable Nearby Village"),max_length=255,null=True,blank=True)
    mandal = models.CharField(verbose_name=("Mandal"),max_length=255,null=True,blank=True)
    
    class Meta:
        ordering = ['state_name','ac_no']
        
    

class VillageBoundaryModel(md.Model):
    state_name = md.CharField(max_length=255, blank=True)
    #ac_no = md.IntegerField(verbose_name=("AC No"),null=False,blank=False,default=99999)
    object_id  = md.BigIntegerField(verbose_name=("Object Id"),null=True,blank=True)
    v_id = md.PositiveBigIntegerField(verbose_name=("ID"),null=True,blank=True)
    name = md.CharField(verbose_name=("Name"),null=True,blank=True,max_length=255)
    distric = md.CharField(verbose_name=("District"),null=True,blank=True,max_length=255)
    subdistric = md.CharField(verbose_name=("Sub District"),null=True,blank=True,max_length=255)
    censusname = md.CharField(verbose_name=("Census Name"),null=True,blank=True,max_length=255)
    lgd_villag = md.CharField(verbose_name=("Lgd Village"),null=True,blank=True,max_length=255)
    level_2011 = md.CharField(verbose_name=("Level 2011"),null=True,blank=True,max_length=255)
    tru_2011 = md.CharField(verbose_name=("Tru 2011"),null=True,blank=True,max_length=255)
    geometry = md.MultiPolygonField()
    
    def __str__(self):
        return self.state_name 




