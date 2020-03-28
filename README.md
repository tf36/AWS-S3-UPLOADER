# AWS-S3-UPLOADER

import boto3
import os

# import module!

#-*- coding:utf-8 -*-

# i am using foreign name files a lot

path = "./upload"
file_list = os.listdir(path)
fa=[]
li = []
for i in range (len(file_list)):
    fa.append(file_list[i])

# part to gather file's name

s3 = boto3.resource('s3')
buc=s3.Bucket('bucketname')
s3 = boto3.client('s3')
path = "./upload"
bucket_name = 'bucketname'
file_list = os.listdir(path)
for f in buc.objects.all():
    li.append(f.key)

# gather files that exist on S3 bucket that files will be upload

com= list(set(fa).intersection(li))

# compare files if files that will be upload are exist on S3 bucket

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

# upload files


        
