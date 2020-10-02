import boto3

BUCKET = 'amazonrekognition1'
KEY_SOURCE = "test.jpg"
KEY_TARGET = "target.jpg"


def compare_faces(bucket, key, bucket_target, key_target, region="us-east-1"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.compare_faces(
        SourceImage={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        TargetImage={
            "S3Object": {
                "Bucket": bucket_target,
                "Name": key_target,
            }
        },
        SimilarityThreshold=80,
    )
    return response['SourceImageFace'], response['FaceMatches']


source_face, matches = compare_faces(BUCKET, KEY_SOURCE, BUCKET, KEY_TARGET)

# Test image
print("Source Face {Confidence}%".format(**source_face))

# Target image
for match in matches:
    print("Target Face {Confidence}%".format(**match['Face']))
    print("Similarity : {}%".format(match['Similarity']))
