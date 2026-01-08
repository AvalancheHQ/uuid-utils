fn main() {
    divan::main();
}

use uuid::{Context, Timestamp, Uuid};

const NODE: &[u8; 6] = &[0x12, 0x34, 0x56, 0x78, 0x9a, 0xbc];

#[divan::bench]
fn uuid_v1() {
    divan::black_box(Uuid::now_v1(NODE));
}

#[divan::bench]
fn uuid_v3() {
    divan::black_box(Uuid::new_v3(&Uuid::NAMESPACE_DNS, b"python.org"));
}

#[divan::bench]
fn uuid_v4() {
    divan::black_box(Uuid::new_v4());
}

#[divan::bench]
fn uuid_v5() {
    divan::black_box(Uuid::new_v5(&Uuid::NAMESPACE_DNS, b"python.org"));
}

#[divan::bench]
fn uuid_v6() {
    divan::black_box(Uuid::now_v6(NODE));
}

#[divan::bench]
fn uuid_v7() {
    divan::black_box(Uuid::now_v7());
}

#[divan::bench]
fn uuid_v8() {
    let bytes = [
        0xa1, 0xa2, 0xa3, 0xa4, 0xb1, 0xb2, 0xc1, 0xc2, 0xd1, 0xd2, 0xd3, 0xd4, 0xd5, 0xd6, 0xd7,
        0xd8,
    ];
    divan::black_box(Uuid::new_v8(bytes));
}

#[divan::bench]
fn uuid_v1_with_timestamp() {
    let timestamp = Timestamp::from_unix(&Context::new_random(), 0, 0);
    divan::black_box(Uuid::new_v1(timestamp, NODE));
}

#[divan::bench]
fn uuid_v6_with_timestamp() {
    let timestamp = Timestamp::from_unix(&Context::new_random(), 0, 0);
    divan::black_box(Uuid::new_v6(timestamp, NODE));
}

#[divan::bench]
fn uuid_v7_with_timestamp() {
    let timestamp = Timestamp::from_unix(&Context::new_random(), 0, 0);
    divan::black_box(Uuid::new_v7(timestamp));
}
