import boto3

region = 'us-east-1'
instances = ['i-06fa8e63218becebf', 'i-075545d2dbaf1d0e4']
ec2 = boto3.client('ec2', region_name=region)

#Used to Stop Instances
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))

#Used to Start instances
def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))