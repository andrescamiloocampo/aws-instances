from flask import Flask,request
import boto3

server = Flask(__name__)

s3 = boto3.client('s3')

@server.route("/")
def list_buckets():
    response = s3.list_buckets()
    return response

if __name__ = "__main__":
    server.run(host='0.0.0.0')