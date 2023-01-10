import boto3
import random
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    
    sms_client= boto3.client("sns")
    paswd=random.randint(100000,999999)
    print('otps: ',paswd)
    number=str(event['queryStringParameters']['mobile'])
    print("Mobile number is :",number)
    message= f"Your OTP for mobile number verification is: {paswd}"
    try:
        ress= sms_client.publish(
        PhoneNumber=number,
        Message=message,

        #Subject="KeepSL_OTP_Demo",
        #MessageAttributes={
        #        'AWS.SNS.SMS.SMSType': {
        #        'DataType': 'String',
        #       'StringValue': 'Transactional'
        #    }}
            )
    except ClientError as er:
        print(er.response['Error']['Message'])
        raise er
    else:
      print("Text Message sent! Message ID:",ress['MessageId']),
    
    
    res="OTP sent to the Customer was: "+str(paswd)


    return res
    
    