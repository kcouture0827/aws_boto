#!/usr/bin/python

import sys
import boto.ec2

#instance_id = sys.argv[1]


conn = boto.ec2.connect_to_region("us-east-2",
        aws_access_key_id="",
        aws_secret_access_key=""
        )

conn.run_instances(
                'ami-02e680c4540db351e',
                key_name='botoDemo',
                instance_type='t2.micro',
                security_groups=['default'])
