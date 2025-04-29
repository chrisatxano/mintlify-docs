# Security

* [**create\_uid**](security.md#create_uid) **-** Returns a unique 64bit unsigned int value seeded off the value.
* [**decrypt**](security.md#decrypt) **-** Decrypts the value and returns the result.
* [**encrypt**](security.md#encrypt) **-** Encrypts the value and returns the result.
* [**hmac\_md5**](security.md#hmac_md5) **-** Returns a MD5 signature representation of the value using a shared secret via the HMAC method
* [**hmac\_sha1**](security.md#hmac_sha1) **-** Returns a SHA1 signature representation of the value using a shared secret via the HMAC method
* [**hmac\_sha256**](security.md#hmac_sha256-hmac384-hmac512)[ **/ hmac\_sha384 / hmac\_sha512**](security.md#hmac_sha256-hmac384-hmac512) **-** Returns a SHA256/384/512 signature representation of the value using a shared secret via the HMAC method
* [**jwe\_decode**](security.md#jwe_encode-jwe_decode) **-** Decodes the value represented as JWE token and returns the original payload.
* [**jwe\_encode**](security.md#jwe_encode-jwe_decode) **-** Encodes the value and returns the result as a JWE token.
* [**md5**](security.md#md5) **-** Returns an MD5 signature representation of the value.
* [**secureid\_decode**](security.md#secureid_decode) **-** Returns the id of the original encode.
* [**secureid\_encode**](security.md#secureid_encode) **-** Returns an encrypted version of the id.
* [**sha1**](security.md#sha1-sha256-sha384-sha512) **-** Returns a SHA1 signature representation of the value.
* [**sha256 / sha384 / sha512**](security.md#sha1-sha256-sha384-sha512) **-** Returns a SHA256/384/512 signature representation of the value.

#### create\_uid:

Returns a unique 64bit unsigned int value seeded off the value.

<figure><img src="../../.gitbook/assets/CleanShot 2025-02-06 at 11.09.41.png" alt=""><figcaption></figcaption></figure>

#### decrypt:

Decrypts the value and returns the result.

![](<../../.gitbook/assets/CleanShot 2022-02-22 at 15.26.55.png>)

#### encrypt:

Encrypts the value and returns the result in raw binary form. Find more details on the [encrypt function](broken-reference) page.

![](<../../.gitbook/assets/CleanShot 2022-02-22 at 15.23.02.png>)



#### hmac\_md5

Returns a MD5 signature representation of the value using a shared secret via the HMAC method.\
The secret key is a unique piece of information that is used to compute the HMAC and is known both by the sender and the receiver of the message. This key will vary in length depending on the algorithm that you use.

<figure><img src="../../.gitbook/assets/CleanShot 2025-02-06 at 11.13.17.png" alt=""><figcaption></figcaption></figure>



#### hmac\_sha1

Returns a SHA1 signature representation of the value using a shared secret via the HMAC method.\
The secret key is a unique piece of information that is used to compute the HMAC and is known both by the sender and the receiver of the message. This key will vary in length depending on the algorithm that you use.

<figure><img src="../../.gitbook/assets/CleanShot 2025-02-06 at 11.14.05.png" alt=""><figcaption></figcaption></figure>

#### hmac\_sha256 / hmac384 / hmac512

Returns a SHA256/384/512 signature representation of the value using a shared secret via the HMAC method.\
The secret key is a unique piece of information that is used to compute the HMAC and is known both by the sender and the receiver of the message. This key will vary in length depending on the algorithm that you use.

<figure><img src="../../.gitbook/assets/CleanShot 2025-02-06 at 11.14.55.png" alt=""><figcaption></figcaption></figure>

#### jwe\_encode / jwe\_decode:

Encodes the value and returns the result as a JWE token.

HEADERS: Any custom headers to include in the JWE token Sample: `{"kid": "12345"}`

KEY: The encryption key for the JWE token Sample: `a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6`

KEY\_ALGORITHM: Choose one of the algorithms used to encode the token.

CONTENT\_ALGORITHM: Choose one of the algorithms used to encode the token.

TTL: Token expiration time in seconds Sample: `3600` (1 hour), `0` means no expiration



#### md5

Returns an MD5 signature representation of the value. A salt value can be added to the text to provide an extra layer of security.

<figure><img src="../../.gitbook/assets/CleanShot 2025-02-06 at 11.22.06.png" alt=""><figcaption></figcaption></figure>

#### secureid\_decode

Returns the id of the original encode. If a salt was added to encode this value the same salt needs to be added to decrypt it.

<figure><img src="../../.gitbook/assets/CleanShot 2025-02-06 at 11.21.36.png" alt=""><figcaption></figcaption></figure>

#### secureid\_encode

Returns an encrypted version of an integer. A salt value can be added to the text to provide an extra layer of security.

<figure><img src="../../.gitbook/assets/CleanShot 2025-02-06 at 11.20.57.png" alt=""><figcaption></figcaption></figure>

#### sha1 / sha256 / sha384 / sha512

Returns a SHA1 signature representation of the value. A salt value can be added to the text to provide an extra layer of security.

<figure><img src="../../.gitbook/assets/CleanShot 2025-02-06 at 11.19.46.png" alt=""><figcaption></figcaption></figure>
