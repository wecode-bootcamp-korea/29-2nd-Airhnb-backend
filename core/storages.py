import boto3
import uuid

from django.conf import settings

class ImageUploader:
    def __init__(self, client, aws_bucket_name):
        self.client          = client
        self.aws_bucket_name = aws_bucket_name

    def upload(self, image, directory):
        file_name = uuid.uuid4().hex[:10]

        self.client.upload_fileobj(
                image,
                self.aws_bucket_name,
                f'{directory}/{file_name}',
                ExtraArgs = {'ContentType' : image.content_type}
            )
        return f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/{directory}/{file_name}'

    def delete(self, image):
        return self.client.delete_object(Bucket=self.aws_bucket_name, Key=image) 

class ImageHandler:
    def __init__(self, image, directory, client):
        self.image     = image
        self.directory = directory
        self.client    = client

    def save(self):
        return self.client.upload(self.image, self.directory)