import json
import io
import pickle

import boto3
from yt_dlp import YoutubeDL

def handler(event, context):
	bucket_name = 'garvittrells3bucket'
	file_name = event['queryStringParameters']['filename']
	s3 = boto3.resource('s3')
	bucket = s3.Bucket(bucket_name)
	bucket_object = bucket.Object(file_name)
	ydl_opts = {'format': 'b[filesize<30M] / w', 'outtmpl': '/tmp/%(id)s-%(title)s.%(ext)s',}
	with YoutubeDL(ydl_opts) as ydl:
		pickle_byte_obj = pickle.dumps(ydl.download(event['queryStringParameters']['url']))
		bucket_object.upload_fileobj(io.BytesIO(pickle_byte_obj))
	return {
		'statusCode': 200,
		'body': json.dumps('Video saved.')
	}