import boto3
import os

# os.environ["AWS_ACCESS_KEY_ID"]="your access key"
# os.environ["AWS_SECRET_ACCESS_KEY"]="your secret key"


def extract_data():

    s3 = boto3.client('s3')
    bucket_name = 'deeplearning-mlops-demo'
    url = s3.generate_presigned_url(
                    ClientMethod='get_object',
                    Params={'Bucket': bucket_name, 'Key': 'object_detection_data.zip'},
                    ExpiresIn=7200  # URL expiration time in seconds (adjust as needed)
                )
    print(url)
    return url

extract_data()
