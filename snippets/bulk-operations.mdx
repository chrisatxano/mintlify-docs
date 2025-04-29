---
title: Bulk Operations
---

## <img src="../assets/docuBadge (9).png" alt="" data-size="line"> Bulk Operations

<details>

<summary>Bulk Add</summary>

```javascript
db.bulk.add user {
    allow_id_field = false
    items = $input.arrayData
} as $bulkAdd
```

| Parameter        | Purpose                       | Example                            |
| ---------------- | ----------------------------- | ---------------------------------- |
| allow\_id\_field | Allow manual ID specification | false                              |
| items            | Array of records to add       | `[{name: "John"}, {name: "Jane"}]` |

```javascript
// Add multiple users at once
db.bulk.add user {
    allow_id_field = false
    items = [
        {
            name: "John Doe",
            email: "john@example.com"
        },
        {
            name: "Jane Smith",
            email: "jane@example.com"
        }
    ]
} as newUsers
```

</details>

<details>

<summary>Bulk Update</summary>

```javascript
db.bulk.update user {
    items = $input.arrayData
} as $updateBulk
```

| Parameter | Purpose                    | Example                                          |
| --------- | -------------------------- | ------------------------------------------------ |
| items     | Array of records to update | `[{id: 1, name: "John"}, {id: 2, name: "Jane"}]` |

```javascript
// Update status for multiple users
db.bulk.update user {
    items = [
        {id: 1, status: "active"},
        {id: 2, status: "inactive"},
        {id: 3, status: "pending"}
    ]
} as statusUpdates
```

</details>

<details>

<summary>Bulk Patch</summary>

```javascript
db.bulk.patch user {
    items = $input.arrayData
} as $patchBulk
```

| Parameter | Purpose                   | Example                                          |
| --------- | ------------------------- | ------------------------------------------------ |
| items     | Array of records to patch | `[{id: 1, name: "John"}, {id: 2, name: "Jane"}]` |

```javascript
// Update role for multiple users
db.bulk.patch user {
    items = [
        {id: 1, data: {}|set:"role":"admin"},
        {id: 2, data: {}|set:"role":"moderator"}
    ]
} as roleUpdates
```

</details>

<details>

<summary>Bulk Delete</summary>

```javascript
db.bulk.delete user {
    search = `$db.user.id >= 100 && $db.user.id <= 150`
} as $deleteBulk
```

| Parameter | Purpose                      | Example              |
| --------- | ---------------------------- | -------------------- |
| search    | Query condition for deletion | `$db.user.id >= 100` |

```javascript
// Delete all inactive users
db.bulk.delete user {
    search = `$db.user.status == "inactive" && $db.user.last_login < "2023-01-01"`
} as inactiveUsersDeletion
```

</details>

> 💡 Bulk operations are more efficient than performing multiple individual operations when working with multiple records.

## Notes

* All operations return the affected record(s) in the variable specified after `as`
* Bulk operations can significantly improve performance when working with multiple records
* The `field_name` and `field_value` combination is used to identify specific records
* Patch operations are useful when you want to update specific fields without affecting others
