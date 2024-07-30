seq = bytearray(5)
seq[0] = 1
seq[2] = 31

ba = bytearray(b'\033[')
ba.extend(b';'.join(str(code).encode() for code in seq if code))
ba.extend(b'm')

ba.extend(b'hello world')

ba.extend(b'\033[0m')

print(ba.decode('utf-8'))


print(bytes('3asdf'))