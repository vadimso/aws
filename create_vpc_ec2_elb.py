#install boto & boto3 
pip install boto
pip install boto3

#!/usr/bin/env python
import boto3
from boto.ec2.elb import ELBConnection
from boto.ec2.elb import HealthCheck

ec2 = boto3.resource('ec2', aws_access_key_id='',
                     aws_secret_access_key='',
                     region_name='us-east-1')



# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-0a313d6098716f372',
     InstanceType='t2.micro',
     MinCount=1,
     MaxCount=2,)

# create VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc.create_tags(Tags=[{"Key":"TestVPC","Value":"default_vpc"}])
vpc.wait_until_available()
print(vpc.id)
subnet = ec2.create_subnet(CidrBlock = '10.0.2.0/24', VpcId= vpc.id)
print(subnet.id)



# create ELB
conn_elb = ELBConnection(aws_access_key_id='', aws_secret_access_key='')

#For a complete list of options see http://boto.cloudhackers.com/ref/ec2.html#module-boto.ec2.elb.healthcheck
hc = HealthCheck('healthCheck',
                     interval=20,
                     target='HTTP:80/index.html',
                     timeout=3)

#For a complete list of options see http://boto.cloudhackers.com/ref/ec2.html#boto.ec2.elb.ELBConnection.create_load_balancer
lb = conn_elb.create_load_balancer('my-lb',
                                       ['us-east-1a', 'us-east-1b', 'us-east-1c'],
                                       [(80, 80, 'http'), (443, 443, 'tcp')])

lb.configure_health_check(hc)

#DNS name for your new load balancer
print "Map the CNAME of your website to: %s" % (lb.dns_name)
