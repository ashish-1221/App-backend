from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class State(models.Model):
    state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    state = models.CharField(choices=state_choices,max_length=255, null=True, blank=True)
    election_year = models.IntegerField(default=0,null=False,blank=False)
    election_type_choices = (("LS","Lok Sabha"),("VS","Vidhan Sabha"))
    election_type = models.CharField(choices=election_type_choices,max_length=255,null=True,blank=True)
    
    class Meta:
        ordering = ['state']
    def __str__(self):
        return self.state

class VillageMappingFile(models.Model):
    # pk_1 = models.CharField(primary_key=True,max_length=255)
    # state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    state = models.CharField(max_length=255, null=True, blank=True)
    #state = models.ForeignKey(State,on_delete=models.CASCADE)
    # csv_file = models.FileField(max_length=512,upload_to="uploads/",null=True)
    # created_at= models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now_add=True)
    # is_deleted=models.BooleanField(default=0)
    ac_no = models.IntegerField(verbose_name=("AC No"),null=False,blank=False,default=99999)
    object_id  = models.IntegerField(verbose_name=("Object Id"),null=True,blank=True)
    name = models.CharField(verbose_name=("Name"),null=True,blank=True,max_length=255)
    locality = models.CharField(verbose_name=("Locality"),null=True,blank=True,max_length=255)
    booth = models.CharField(verbose_name=("Booth"),null=True,blank=True,max_length=255)
    probable_nearby_vil_voter = models.CharField(verbose_name=("Probable Nearby Village"),max_length=255,null=True,blank=True)
    mandal = models.CharField(verbose_name=("Mandal"),max_length=255,null=True,blank=True)
    
    class Meta:
        ordering = ['state']
    



class VillageLocalityModel(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE,verbose_name="State")
    village = models.ManyToManyField(VillageMappingFile,verbose_name="Excel File")
    

   
    
    def __str__(self):
        return self.state.state + "_" + str(self.state.election_year) + "_" + self.state.election_type