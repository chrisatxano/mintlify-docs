# External Filtering Examples

### **Basic Equals Operation**

Checking if a user ID equals 1:

```json
{
  "expression": [{
    "statement": {
      "left": {
        "tag": "col",
        "operand": "users.id"
      },
      "op": "=",
      "right": {
        "operand": "1"
      }
    }
  }]
}
```

### **Between Operation**

Finding transactions with amount between 100 and 1000:

```json
{
  "expression": [{
    "statement": {
      "left": {
        "tag": "col",
        "operand": "transactions.amount"
      },
      "op": "between",
      "right": {
        "operand": ["100", "1000"]
      }
    }
  }]
}
```

### **Contains Operation**

Finding users with email containing '@company.com':

```json
{
  "expression": [{
    "statement": {
      "left": {
        "tag": "col",
        "operand": "users.email"
      },
      "op": "contains",
      "right": {
        "operand": "@company.com"
      }
    }
  }]
}
```

### **Multiple Conditions Example**

Finding active premium users who have made at least 5 purchases:

```json
{
  "expression": [
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.status"
        },
        "op": "=",
        "right": {
          "operand": "active"
        }
      }
    },
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.account_type"
        },
        "op": "=",
        "right": {
          "operand": "premium"
        }
      }
    },
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.purchase_count"
        },
        "op": ">=",
        "right": {
          "operand": "5"
        }
      }
    }
  ]
}
```

### **Case-Insensitive Pattern Matching (ilike)**

Finding products with names starting with 'phone', regardless of case:

```json
{
  "expression": [{
    "statement": {
      "left": {
        "tag": "col",
        "operand": "products.name"
      },
      "op": "ilike",
      "right": {
        "operand": "phone%"
      }
    }
  }]
}
```

### **Array Membership (in)**

Finding orders with specific status values:

```json
{
  "expression": [{
    "statement": {
      "left": {
        "tag": "col",
        "operand": "orders.status"
      },
      "op": "in",
      "right": {
        "operand": ["pending", "processing", "shipped"]
      }
    }
  }]
}
```

### **Complex Multiple Conditions**

Finding high-value transactions (>1000) made in the last 30 days by premium users:

```json
{
  "expression": [
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "transactions.amount"
        },
        "op": ">",
        "right": {
          "operand": "1000"
        }
      }
    },
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "transactions.date"
        },
        "op": ">=",
        "right": {
          "operand": "2024-12-29"
        }
      }
    },
    {
      "statement": {
        "left": {
          "tag": "col",
          "operand": "users.account_type"
        },
        "op": "=",
        "right": {
          "operand": "premium"
        }
      }
    }
  ]
}
```
