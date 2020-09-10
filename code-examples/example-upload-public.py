# My IAM User inline policy is:
#
# {
#   "Version": "2012-10-17",
#   "Statement": [
#           {
#               "Effect": "Allow",
#               "Action": [
#                   "s3:ListAllMyBuckets",
#                   "s3:PutObject",
#                   "s3:GetObject",
#                   "s3:PutObjectAcl",
#                   "s3:GetObjectAcl"
#               ],
#               "Resource": [
#                   "arn:aws:s3:::*"
#               ]
#           }
#   ]
# }


import boto3
import os

# Creating a function that when ran will upload a file to our s3 bucket
def upload_to_aws():

    # Setting these variables to the value of our access and secret key in our ENV  variables
    ACCESS_KEY = os.environ["AWS_ACCESS_KEY"]
    SECRET_KEY = os.environ["AWS_SECRET_KEY"]

    s3_client = boto3.client(
            's3',
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
        )

    # We are looking for a downloads folder in this current diretory and a file named 'ItJobsWatchTop30.csv' within it
    # We are then uploading this file to a bucket that we have specified and finally given it a name (in this case we call it the same thing)
    s3_client.upload_file('Downloads/ItJobsWatchTop30.csv', 'andrew-mvc-with-itjobs', 'ItJobsWatchTop30.csv')

    # We then print to the console to let the developer know that the file has uploaded successfully
    print("Your file has been successfully uploaded to an AWS bucket!")
