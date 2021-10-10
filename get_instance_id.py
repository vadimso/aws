import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')
vpc = ec2.Vpc("vpc-id")
for i in vpc.instances.all():
    print(i)
