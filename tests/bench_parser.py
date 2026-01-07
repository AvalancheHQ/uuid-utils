import uuid

import pytest

import uuid_utils


@pytest.mark.benchmark
def test_uuid_from_hex_stdlib():
    for _ in range(10_000):
        uuid.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")


@pytest.mark.benchmark
def test_uuid_from_hex_uuid_utils():
    for _ in range(10_000):
        uuid_utils.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")


@pytest.mark.benchmark
def test_uuid_from_bytes_stdlib():
    for _ in range(10_000):
        uuid.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")


@pytest.mark.benchmark
def test_uuid_from_bytes_uuid_utils():
    for _ in range(10_000):
        uuid_utils.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")


@pytest.mark.benchmark
def test_uuid_from_int_stdlib():
    for _ in range(10_000):
        uuid.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")


@pytest.mark.benchmark
def test_uuid_from_int_uuid_utils():
    for _ in range(10_000):
        uuid_utils.UUID("a8098c1a-f86e-11da-bd1a-00112444be1e")


@pytest.mark.benchmark
def test_uuid_from_fields_stdlib():
    for _ in range(10_000):
        uuid.UUID(fields=(2819197978, 63598, 4570, 189, 26, 73622928926))


@pytest.mark.benchmark
def test_uuid_from_fields_uuid_utils():
    for _ in range(10_000):
        uuid_utils.UUID(fields=(2819197978, 63598, 4570, 189, 26, 73622928926))
