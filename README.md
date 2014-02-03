# Sublime Codec
Provides a bunch of useful codecs to allow you to work with:
- RFC 4648:
    - encode/decode base64 (standard and url safe)
    - encode/decode base32
    - encode/decode base16
- RFC 1321:
    - MD5
- FIPS 180-2:
    - SHA-1
    - SHA-224
    - SHA-256
    - SHA-384
    - SHA-512
- url encoding:
    - percent encoding
    - percent encoding plus

## Limitations
- Note that this plugin assumes that your file is UTF-8 encoded.

## Installation

### Package Control
Hopefully coming soon

### Manual Install
- Copy a release from https://github.com/furikake/sublime-codec/releases
- Unzip files into `~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Codec` (or equivalent in Linux and Windows)

## Usage
- Look in the selection menu
- Look in command palette under `Codec` (```Shift+Super+P``` to bring up palette)
- ```Ctrl+Super+Y``` to base64 encode
- ```Shift+Super+Y``` to base64 decode
