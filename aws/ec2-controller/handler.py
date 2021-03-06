import boto3

def handler(event, context):
  ec2 = boto3.resource('ec2', region_name='ap-south-1')
  ec2_instances_stopped = []
  ec2_instances_running = []

  print("Boto")
  print(dir(boto3.DEFAULT_SESSION.get_credentials))

  filter = [
    {
      "Name": "tag:Type",
      "Values": ['personal']
    }
  ]
  try:
    for instance in ec2.instances.filter(Filters=filter):
      instance_state = instance.state
      if instance_state.get('Name') != 'stopped':
        ec2_instances_running.append(instance)
        # instance.stop()
      else:
        ec2_instances_stopped.append(instance)
    
    if len(ec2_instances_running) == 0:
      print('No EC2 instances was running')
      return "No EC2 instances was running"
    else:
      print("Stopped running machines")
      return "Stopped running machines"
  except Exception as e:
    print(e)
    return "Error occured"
  return
