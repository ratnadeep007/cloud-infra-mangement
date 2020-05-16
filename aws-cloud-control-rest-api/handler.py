import boto3
from datetime import datetime

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

@app.route('/billing')
def billing():
  ce = boto3.client('ce')

  today = datetime.today()
  month = today.month

  lastday = 31
  leapyear = (today.year % 4 == 0) and (today.year % 100 == 0) and (today.year % 400 == 0) 

  if month == 2 and leapyear:
    lastday = 29
  elif month and not leapyear:
    lastday = 28
  elif month <= 7 and (month % 2 != 0):
    lastday = 31
  elif month >= 8 and (month % 2 == 0):
    lastday = 30

  if month < 10:
    month = '0{0}'.format(month)

  start_date = "{0}-{1}-{2}".format(today.year, month, "01")
  end_date = "{0}-{1}-{2}".format(today.year, month, lastday)

  # resp = ce.get_cost_and_usage_with_resources(
  #   TimePeriod={
  #     'Start': start_date,
  #     'End': end_date
  #   },
  #   Granularity='MONTHLY'
  # )
  # print(resp)
  return "Not implemented"