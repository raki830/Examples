import boto3
import pprint

# Create an boto client for Amazon Polly
client = boto3.client(
    "polly",
    aws_access_key_id="Enter Access Key",
    aws_secret_access_key="Enter Secret Access Key",
    region_name="ap-southeast-2"
)

with open("TwinkleNurseryRhyme.txt","r") as textFile:
    response = client.synthesize_speech(Text=textFile.read(), OutputFormat="mp3",
                                            VoiceId="Nicole")


    #print the json response
    pprint.pprint(response)

    with open("NurseryRhyme.mp3","wb") as speechFile:
        speechFile.write(response['AudioStream'].read())




