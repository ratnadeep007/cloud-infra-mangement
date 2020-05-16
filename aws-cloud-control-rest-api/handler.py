import boto3
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/ec2")
def rest():
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
      add_instance = {
        'id': instance.id,
        'type': instance.instance_type,
        'image_id': instance.image_id,
        'status': instance.state,
        'tags': instance.tags 
      }
      print(instance.tags)
      ec2_instances.append(add_instance)
    print(ec2_instances)
  except Exception as e:
    print(e)
  return jsonify(ec2_instances)