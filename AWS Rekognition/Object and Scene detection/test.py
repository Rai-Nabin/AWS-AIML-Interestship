import boto3

BUCKET = "amazonrekognition1"
KEY = "fake.jpg"


def detect_labels(bucket, key, region="us-east-1"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        MaxLabels=10,
        MinConfidence=90,
    )
    return response['Labels']


for label in detect_labels(BUCKET, KEY):
    print("{Name}: {Confidence}%".format(**label))
