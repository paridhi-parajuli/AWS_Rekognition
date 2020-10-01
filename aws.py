import boto3
import json
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to input image")
args = vars(ap.parse_args())

client=boto3.client('rekognition')


with open(args["image"], 'rb') as image:

    response = client.detect_faces(Image={'Bytes': image.read()},
        Attributes = ['ALL']) 

print('*******GCA_CANDIDATES_IMAGE_ANALYSIS*******')

if response==None:
    print("No faces Detected")

for i,face in enumerate(response['FaceDetails']):
    i=i+1
    print('')
    print('Age Range of person'+str(i) +' : '+ str(face['AgeRange']['Low']) + ' - ' + str(face['AgeRange']['High']))
    print('Gender of person' +str(i) +' : '+ str(face['Gender']['Value']))

    if str(face['Gender']['Value']) == 'Male':
        beard = str(face['Beard']['Value'])
        if beard == 'True':
            print('The person'+str(i)+' has beard')
        else:
            print('The person'+str(i)+' does not have beard')
        moustache = str(face['Mustache']['Value'])
        if moustache == 'True':
            print('The person'+str(i)+' has moustache')
        else:
            print('The person'+str(i)+' does not have moustache')
    
    eyeglass = str(face['Eyeglasses']['Value'])
    if eyeglass == 'True':
        print('The person'+str(i)+' is wearing glasses')
    else:
        print('The person'+str(i)+' is not wearing glasses')
    for emotion in face['Emotions']:
        if (emotion['Confidence'] > 60):
            print('The person'+str(i)+' is {} with confidence of {}'.format(emotion['Type'],emotion['Confidence']))
    