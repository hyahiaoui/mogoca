from google.cloud import storage

from mogoca import mock_storage


@mock_storage
def test_create_bucket_by_name():
    """Tests creation of a new bucket.

    cf. https://cloud.google.com/storage/docs/samples/storage-create-bucket
    """
    bucket_name = "new-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.create_bucket(bucket_name)

    assert bucket.name == bucket_name


@mock_storage
def test_create_bucket():
    """Tests creation of a new bucket.

    cf. https://cloud.google.com/storage/docs/samples/storage-create-bucket
    """
    bucket_name = "your-new-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    storage_client.create_bucket(bucket)

    assert bucket.name == bucket_name
