import boto3

BUCKET = "amazonrekognition1"
KEY = "img.jpg"

rekognition = boto3.client("rekognition", region_name="us-east-1")
response = rekognition.detect_text(
    Image={
        "S3Object": {
            "Bucket": BUCKET,
            "Name": KEY,
        }
    }
)
texts = []
for text in response['TextDetections']:
    if(text['Type'] == 'WORD'):
        texts.append(text['DetectedText'])
print(" ".join(texts))
