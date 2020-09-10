import boto3
from botocore.client import Config
import os

# Here we are setting these variables to the aws secret and access keys that we have in our env variables
ACCESS_KEY = os.environ["AWS_ACCESS_KEY"]
SECRET_KEY = os.environ["AWS_SECRET_KEY"]

BUCKET_NAME = ''
FILE_NAME = '';


data = open(FILE_NAME, 'rb')

# S3 Connect
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=ACCESS_SECRET_KEY
)

# Here we are downloading the file and placing it in our Downloads folder situated in our home directory (hence the tilda)
s3.Bucket(BUCKET_NAME).download_file(FILE_NAME, '~/Downloads/my_file.csv')


print ("Done")
