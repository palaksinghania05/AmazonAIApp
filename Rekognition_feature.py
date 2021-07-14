import cv2
import boto3

cap = cv2.VideoCapture(0)
ret,photo=cap.read()
print(ret)
photoToUpload=cv2.imwrite("hello.jpg",photo)
cap.release()
print(photoToUpload)

region="ap-south-1"
bucket="airekognitionsample"
s3Connection = boto3.resource('s3')
print(s3Connection)
upload_image="file.jpg"
uploaded = s3Connection.Bucket(bucket).upload_file(photoToUpload,upload_image)
print(uploaded)

#object detection
rekConnection = boto3.client('rekognition',region)
print(rekConnection)
response=rekConnection.detect_lables(
    Image = {
        'S3Object':{
            'Bucket':bucket,
            'Name': upload_image,
        }
    },
    MaxLabels = 10,
    MinConfidence=90
)
print(response)

#facial analysis
response_face = rekConnection.detect_faces(
    Image = {
        'S3Object':{
            'Bucket':bucket,
            'Name': upload_image,
        }
    },
    Attributes=['ALL']
)
print(response_face)

#



