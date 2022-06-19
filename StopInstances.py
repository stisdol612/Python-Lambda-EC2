import boto3

region = 'ENTER REGION'
instances = ['ENTER INSTANCE ID']
ec2 = boto3.client('ec2', region_name=region)

#Used to Stop Instances
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))

