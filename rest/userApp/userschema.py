from rest.ormdb import mar
 
class UserSchema(mar.Schema):
    class Meta:
        fields = ('id','username','email')
        
        
        

       
        