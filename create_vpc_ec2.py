#create VPC
aws ec2 create-vpc --cidr-block 10.0.0.0/16
# Replace the VPC Id with yours.
#create subnets for the VPC
aws ec2 create-subnet --vpc-id vpc-id --cidr-block 10.0.1.0/24
aws ec2 create-subnet --vpc-id vpc-id --cidr-block 10.0.2.0/24
#create an internet gateway 
aws ec2 create-internet-gateway
#note down the InternetGatewayId from the output.
# attach ig to vpc
aws ec2 attach-internet-gateway --internet-gateway-id igw-id --vpc-id vpc-id
#create route table
aws ec2 create-route-table --vpc-id vpc-id
# add ig rule
aws ec2 create-route --route-table-id rtb-b86fe2dc --destination-cidr-block 0.0.0.0/0 --gateway-id igw-id
#associate route table to a subnet 
aws ec2 associate-route-table --route-table-id rtb-id --subnet-id subnet-id
#launch an EC2 instance in the public subnet
aws ec2 run-instances --image-id ami-9abea4fb --count 1 --instance-type t2.micro --key-name test-key --security-group-ids sg-af7a50c8 --subnet-id subnet-id --associate-public-ip-address
