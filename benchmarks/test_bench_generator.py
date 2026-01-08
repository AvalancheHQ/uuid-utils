import uuid

import pytest

import uuid_utils

node = uuid.getnode()


@pytest.mark.benchmark
def test_uuid_uuid1():
    for _ in range(10_000):
        uuid.uuid1(node)


@pytest.mark.benchmark
def test_uuid_utils_uuid1():
    for _ in range(10_000):
        uuid_utils.uuid1(node)


@pytest.mark.benchmark
def test_uuid_uuid3():
    for _ in range(10_000):
        uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid_utils_uuid3():
    for _ in range(10_000):
        uuid_utils.uuid3(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid_uuid4():
    for _ in range(10_000):
        uuid.uuid4()


@pytest.mark.benchmark
def test_uuid_utils_uuid4():
    for _ in range(10_000):
        uuid_utils.uuid4()


@pytest.mark.benchmark
def test_uuid_uuid5():
    for _ in range(10_000):
        uuid.uuid5(namespace=uuid.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid_utils_uuid5():
    for _ in range(10_000):
        uuid_utils.uuid5(namespace=uuid_utils.NAMESPACE_DNS, name="python.org")


@pytest.mark.benchmark
def test_uuid_uuid6():
    for _ in range(10_000):
        uuid.uuid1(node)


@pytest.mark.benchmark
def test_uuid_utils_uuid6():
    for _ in range(10_000):
        uuid_utils.uuid6(node)


@pytest.mark.benchmark
def test_uuid_uuid7():
    for _ in range(10_000):
        uuid.uuid1()


@pytest.mark.benchmark
def test_uuid_utils_uuid7():
    for _ in range(10_000):
        uuid_utils.uuid7()
