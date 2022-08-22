
import Falcon
import time

  
Falcon.ArmCameraStart()


Falcon.angles = Falcon.IK(x=34,y=0,z=8.5)
print(Falcon.angles)

if(Falcon.angles[0]<0):
    Falcon.angles[0]=360 + Falcon.angles[0]
if(Falcon.angles[1]<0):
    Falcon.angles[1]=360 + Falcon.angles[1]
if(Falcon.angles[2]<0):
    Falcon.angles[2]=360 + Falcon.angles[2]
if(Falcon.angles[3]<0):
    Falcon.angles[3]=360 + Falcon.angles[3]
if(Falcon.angles[4]<0):
    Falcon.angles[4]=360 + Falcon.angles[4]


print(Falcon.angles)
#Falcon.ArmIk(Falcon.angles[0]+80,Falcon.angles[1] ,Falcon.angles[2] ,Falcon.angles[3]+90 ,Falcon.angles[4], f=70)
time.sleep(2)
#Falcon.ArmIk(Falcon.angles[0]+80,Falcon.angles[1] ,Falcon.angles[2] ,Falcon.angles[3]+90 ,Falcon.angles[4], f=0)
time.sleep(2)
print("PICKED")
#Falcon.ArmIk(Falcon.angles[0],b=90 ,Falcon.angles[2] ,Falcon.angles[3] ,e=90, f=0)

#Falcon.ArmIk(a,b=90 ,c ,d ,e=90, f=0)
print("DONE")


print("2222222222222222")
time.sleep(1)
Falcon.ArmCameraStart()


