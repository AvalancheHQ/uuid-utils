import uuid

import pytest

import uuid_utils

node = uuid.getnode()


@pytest.mark.benchmark
def test_uuid1_stdlib():
    for _ in range(10_000):
        uuid.uuid1(node)


@pytest.mark.benchmark
def test_uuid1_uuid_utils():
    for _ in range(10_000):
        uuid_utils.uuid1(node)


@pytest.mark.benchmark
def test_uuid3_stdlib():
    for _ in range(10_000):
        uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid3_uuid_utils():
    for _ in range(10_000):
        uuid_utils.uuid3(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid4_stdlib():
    for _ in range(10_000):
        uuid.uuid4()


@pytest.mark.benchmark
def test_uuid4_uuid_utils():
    for _ in range(10_000):
        uuid_utils.uuid4()


@pytest.mark.benchmark
def test_uuid5_stdlib():
    for _ in range(10_000):
        uuid.uuid5(namespace=uuid.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid5_uuid_utils():
    for _ in range(10_000):
        uuid_utils.uuid5(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")
