## api document
prefix :```/api```
### <span style="color:blue">/products

#### **method** ```GET```

#### **result**

* success
```
{
    "result": [
        {
            "category": {
                "id": 1,
                "name": "jeans"
            },
            "code": {
                "id": 1,
                "name": "A-001"
            },
            "colors": [
                {
                    "name": "red"
                }
            ],
            "create_time": 1691049902,
            "delete_time": null,
            "id": 1,
            "inventory": 100,
            "name": "this is product1",
            "sizes": [
                {
                    "name": "M"
                }
            ],
            "unit_price": 4000,
            "update_time": 1691049917
        },
        {
            "category": {
                "id": 2,
                "name": "pants"
            },
            "code": {
                "id": 2,
                "name": "B-001"
            },
            "colors": [
                {
                    "name": "red"
                }
            ],
            "create_time": 1691050046,
            "delete_time": null,
            "id": 2,
            "inventory": 100,
            "name": "product2",
            "sizes": [
                {
                    "name": "M"
                },
                {
                    "name": "L"
                }
            ],
            "unit_price": 2000,
            "update_time": null
        }
    ],
    "success": "true"
}
```

* failed
```
{
    "message": "error",
    "success": "false"
}
```

### <span style="color:blue">/product

#### **method** ```POST```

#### **params**
**body** :

Content-Type : ```application/json```

| param     | required | description |
| :-----    | :---     | :----       |
| name      | v        |  str  |
| code_id     | v        |   int   |
| category_id    | v        | int |
| size_ids  | v        |  array[int] |
| unit_price  | v        |  int  |
| inventory  | v        |  int  |
| color_ids  | v        | array[int]  |


```
{
    "name":"product1",
    "code_id":1,
    "category_id":1,
    "size_ids":[
        1,
        2
    ],
    "unit_price":2000,
    "inventory":100,
    "color_ids":[
        1,
        2
    ]  
}
```

#### **result**

* success
```
{
    "success": "true"
}
```

* failed
```
{
    "message": "name required",
    "success": "false"
}
```

### <span style="color:blue">/product/<product_id>

#### **method** ```PUT```

#### **params**
**body** :

Content-Type : ```application/json```

| param     | required | description |
| :-----    | :---     | :----       |
| name      | v        |  str  |
| code_id     | v        |   int   |
| category_id    | v        | int |
| size_ids  | v        |  array[int] |
| unit_price  | v        |  int  |
| inventory  | v        |  int  |
| color_ids  | v        | array[int]  |
```
{
    "name":"product1",
    "code_id":1,
    "category_id":1,
    "size_ids":[
        1,
        2
    ],
    "unit_price":2000,
    "inventory":100,
    "color_ids":[
        1,
        2
    ]  
}
```

#### **result**

* success
```
{
    "success": "true"
}
```

* failed
```
{
    "message": "name required",
    "success": "false"
}
```

### <span style="color:blue">/product/<product_id>

#### **method** ```DELETE```
soft delete
#### **result**

* success
```
{
    "success": "true"
}
```

* failed
```
{
    "message": "err",
    "success": "false"
}
```