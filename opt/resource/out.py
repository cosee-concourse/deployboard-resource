import sys
from concourse_common import common
from concourse_common import jsonutil
from concourse_common import request
import boto3
import os
import schemas
import json


def execute(filepath):

    valid, payload = jsonutil.load_and_validate_payload(schemas, request.Request.OUT)

    if valid is False:
        return -1

    bucket = jsonutil.get_params_value(payload, "bucket")
    directory = jsonutil.get_params_value(payload, "directory")
    version = open(os.path.join(filepath, jsonutil.get_params_value(payload, "version"))).read()

    client = boto3.client(
        's3',
        aws_access_key_id=jsonutil.get_source_value(payload, "AWS_ACCESS_KEY"),
        aws_secret_access_key=jsonutil.get_source_value(payload, "AWS_SECRET_KEY")
    )

    num = 1

    for rootdir, dirs, files in os.walk(os.path.join(filepath, directory)):
        for name in files:
            common.log(name)
            if name.endswith("surefire-report.html"):
                client.upload_file(os.path.join(filepath, rootdir, name),
                                   bucket,
                                   "surefire-report-" + version + "-" + str(num) + ".html")
                num += 1

    print(json.dumps(
        {"version": {"version": version}}))



if __name__ == '__main__':
    if len(sys.argv) != 2:
        common.log("Wrong number of arguments!")
        exit(-1)
    exit(execute(sys.argv[1]))

