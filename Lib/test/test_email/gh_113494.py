import email, email.policy


email_raw_1 = """Content-Type: multipart/mixed; boundary="==="

--===
Content-Type: message/plain

 您0123456789012.3456789

--===--
""".encode()

email_raw_2 = """Content-Type: multipart/mixed; boundary="==="

--===
Content-Type: message/plain

 您0123456789012.34567890

--===--
""".encode()

message_1 = email.message_from_bytes(email_raw_1, policy=email.policy.SMTPUTF8)
message_2 = email.message_from_bytes(email_raw_2, policy=email.policy.SMTPUTF8)
print(message_1)
print(message_2)
