import boto3

region = 'us-east-1'
instances = ['i-0c7b862d1b69a19dc']
ec2 = boto3.client('ec2', region_name=region)

#Used to Stop Instances
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))

