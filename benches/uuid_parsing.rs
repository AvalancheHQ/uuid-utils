fn main() {
    divan::main();
}

use uuid::Uuid;

const UUID_STRING: &str = "a8098c1a-f86e-11da-bd1a-00112444be1e";
const UUID_BYTES: [u8; 16] = [
    0xa8, 0x09, 0x8c, 0x1a, 0xf8, 0x6e, 0x11, 0xda, 0xbd, 0x1a, 0x00, 0x11, 0x24, 0x44, 0xbe, 0x1e,
];
const UUID_INT: u128 = 223569345403422308016554334024933380638;

#[divan::bench]
fn from_str() {
    divan::black_box(Uuid::parse_str(UUID_STRING).unwrap());
}

#[divan::bench]
fn from_bytes() {
    divan::black_box(Uuid::from_bytes(UUID_BYTES));
}

#[divan::bench]
fn from_bytes_le() {
    divan::black_box(Uuid::from_bytes_le(UUID_BYTES));
}

#[divan::bench]
fn from_u128() {
    divan::black_box(Uuid::from_u128(UUID_INT));
}

#[divan::bench]
fn to_string() {
    let uuid = Uuid::from_u128(UUID_INT);
    divan::black_box(uuid.to_string());
}

#[divan::bench]
fn to_hyphenated() {
    let uuid = Uuid::from_u128(UUID_INT);
    divan::black_box(uuid.hyphenated().to_string());
}

#[divan::bench]
fn to_simple() {
    let uuid = Uuid::from_u128(UUID_INT);
    divan::black_box(uuid.simple().to_string());
}

#[divan::bench]
fn to_urn() {
    let uuid = Uuid::from_u128(UUID_INT);
    divan::black_box(uuid.urn().to_string());
}
