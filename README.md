# Sublime Codec for ST2 and ST3
Provides a bunch of useful codecs as a Sublime Text plugin to allow you to work with:
- RFC 4648:
    - encode/decode base64 (standard and url safe)
    - encode/decode base32
    - encode/decode base16 (hex)
- RFC 1321:
    - MD5
- FIPS 180-2:
    - SHA-1
    - SHA-224
    - SHA-256
    - SHA-384
    - SHA-512
- RFC 3986 URL encoding (percent encoding):
    - URL encoding (classic)
    - URL encoding (new school plus instead of ```%20``` method)

## Limitations
- Note that this plugin assumes that your file is UTF-8 encoded.

## Installation

### Package Control
- Install Package Control https://sublime.wbond.net/installation
- Pull up the command palette (```Shift+Super+P```)
- Type `Package Control: Install Package` and press `return` key
- Type `Codec` and press `return` key
- Enjoy

### Manual Install
- Copy a release from https://github.com/furikake/sublime-codec/releases
- Unzip files into `~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Codec` (or equivalent in Linux and Windows)

## Usage
- Look in the selection menu
- Look in command palette under `Codec` (```Shift+Super+P``` to bring up palette)
- ```Ctrl+Super+Y``` to base64 encode
- ```Shift+Super+Y``` to base64 decode
