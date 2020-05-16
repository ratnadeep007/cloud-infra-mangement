import boto3
from flask import Flask
app = Flask(__name__)

@app.route("/ec2")
def rest(event, context):
  ec2 = boto3.resource('ec2', region_name='ap-south-1')
  ec2_instances = []

  filter = [
    {
      "Name": "tag:Type",
      "Values": ["personal"]
    }
  ]
  try:
    for instance in ec2.instances.filter(Filters=filter):
      ec2_instances.append(instance)
    print(ec2_instances)
    return "okay"