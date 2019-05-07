import json
import boto3

bucket_name = ""
s3 = boto3.resource('s3')

s3.Bucket(bucket_name).upload_file('', 'upload.jpg')