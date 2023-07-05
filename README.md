# Message Encoding and Decoding

Applications transform information between different forms - from bytes into
images on the screen, from one data protocol for the network to another format
for storing in a database, or from the plain text of a message into a secret
ciphertext.

In this exercise, you'll write helper functions to transform messages into
different formats, and then back again.

## Background: Encoding and Decoding

Transforming a plaintext message into a coded format is called _encoding_. It
changes the way messages are represented. Transforming them back is called
_decoding_.

The whole process together is called encoding/decoding. Since it is so common to
encode and decode messages before sending them over the network, there are
special devices called 'encoders' and 'decoders' that do the job. Often, the two
are combined into a single encoder/decoder, or _codec_.

There are many possible encodings for the same message. Depending on the
purpose, a different encoding could be more useful. Different encodings take up 
less space, are easier to perform, or make it easier or more reliable to send
over the network.

### ASCII

In [ASCII](https://en.wikipedia.org/wiki/ASCII), letters map to numbers.

* A: 65
* B: 66
* C: 67
* ...
* Z: 90
* a: 97
* b: 98

91 through 96 map to the symbols [, \, ], \^, \_, and \`. This makes
capitalization and lowercasing easy: add or subtract 30.

See `ascii.py` for a demo.

### Morse

In [Morse code](https://en.wikipedia.org/wiki/Morse_code), letters are 
represented as combinations of dashes and dots:
	
* a: . -
* b: - . . .
* c: - . - .

Morse code does not differentiate between uppercase and lowercase letters. Morse
code isn't used much in computers, but it was the typical encoding for
telegraphs, and it is still used in some manual signalling, using light or
sound.

### Base64

[Base64 encoding](https://en.wikipedia.org/wiki/Base64) is helpful for
representing binary data as text. Here's how it works:

A byte is 8 bites, so there are 64 possible values for each byte of information. 
Base64 assigns a different letter, number, or symbol to each possible byte. The 
first 62 possible bytes are represented by the 26 lowercase and  26 uppercase 
ASCII letters and 10 decimal numbers. Two symbols represent the last two possible 
bytes. Typically either `+` and `/` or `-` and `_`, depending on where the data
will be used, and whether those symbols have some other meaning.

* 0 (`00000000`): A
* 1 (`00000001`): B
* 2 (`00000010`): C
* 0 (`00000000`): A
* 0 (`00000000`): A

Since there are many text-only channels and formats, base64 is helpful for 
representing binary data in those channels. For instance, if you wanted to put
an image into a URL, it would typically be impossible - URLs are strings, and
can't just have bytes. But, you could encode the bytes of the image using
base64, add them to the end of the URL, then decode them on the other side. This
strategy is actually fairly common -- it's even more common as an alternate way 
to add an image to HTML, using a [Data URL](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs).

---

There are many other kinds of encodings. You can read more about
[encoding](https://en.wikipedia.org/wiki/Character_encoding) on Wikipedia. If
you like, you can also try designing your own encoding.

## Background: Encryption

Encoding transforms the way a message is represented, but it's typically easy
to decode a message. Even if you don't know exactly how a message has been 
encoded, there are many effective strategies for guessing the encoding and
getting the plaintext back.

_Encryption_ is a way of transforming messages, like encoding, that tries to
make it difficult or impossible to reverse the process without knowing the key.
Keeping messages totally secret is possible, using proven cryptographic methods
based in mathematics.

The encrypted message is often called _ciphertext_. Transforming the ciphertext 
back into a plaintext message is called _decryption_.

It can be educational and fun to implement cryptographic methods yourself - and
to write code to break your encryption, if it isn't strong enough.

If you try to use hand-rolled cryptographic functions in a real application, it's 
easy to make a mistake and allow secret data to be vulnerable to decryption by 
an attacker. This is especially the case if you try to design your own encryption 
functions, rather than use known and vetted algorithms.

Instead, it's best to rely on a well-tested solution that has been vetted
by the cryptographic community. In Python, the library to use is called 
[`cryptography`](https://cryptography.io/en/latest/). From the library, it's
typically best to use the 'recipes' layer, which handles nearly all the tricky
parts for you, so that it's difficult to mess up.

## Your Task

Practice with encoding and decoding, and with encryption and decryption. There 
are several encoding and decoding helper functions to implement:

**Morse**

- `encode_morse` should take a plaintext message and turn it into Morse code.
    The starter code has a table of Morse values for the uppercase ascii
    letters, digits, and the space character called `MORSE_TABLE`.
- `decode_morse` should undo the `encode_morse` function, taking a Morse-encoded
    message back into plaintext. The starter code has a dict called
    `MORSE_INVERSE` which maps the morse values to the ascii equivalents.

**Base64**

- `encode_base64` should turn a plaintext message into its base64 equivalent.
    Use Python's built-in `base64` library, and the `urlsafe` versions
    of the encoding and decoding methods. 
- `decode_base64` should undo the base64 encoding, and convert the message back
    into its plaintext form.

Note: Since base64 encoding operates on _bytes_, you'll have to turn the string 
message into bytes, and turn the base64-encoded message back into a string. You 
can use Python's built-in string methods `encode` and `decode` to convert from
string into bytes. You can assume that all the strings are valid ASCII text.

Converting to bytes:

```python
byte_array = "hello world".encode('ascii')
```

Converting from bytes back to a string:

```python
byte_array.decode('ascii')
```

**Encryption using `Fernet`**

- `encrypt` should use Fernet to encrypt a message, encode the bytes as an ascii
    string, and return the result
- `decrypt` should use Fernet to decrypt a ciphertext, and return the original
    string.

Notes:
- Refer to the [Fernet](https://cryptography.io/en/latest/fernet/) documentation
    for information about how to use the library
- Generate your key and set up Fernet _outside_ of the `encrypt` and `decrypt` 
    functions, so that the same key is shared between the functions.

## Starter Code

The file `main.py` has the empty functions for you to fill in. It also has
driver code that will call each of the functions with the input passed on the 
command line and display the results, to make it easy to test out your code.

## Testing

To run the program with a sample value, pass in a message like this:

```shell
python main.py 'some secrets should stay buried'
```

You can also run the tests to verify your solution. The tets cover lots of cases
for the Morse and base64 modes, but only check that the Fernet encryption and
decryption are the inverse of each other. You should check that your output is
similar to the expected results below.

## Expected Results

With the secret message above, the output of main.py is:

```txt
Morse encoded:
... --- -- . / ... . -.-. .-. . - ... / ... .... --- ..- .-.. -.. / ... - .- -.-- / -... ..- .-. .. . -..
Morse decoded:
SOME SECRETS SHOULD STAY BURIED

Base64 encoded:
c29tZSBzZWNyZXRzIHNob3VsZCBzdGF5IGJ1cmllZA==
Base64 decoded:
some secrets should stay buried

Encrypted (using Fernet):
gAAAAABjVsJSRSvNWKpY6m0G0fu2HV-f7SeyUoEk5AtuW0rp7Bjq9xBLCHMH97uTbqOIQGLZivw3tgas_prUqZYaoslkRkdxXCDGXRG7Uq_Bw9g4Tpel8MQ=
Decrypted:
some secrets should stay buried
```

The Fernet key is regenerated each run, so you should get a
slightly different encrypted output each time you run the code.

## Bonus Task: Web Interface

After you get your encoding and decoding functions working properly, you can
create a web interface for the functions using Flask.

The flask app needs:
- A form where the user enters a message and selects which operation to perform
- Flask endpoints to take the input from the form and send back the result
- A page to display the result value

It may be helpful to work with teammates and read about templates and forms in
Flask if you attempt the bonus challenge.
