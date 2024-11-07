import os
import json
import logging
import aioredis
import configs.settings as settings
import requests
from datetime import datetime
from google.cloud import storage


# Configure logging to track important events in Redis and Pub/Sub interactions
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RedisManager:
    """
    A class to manage asynchronous interactions with Redis. This class provides methods
    to save, retrieve, and delete session-specific data in Redis.
    """

    def __init__(self):
        """
        Initialize the RedisManager with the necessary Redis configuration.
        Establish a connection to the Redis server using host, port, and password.
        """
        self.redis_client = aioredis.from_url(
            f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
            password=settings.REDIS_PASSWORD,
            decode_responses=True
        )

    async def save_to_redis(self, session_id: str, key: str, data: dict):
        """
        Save data to Redis under a key prefixed with the session ID.
        
        :param session_id: Unique identifier for the session.
        :param key: Specific key under the session to store data.
        :param data: The data to be stored in Redis.
        """
        redis_key = f"{session_id}:{key}"
        await self.redis_client.set(redis_key, json.dumps(data))  # Save the data in Redis as a JSON string
        logging.info(f"Data saved to Redis with key: {redis_key}")

    async def get_from_redis(self, session_id: str, key: str):
        """
        Retrieve data from Redis based on the session ID and key.
        
        :param session_id: Unique identifier for the session.
        :param key: Specific key under the session to retrieve data.
        :return: The retrieved data, or None if not found.
        """
        redis_key = f"{session_id}:{key}"
        data = await self.redis_client.get(redis_key)  # Fetch the data from Redis
        if data:
            logging.info(f"Data retrieved from Redis with key: {redis_key}")
            return json.loads(data)  # Return the data after converting it from JSON format
        else:
            logging.warning(f"No data found in Redis for key: {redis_key}")
            return None

    async def delete_from_redis(self, session_id: str, key: str):
        """
        Delete specific data from Redis based on the session ID and key.
        
        :param session_id: Unique identifier for the session.
        :param key: Specific key under the session to delete data.
        """
        redis_key = f"{session_id}:{key}"
        await self.redis_client.delete(redis_key)  # Delete the specified key from Redis
        logging.info(f"Data deleted from Redis for key: {redis_key}")


class GCSManager:
    """
    A class to manage uploads and downloads of files to and from Google Cloud Storage.
    This class provides methods to upload files to a specified bucket and retrieve files from the bucket.
    """

    def __init__(self, bucket_name: str):
        """
        Initialize the GCSManager with the necessary GCS configuration.
        Establish a connection to the GCS bucket.
        
        :param bucket_name: The name of the GCS bucket where files will be stored/retrieved.
        """
        self.bucket_name = bucket_name  # Store the bucket name as a string
        self.storage_client = storage.Client()
        self.bucket = self.storage_client.bucket(bucket_name)  # Bucket object

    def get_gcs_files(self, prefix: str) -> list:
        """
        Retrieve all files from the specified path (prefix) in the GCS bucket and store their content as a list of JSON objects.
        
        :param prefix: The path prefix within the bucket to search for files.
        :return: A list of JSON objects parsed from the files.
        """
        json_data_list = []

        # List all blobs in the specified path (prefix)
        blobs = self.storage_client.list_blobs(self.bucket_name, prefix=prefix)
        
        for blob in blobs:
            try:
                # Download the file content as a string
                file_content = blob.download_as_text()
                # Parse the string content as JSON and append to the list
                json_data = json.loads(file_content)
                json_data_list.append(json_data)
            except Exception as e:
                print(f"Error processing file {blob.name}: {e}")
        
        return json_data_list

    def upload_to_gcs(self, destination_blob_name: str, file_path: str):
        """
        Upload a file to GCS.

        :param destination_blob_name: The name of the blob (file) in the GCS bucket.
        :param file_path: The local path to the file that needs to be uploaded.
        """
        blob = self.bucket.blob(destination_blob_name)
        logging.info("Preparing file upload into GCS..")
        try:
            blob.upload_from_filename(file_path)
            logging.info(f"File {file_path} uploaded to {destination_blob_name}.")
        except Exception as e:
            logging.error(f"Failed to upload file {file_path} to {destination_blob_name}: {e}")

    def download_blob(self, blob_name: str, destination_file_path: str):
        """
        Download a file from GCS.

        :param blob_name: The name of the blob (file) in the GCS bucket to be downloaded.
        :param destination_file_path: The local path where the downloaded file should be saved.
        """
        blob = self.bucket.blob(blob_name)

        try:
            blob.download_to_filename(destination_file_path)
            logging.info(f"File {blob_name} downloaded to {destination_file_path}.")
        except Exception as e:
            logging.error(f"Failed to download file {blob_name}: {e}")

    def get_latest_blob(self, path_prefix=None):
        """
        Get the contents of the most recently uploaded JSON file from a specified path in GCS.

        :param path_prefix: The path prefix to filter blobs (e.g., "final_profiles/").
        :return: The contents of the most recent blob as a Python dictionary, or None if no blobs are found.
        """
        try:
            # List all blobs in the bucket, filtered by the provided path prefix
            if path_prefix:
                blobs = list(self.bucket.list_blobs(prefix=path_prefix))
            else:
                blobs = list(self.bucket.list_blobs())

            if not blobs:
                logging.info("No blobs found in the bucket.")
                return None

            # Sort blobs by time created and get the most recent one
            latest_blob = max(blobs, key=lambda b: b.time_created)

            # Download the contents of the most recent blob as text
            json_content = latest_blob.download_as_text()

            # Parse the JSON content into a Python dictionary
            json_data = json.loads(json_content)

            logging.info(f"Most recent file: {latest_blob.name}")
            return json_data
    
        except Exception as e:
            logging.error(f"Failed to get the most recent JSON file contents: {e}")
            return None
        
    def upload_image_to_gcs(self, destination_blob_name: str, image_data: bytes):
        """
        Upload an image to GCS from memory (image data in bytes).

        :param destination_blob_name: The name of the blob (file) in the GCS bucket.
        :param image_data: The image data in bytes that needs to be uploaded.
        """
        blob = self.bucket.blob(destination_blob_name)

        try:
            # Upload the image bytes to the specified GCS blob
            blob.upload_from_string(image_data, content_type='image/png')
            logging.info(f"Image uploaded to {destination_blob_name}.")
            return destination_blob_name
        except Exception as e:
            logging.error(f"Failed to upload image to {destination_blob_name}: {e}")
            return None
        
    def generate_authenticated_url(self, blob_name: str):
        """
        Generate an authenticated URL for a blob in GCS.
        This URL requires users to be authenticated with Google and have access to the bucket.

        :param blob_name: The name of the blob (file) in the GCS bucket.
        :return: The authenticated URL that can be used to access the blob.
        """
        try:
            # Use the bucket name (string) to construct the authenticated URL
            authenticated_url = f"https://storage.cloud.google.com/{self.bucket_name}/{blob_name}"
            logging.info(f"Authenticated URL: {authenticated_url}")
            return authenticated_url
        except Exception as e:
            logging.error(f"Failed to generate authenticated URL for {blob_name}: {e}")
            return None
        
    def download_and_upload_images(self, image_data, session_id):
        
        """
        Download images from provided URLs and upload them to GCS, generating authenticated URLs.
        """
        uploaded_image_urls = []

        # Fetching the upscaled URLs from the response
        upscaled_urls = image_data.get('upscaled_urls', [])
        
        if not upscaled_urls:
            logging.info("No upscaled URLs found in the response")
            return uploaded_image_urls
        
        # Downloading and uploading images
        logging.info("Downloading images..")
        for i, image_url in enumerate(upscaled_urls):
            try:
                # Send a GET request to fetch the image
                response = requests.get(image_url, stream=True)
                response.raise_for_status()
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                
                # Ensure we're reading the content in a stream to avoid loading it all at once into memory
                local_filename = f'/tmp/image_{i + 1}_{session_id}_{timestamp}.png'
                with open(local_filename, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                # Uploading to GCS
                blob_name = f'processed_images/image_{i + 1}_{session_id}_{timestamp}.png'
                blob = self.bucket.blob(blob_name)
                blob.upload_from_filename(local_filename)

                # Generate authenticated URL instead of making the file public
                authenticated_url = self.generate_authenticated_url(blob_name)
                if authenticated_url:
                    uploaded_image_urls.append(authenticated_url)
                else:
                    print(f"Failed to generate authenticated URL for image {i + 1}")

                # Removing the local file after upload
                os.remove(local_filename)
            except Exception as e:
                logging.error(f"An error occurred while downloading image {i + 1}: {e}")
        
        return uploaded_image_urls

    def delete_blob(self, blob_name: str):
        """
        Delete a file from GCS.

        :param blob_name: The name of the blob (file) in the GCS bucket to be deleted.
        """
        blob = self.bucket.blob(blob_name)

        try:
            blob.delete()
            logging.info(f"Blob {blob_name} deleted from GCS.")
        except Exception as e:
            logging.error(f"Failed to delete blob {blob_name}: {e}")