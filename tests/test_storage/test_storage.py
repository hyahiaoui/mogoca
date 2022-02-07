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


@mock_storage
def test_create_bucket_by_name_using_anonymous_client():
    """Tests creation of a new bucket.

    cf. https://cloud.google.com/storage/docs/samples/storage-create-bucket
    """
    bucket_name = "new-bucket-name"

    storage_client = storage.Client.create_anonymous_client()

    bucket = storage_client.create_bucket(bucket_name)

    assert bucket.name == bucket_name


@mock_storage
def test_create_bucket_using_anonymous_client():
    """Tests creation of a new bucket.

    cf. https://cloud.google.com/storage/docs/samples/storage-create-bucket
    """
    bucket_name = "your-new-bucket-name"

    storage_client = storage.Client.create_anonymous_client()

    bucket = storage_client.bucket(bucket_name)
    storage_client.create_bucket(bucket)

    assert bucket.name == bucket_name


@mock_storage
def test_create_bucket_class_location():
    """
    Tests creation of a new bucket in the US region with the coldline storage
    class.

    cf. https://cloud.google.com/storage/docs/samples/storage-create-bucket-class-location
    """
    bucket_name = "your-new-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "COLDLINE"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    assert new_bucket.name == bucket_name
    assert new_bucket.location == "us"
    assert new_bucket.storage_class == "COLDLINE"
