import boto3
import sys

reg_name=sys.argv[1]
access_key.argv[2]
secret_key.argv[3]

client = boto3.client('ec2', region_name=reg_name, aws_access_key_id=access_key, aws_secret_access_key=secret_key)
ec2_response = client.describe_instances()
for xyz in ec2_response['Reservations']:
	for abc in xyz['Instances']:
		print(abc['ImageId'],abc['InstanceId'],abc['InstanceType'])
	
