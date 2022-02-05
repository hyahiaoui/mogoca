from google.cloud import storage
from google.cloud.exceptions import Conflict
from google.cloud.storage._helpers import _validate_name


class FakeBucket:
    """
    Mocked implementation of Google Cloud Storage Bucket.
    """

    def __init__(self, client, name=None, user_project=None):
        self.name = _validate_name(name)
        self._client = client
        self._user_project = user_project


class FakeClient:
    """
    Mocked implementation of Google Cloud Storage Client.
    """

    def __init__(self):
        self._buckets = {}

    def bucket(self, bucket_name, user_project=None):
        return FakeBucket(client=self, name=bucket_name, user_project=user_project)

    def create_bucket(
        self,
        bucket_or_name,
        # requester_pays=None,
        # project=None,
        user_project=None,
        # location=None,
        # predefined_acl=None,
        # predefined_default_object_acl=None,
        # timeout=60,
        # retry=None,
    ):
        bucket_name = (
            bucket_or_name if isinstance(bucket_or_name, str) else bucket_or_name.name
        )

        if bucket_name in self._buckets:
            raise Conflict(
                "Sorry, that name is not available. Please try a different one."
            )

        new_bucket = (
            FakeBucket(client=self, name=bucket_name, user_project=user_project)
            if isinstance(bucket_or_name, str)
            else bucket_or_name
        )

        self._buckets[bucket_name] = new_bucket
        return new_bucket


class StorageBackend:
    def __init__(self):
        self._savedClient = None

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            self._start()
            result = fn(*args, **kwargs)
            self._stop()

            return result

        return wrapper

    def __enter__(self):
        self._start()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop()

    def _start(self):
        self._savedClient = storage.Client
        storage.Client = FakeClient

    def _stop(self):
        storage.Client = self._savedClient


storage_backend = StorageBackend()