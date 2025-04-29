# Math

For each of these examples, we'll start with a value of 5.

{% @arcade/embed flowId="V97HHLB4uaJpfBmFNi2w" url="https://app.arcade.software/share/V97HHLB4uaJpfBmFNi2w" %}



### Add Number

Adds one value to another

### Subtract Number

Subtracts one value from another

### Multiply Number

Multiplies one value by another

### Divide Number

Divides one value by another

### Modulus Number

Get the remainder when an existing value is divided by a number.

### Bitwise

Working on bytes, or Data Types comprising of bytes like ints, floats, doubles or even data structures that store large amounts of bytes is normal for a programmer. In some cases, a programmer needs to go beyond this - that is to say, on a deeper level where the importance of bits is realized.

Operations with bits are used in **Data Compression** (data is compressed by converting it from one representation to another, to reduce the space), **Exclusive-Or Encryption** (an algorithm to encrypt the data for safety issues). In order to encode, decode, or compress files we have to extract the data at bit level. Bitwise Operations are faster and closer to the system and sometimes optimize the program to a good level.

1 byte comprises of 8 bits and any integer or character can be represented using bits in computers, which we call its binary form(contains only 1 or 0) or in its base 2 form. [Real-world use cases of Bitwise Operators (Stack Overflow)](https://stackoverflow.com/questions/2096916/real-world-use-cases-of-bitwise-operators)

**Bitwise AND**

The output of bitwise AND is 1 if the corresponding bits of two operands is 1. If either bit of an operand is 0, the result of the corresponding bit is evaluated to 0. Here's an example with the binary values written out:

```
12 = 00001100 (In Binary)
25 = 00011001 (In Binary)

Bit Operation of 12 and 25
  00001100
& 00011001
  ________
  00001000  = 8 (In decimal)
```

We will set up the same example in **Xano** and change the number variable to 12.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FdnLk2RZSWZwBOZyY3zTJ%252FCleanShot%25202023-01-18%2520at%252010.06.09%25402x.png%3Falt%3Dmedia%26token%3Dd4f54fde-f592-41f5-beb6-b37bf437f584\&width=768\&dpr=4\&quality=100\&sign=f40737df\&sv=2)

And for the API action we will use Bitwise AND with the value 25:

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FKdsin8QtlLW0S6UZuoKH%252FCleanShot%25202023-01-18%2520at%252010.06.35%25402x.png%3Falt%3Dmedia%26token%3D57dda671-646b-44bf-8891-f1c48008c214\&width=768\&dpr=4\&quality=100\&sign=fdfe129b\&sv=2)

In the above example, the `number` variable would be **8**

**Bitwise OR**

The output of bitwise OR is 1 if at least one corresponding bit of two operands is 1. In C Programming, bitwise OR operator is denoted by |. Here's an example with the binary values written out:

```
12 = 00001100 (In Binary)
25 = 00011001 (In Binary)

Bitwise OR Operation of 12 and 25
  00001100
| 00011001
  ________
  00011101  = 29 (In decimal)
```

We will set up the same example in **Xano** and change the number variable to 12.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FdnLk2RZSWZwBOZyY3zTJ%252FCleanShot%25202023-01-18%2520at%252010.06.09%25402x.png%3Falt%3Dmedia%26token%3Dd4f54fde-f592-41f5-beb6-b37bf437f584\&width=768\&dpr=4\&quality=100\&sign=f40737df\&sv=2)

And for the API action we will use Bitwise OR with the value 25:

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F7l05Zlod386o0QyoZolZ%252FCleanShot%25202023-01-18%2520at%252010.07.04%25402x.png%3Falt%3Dmedia%26token%3D9ec5888a-4879-4fb7-bd99-b1f71da7ef44\&width=768\&dpr=4\&quality=100\&sign=13d31532\&sv=2)

In the above example, the `number` variable would be **29**

**Bitwise XOR**

The result of bitwise XOR operator is 1 if the corresponding bits of two operands are opposite. It is denoted by ^. The exclusive-or operation takes two inputs and returns a 1 if either one or the other of the inputs is a 1, but not if both are. That is, if both inputs are 1 or both inputs are 0, it returns 0. Bitwise exclusive-or, with the operator of a caret, ^, performs the exclusive-or operation on each pair of bits. Exclusive-or is commonly abbreviated XOR. Here's an example with the binary values written out:

```
12 = 00001100 (In Binary)
25 = 00011001 (In Binary)

Bitwise XOR Operation of 12 and 25
  00001100
^ 00011001
  ________
  00010101  = 21 (In decimal)
```

We will set up the same example in **Xano** and change the number variable to 12.

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252FdnLk2RZSWZwBOZyY3zTJ%252FCleanShot%25202023-01-18%2520at%252010.06.09%25402x.png%3Falt%3Dmedia%26token%3Dd4f54fde-f592-41f5-beb6-b37bf437f584\&width=768\&dpr=4\&quality=100\&sign=f40737df\&sv=2)

And for the API action we will use Bitwise XOR with the value 25:

![](https://docs.xano.com/~gitbook/image?url=https%3A%2F%2F3176331816-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F-M8Si5XvG2QHSLi9JcVY%252Fuploads%252F9Yvj06myzBBUF9mBYfxb%252FCleanShot%25202023-01-18%2520at%252010.08.16%25402x.png%3Falt%3Dmedia%26token%3D9a6ae9d0-64fe-4757-8bf2-ca2c649c20d0\&width=768\&dpr=4\&quality=100\&sign=b8aa4141\&sv=2)

In the above example, the `number` variable would be **21**
