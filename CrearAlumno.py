import json
import boto3
def lambda_handler(event, context):

# Publicar en SNS
sns_client = boto3.client('sns')
response_sns = sns_client.publish(
    TopicArn = 'arn:aws:sns:us-east-1:570699102669:NuevoAlumno',
    Subject = 'Nuevo Alumno',
    Message = json.dumps(alumno),
    MessageAttributes = {
        'tenant_id': {'DataType': 'String', 'StringValue': tenant_id }
    }
)
print(response_sns)
# Salida (json)
return {
    'statusCode': 200,
    'response': response
}
