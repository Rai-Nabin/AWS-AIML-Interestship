import boto3
import base64
import json

photo = 'Images/bigsmile.jpg'
rekognition_client = boto3.client('rekognition', region_name='us-east-1')
file = open(photo, 'rb').read()

response = rekognition_client.detect_faces(

    Image={
        'Bytes': file
    },
    Attributes=['ALL']
)
for face in response['FaceDetails']:
    print('The detected face is of ' + str(face['Gender']['Value']))
    print('The detected face is between ' +
          str(face['AgeRange']['Low']) + ' and ' + str(face['AgeRange']['High']) + 'years old')
    for emotion in face['Emotions']:
        if emotion['Confidence'] > 95:
            print('The detected face appears to be ' + str(emotion['Type']))

    Sunglass = str(face['Sunglasses']['Value'])
    if Sunglass == 'True':
        print('The detected face is wearing Sunglasses')
    else:
        print('The detected face is not wearing Sunglasses')
    Beard = str(face['Beard']['Value'])
    if Beard == 'True':
        print('The detected face has a beard')
    else:
        print('The detected face does not have a beard')
