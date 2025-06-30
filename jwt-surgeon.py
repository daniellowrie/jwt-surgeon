#!/usr/bin/env python3

import base64
import sys
import readline

jwt = input("Paste JWT Here ~> ")

jwt_split = jwt.split(".")
jwt_header = jwt_split[0]
jwt_payload = jwt_split[1]
print("""
==================================================================""")
print(f'Original Base64 Header: {jwt_header}')
print(f'Original Base64 Payload: {jwt_payload}')

jwt_header_info = base64.b64decode(jwt_header + "==")
jwt_header_info_str_convert = str(jwt_header_info, "utf-8")
jwt_payload_info = base64.b64decode(jwt_payload + "==")
jwt_payload_info_str_convert = str(jwt_payload_info, "utf-8")

print("""
==================================================================""")
print(f'Original Header Info: {jwt_header_info_str_convert}')
print(f'Original Payload Info: {jwt_payload_info_str_convert}')
print("""
==================================================================""")

readline.set_startup_hook(lambda: readline.insert_text(jwt_header_info_str_convert))
new_header_info_str = input(f"Modify Header Info ~> ")
readline.set_startup_hook(None)

print("")

readline.set_startup_hook(lambda: readline.insert_text(jwt_payload_info_str_convert))
new_payload_info_str = input(f"Modify Payload Info ~> ")
readline.set_startup_hook(None)

print("")
print("==================================================================")
print("")

new_header_info_bytes = bytes(new_header_info_str, "utf-8")
new_payload_info_bytes = bytes(new_payload_info_str, "utf-8")

new_header_info_b64 = base64.urlsafe_b64encode(new_header_info_bytes)
new_payload_info_b64 = base64.urlsafe_b64encode(new_payload_info_bytes)

# Convert back to string and concatenate everyting into JWT

new_jwt_header = new_header_info_b64.replace(b"=", b"").decode("utf-8")
new_jwt_payload = new_payload_info_b64.replace(b"=", b"").decode("utf-8")

new_jwt = new_jwt_header + "." + new_jwt_payload + "."
print(f'New JWT: {new_jwt}')
