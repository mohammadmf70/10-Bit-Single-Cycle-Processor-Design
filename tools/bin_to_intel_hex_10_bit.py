def binary_to_intel_hex(binary_lines):
    intel_hex = []
    address = 0

    for line in binary_lines:
        # حذف کامنت
        line = line.split('#')[0].strip()

        # رد کردن خط خالی
        if not line:
            continue

        # بررسی معتبر بودن باینری
        if any(c not in '01' for c in line):
            raise ValueError(f"Invalid binary line: {line}")

        value = int(line, 2)

        if value > 0x3FF:
            raise ValueError("Value exceeds 10 bits")

        low = value & 0xFF
        high = (value >> 8) & 0x03

        byte_count = 2
        record_type = 0

        record = [
            byte_count,
            (address >> 8) & 0xFF,
            address & 0xFF,
            record_type,
            low,
            high
        ]

        checksum = ((~sum(record) + 1) & 0xFF)

        hex_line = (
            f":{byte_count:02X}{address:04X}{record_type:02X}"
            f"{low:02X}{high:02X}{checksum:02X}"
        )

        intel_hex.append(hex_line)
        address += 2

    intel_hex.append(":00000001FF")
    return "\n".join(intel_hex)


binary_lines = """
0101010000
1001001001
0100010100
1001000011
0101011010
1001000101
0100000100
1001000110
0100000110
1001000111
0100000000
1001001000
1010010000  
1001100001
1100010010
1000101001
1010010000
1000110001
1100010010
0000001100 
0100000001 
1001001000
1010010000 
1001110001
1100000010
1000101001
1001010000
1010010001
1100010010
0000010110 
0100000000 
1001001000  
1111111111
""".splitlines()

result = binary_to_intel_hex(binary_lines)
print(result)
