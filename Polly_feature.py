import boto3

pollyConnection = boto3.client('polly')
response = pollyConnection.synthesize_speech(Text="This is just a test, welcome", OutputFormat='mp3', VoiceId='Joanna')
print(response['AudioStream'])
file=open('myaudio.mp3','wb')
file.write(response['AudioStream'].read())
file.close()

import IPython
IPython.display.Audio("myaudio.mp3")