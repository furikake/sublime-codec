# Sublime Codec
Provides a bunch of useful codecs to allow you to work with:
- RFC 4648:
 - encode/decode base64 (standard and url safe)
 - encode/decode base32
 - encode/decode base16
- RFC 1321 (TODO):
 - SHA1
 - SHA224
 - SHA256
 - SHA384
 - SHA512
- FIPS 180-2 (TODO):
 - MD5
- url encoding (TODO):
 - percent encoding
 - percent encoding space as plus symbol

## Limitations
Note that this plugin assumes that your file is UTF-8 encoded.

## Installation
TODO

## Usage
- ```Ctrl+Super+Y``` to base64 encode
- ```Shift+Super+Y``` to base64 decode
- ```Ctrl+Super+U``` to url safe base64 encode
- ```Shift+Super+U``` to url safe base64 decode
- ```Ctrl+Super+I``` to base32 encode
- ```Shift+Super+I``` to base32 decode
- ```Ctrl+Super+O``` to base16 encode
- ```Shift+Super+O``` to base16 decode
