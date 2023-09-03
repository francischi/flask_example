## introduction
此專案以下表為範例建立商品訂單，包含 DB schema 多對一 多對多的設計，以及api-document的撰寫。
| Name     | Code | Category |  Size | Unit | inventory | color | 
| :-----   | :--- | :----    | :-----| :--- | :----     | :---- |
| product1 | A-001|  pants   | S、M  | 300  | 20        | red、yellow | 
| product2 | B-001|  cloth   | S、M、L  | 500  | 25        | green、blue |
| product3 | B-002|  pants   | L  | 100  | 50        | red、yellow |

## running service
```
> pip install -r requirements.txt
> python index.py
<!-- run on 127.0.0.1:3000 -->
```

## migrate
please create a db name 'test'
table will auto migrate after server run if table didn't exist

## note
還未在新增產品時加上檢查table有無對應ID之檢查
因此測試新增或修改產品時請輸入以下現有ID(migrate時生成之資料)
category_id : 1(cloth) , 2(pants)
code_id : 1(A-001) , 2(B-001)
size_id : 1(L) , 2(M)
color_id : 1(red) , 2(blue)

## table schema design
* products
    ```
    id
    name
    code_id
    category_id
    unit_price
    inventory
    update_time
    delete_time
    create_time
    ```

* codes
    ```
    id
    code
    ```

* categories
    ```
    id
    name
    ```

* products_size
    ```
    id
    product_id
    size_id
    ```

* sizes
    ```
    id
    name
    ```
* products_color
    ```
    id
	product_id
	color_id
    ```
* colors
    ```
    id
    name
    ```