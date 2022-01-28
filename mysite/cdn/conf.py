import os

AWS_ACCESS_KEY_ID=os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME='dj-ocean'
AWS_S3_ENDPOINT_URL='https://fra1.digitaloceanspaces.com'

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_LOCATION = 'https://dj-ocean.fra1.digitaloceanspaces.com'

DEFAULT_FILE_STORAGE = 'mysite.cdn.backends.MediaRootS3Boto3Storage'

STATICFILES_STORAGE = 'mysite.cdn.backends.StaticRootS3Boto3Storage'