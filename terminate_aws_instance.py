#!/usr/bin/python

import sys
import boto.ec2

instance_id = sys.argv[1]
print(instance_id + 'will be terminated')

conn = boto.ec2.connect_to_region("us-east-2",
        aws_access_key_id="",
        aws_secret_access_key=""
        )

conn.terminate_instances(instance_ids=[instance_id])

