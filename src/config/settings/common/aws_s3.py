from decouple import config

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = config('AWS_BUCKET_NAME', '')
AWS_S3_REGION_NAME = 'eu-central-1'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = True
AWS_S3_OBJECT_PARAMETERS = {
    'ACL': 'public-read',  # Allow READ on all new objects
}
