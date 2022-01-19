# What this does

Downloads youtube video and pipes the stream directly to S3. By using pipeline we can download youtube videoes of any size, we wont be limited by memory or disk storage limits.

# How to use

1. Upload the `lambda/nodejs.zip` file as AWS Lambda layer. The layer file includes important node libraries such as ytdl-core (youtube-dl)
2. Use the code in functionfile.js as your lambda function, you need to replace the variables S3_ACCESS_KEY, S3_SECRET, S3_REGION and S3_BUCKET.

# How to use the API

Check `index.js`

# Important notice

Taken from [San-Jeevan's work](https://github.com/San-Jeevan/aws-lambda-youtube-dl)
