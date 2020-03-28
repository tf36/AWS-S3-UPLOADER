import boto3
import os
#-*- coding:utf-8 -*-
path = "./upload"
file_list = os.listdir(path)
fa=[]
li = []
for i in range (len(file_list)):
    fa.append(file_list[i])

s3 = boto3.resource('s3')
buc=s3.Bucket('bucketname')

s3 = boto3.client('s3')

path = "./upload"
bucket_name = 'bucketname'
file_list = os.listdir(path)
for f in buc.objects.all():
    li.append(f.key)

com= list(set(fa).intersection(li))
try:
    for i in range (len(com)):
        fa.remove(com[i])
    for k in range (len(fa)):
        filename = fa[k]
        s3.upload_file("./upload/"+filename, bucket_name, filename) 
except:
    for k in range (len(fa)):
        filename = fa[k]
        s3.upload_file("./upload/"+filename, bucket_name, filename)



        