from flask import Flask, request, jsonify
import boto3

server = Flask(__name__)

s3 = boto3.client('s3')

@server.route("/")
def list_buckets():
    query = request.args.get('query')  
    
    if query:
        try:
            s3.head_bucket(Bucket=query) 
            return jsonify({"Bucket": query})
        except s3.exceptions.ClientError:
            return jsonify({"Error": "Bucket not found"}), 404
    
    response = s3.list_buckets()
    bucket_names = [bucket['Name'] for bucket in response.get('Buckets', [])]
    return jsonify({"Buckets": bucket_names})

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000, debug=True)
