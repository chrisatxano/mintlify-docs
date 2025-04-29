# Conversion

* [**base64\_decode**](conversion.md#base64_decode) **-** Decodes the value represented as base64 and returns the result.
* [**base64\_decode\_urlsafe**](conversion.md#base64_decode_urlsafe) **-** Decodes the value represented as base64 URL safe text and returns the result.
* [**base64\_encode**](conversion.md#base64_encode) **-** Encodes the value and returns the result as base64 text.
* [**base64\_encode\_urlsafe**](conversion.md#base64_encode_urlsafe) **-** Encodes the value and returns the result as base64 URL safe text.
* [**base\_convert**](conversion.md#base_convert) **-** Converts a value between two base&#x73;_._
* [**bin2hex**](conversion.md#bin2hex) - Converts a binary value into its hex equivalent.
* [**decbin**](conversion.md#decbin) **-** Converts a decimal value into its binary string (i.e. 01010) equivalent.
* [**bindec**](conversion.md#bindec) **-** Converts a binary string (i.e. 01010) into its decimal equivalent.
* [**create\_object**](conversion.md#create_object) **-** Creates an object based on a list of keys and a list of values.
* [**csv\_decode**](conversion.md#csv_decode) **-** Decodes the value represented as CSV and returns the result
* [**csv\_encode** ](conversion.md#csv_encode)**-** Encodes the value and returns the result in CSV-formatted text
* [**dechex**](conversion.md#dechex) **-** Converts a decimal value into its hex equivalent.
* [**decoct**](conversion.md#decoct) **-** Converts a decimal value into its octal equivalent.
* [**hex2bin**](conversion.md#hex2bin) **-** Converts a hex value into its binary equivalent.
* [**hexdec**](conversion.md#hexdec) **-** Converts a hex value into its decimal equivalent.
* [**json\_decode**](conversion.md#json_decode) **-** Decodes the value represented as json and returns the result.
* [**json\_encode**](conversion.md#json_encode) **-** Encodes the value and returns the result as json text.
* [**octdec**](conversion.md#octdec) **-** Converts an octal value into its decimal equivalent.
* [**to\_bool**](conversion.md#to_bool) **-** Converts text, integer, or decimal types to a bool and returns the result.
* [**to\_dec**](conversion.md#to_decimal) **-** Converts text, integer, or bool types to a decimal and returns the result.
* [**to\_int**](conversion.md#to_int) **-** Converts text, integer, or bool types to an integer and returns the result.
* [**to\_text**](conversion.md#to_text) **-** Converts text, integer, or bool types to text and returns the result.
* [**to\_timestamp**](conversion.md#to_timestamp) **-** Converts a text expression (now, next Friday) to timestamp comparable format.
* [**url\_decode**](conversion.md#url_decode) **-** Decodes the value represented as a URL encoded value.
* [**url\_decode\_rfc3986**](conversion.md#url_decode_rfc3986) **-** Decodes the value represented as a URL encoded value conforming to RFC3986 specifications
* [**url\_encode**](conversion.md#url_encode) **-** Encodes the value and returns the result as a URL encoded value.
* [**url\_encode\_rfc3986**](conversion.md#url_encode_rfc3986) **-** Encodes the value and returns the result as a URL encoded value conforming to RFC3986 specifications
* [**yaml\_decode**](conversion.md#yaml_decode) **-** Decodes the value represented as yaml and returns the result.
* [**yaml\_encode**](conversion.md#yaml_encode) **-** Encodes the value and returns the result as yaml text.
* [**xml\_decode**](conversion.md#xml_decode) - Decodes the value represented as XML to JSON and returns the result

#### **base64\_decode**:

Decodes the value represented as base64 and returns the result.

![Example: we have a text value of aGVsbG8gd29ybGQ= using the filter base64\_decode we get hello world. ](../../.gitbook/assets/decode.png)

#### **base64\_decode\_urlsafe:**

Decodes the value represented as base64 URL safe text and returns the result.

This filter transforms the base64 URL safe encoded characters `-_.` back to `+/=`.&#x20;

#### **base64\_encode**:

Encodes the value and returns the result as base64 text.

![Example: we have a text value of hello world using the filter base64\_encode we get aGVsbG8gd29ybGQ= .](../../.gitbook/assets/encode.png)

#### base64\_encode\_urlsafe:

Encodes the value and returns the result as base64 URL safe text.

In base64 encoding, a URL safe format is not taken into consideration but there's only three characters we need to be cautious of `+/=`. With this filter those characters become `-_.` respectively.&#x20;

#### base\_convert:

Converts a value between two base&#x73;_._

* **frombase**: Specifies the original base of number. Has to be between 2 and 36, inclusive. Digits in numbers with a base higher than 10 will be represented with the letters a-z, with a meaning 10, b meaning 11 and z meaning 35
* **tobase**: Specifies the base to convert to. Has to be between 2 and 36, inclusive. Digits in numbers with a base higher than 10 will be represented with the letters a-z, with a meaning 10, b meaning 11 and z meaning 35

In this example we are converting a hexadecimal number to an octal number:

#### bin2hex:

Converts a binary value into its hex equivalent.

#### decbin:&#x20;

Converts a decimal value into its binary string (i.e. 01010) equivalent.



#### bindec:&#x20;

Converts a binary string (i.e. 01010) into its decimal equivalent.

#### create\_object:

Creates an object based on a list of keys and a list of values.

![Keys list is \[first\_name, company, position\]. Values list is \[Michael, Xano, Customer Success Lead\].](<../../.gitbook/assets/CleanShot 2022-01-12 at 16.54.15.png>)

Resulting in a created object:

![The lists of keys and values are combined to create an object.](<../../.gitbook/assets/CleanShot 2022-01-12 at 16.59.43.png>)

#### **csv\_decode:**

Decodes the value represented in the CSV format and returns the result.

* **separator** - the field delimiter, one character only (usually a comma)
* **enclosure** - the field enclosure, one character only (usually a quotation mark)
* **escape** - the escape character that allows the enclosure character to be used within a field

<figure><img src="../../.gitbook/assets/CleanShot 2023-08-30 at 10.15.47.png" alt=""><figcaption></figcaption></figure>

#### **csv\_encode:**

Encodes the value and returns the result in CSV format

* **separator** - the field delimiter, one character only (usually a comma)
* **enclosure** - the field enclosure, one character only (usually a quotation mark)
* **escape** - the escape character that allows the enclosure character to be used within a field

<figure><img src="../../.gitbook/assets/CleanShot 2023-08-30 at 10.16.56.png" alt=""><figcaption></figcaption></figure>

#### **dechex**:&#x20;

Converts a decimal value into its hex equivalent.

#### decoct:&#x20;

Converts a decimal value into its octal equivalent.

#### hex2bin:

Converts a hex value into its binary equivalent.

#### hexdec:

Converts a hex value into its decimal equivalent.

#### json\_decode:

Decodes the value represented as json and returns the result. We will decode the json from the json\_encode filter example.

#### json\_encode:

Encodes the value and returns the result as json text. The variable object is: { "a":"3", "b":"2", "c":"1" }.

#### octdec:&#x20;

Converts an octal value into its decimal equivalent.

#### to\_bool:

Converts text, integer, or decimal types to a bool and returns the result.\
The different conversions that are possible with this filter are:\
Converting a text/integer/decimal value of 0 to false.\
Converting a text/integer/decimal value of 1 to true.\
Converting a text value of "true" to true.\
Converting a text value of "false" to false.

#### to\_decimal:

Converts text, integer, or bool types to a decimal and returns the result.

#### to\_int:

Converts text, decimal, or bool types to an integer and returns the result.

#### to\_text:

Converts text, decimal, or bool types to text and returns the result.

#### to\_timestamp:

Converts a text expression (now, next Friday) to timestamp comparable format.

#### url\_decode:

Decodes the value represented as a URL encoded value.

#### url\_decode\_rfc3986

Similar to url\_decode, this decodes the value represented as a URL encoded value, but conforming to [rfc3986](https://datatracker.ietf.org/doc/html/rfc3986) standards.

<figure><img src="../../.gitbook/assets/CleanShot 2023-08-30 at 12.49.36.png" alt=""><figcaption></figcaption></figure>

#### url\_encode:

Encodes the value and returns the result as a URL encoded value.

![Example: we have a text value then use the url\_encode filter to change it to Hello+World+%26+Xano. ](../../.gitbook/assets/urlencode.png)

#### url\_encode\_rfc3986

Similar to url\_encode, this encodes the value and returns the result as a URL encoded value, but conforming to [rfc3986](https://datatracker.ietf.org/doc/html/rfc3986) standards.

<figure><img src="../../.gitbook/assets/CleanShot 2023-08-30 at 12.47.21.png" alt=""><figcaption></figcaption></figure>

#### yaml\_decode:

Decodes the value represented as yaml and returns the result.\
For this example, we will use the example from yaml encode and then decode the variable.\
The variable gets changed into:

```
{
  "name": "John",
  "age": 30,
  "car": "ford"
}
```

![](https://mrkr.io/s/600f259aedf5d27fb4d8f24d/0)

#### yaml\_encode:

Encodes the value and returns the result as yaml text.

#### xml\_decode:

Decodes the provided data as XML, to JSON, and returns the result.

<figure><img src="../../.gitbook/assets/CleanShot 2023-08-30 at 12.52.02.png" alt=""><figcaption></figcaption></figure>
