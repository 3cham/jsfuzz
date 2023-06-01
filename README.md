# Fuzzy matching for JSON payload. Find json_path that matches best for your provided value

## Examples:


```json
{
  "id": 11,
  "title": "perfume Oil",
  "description": "Mega Discount, Impression of A...",
  "price": 13,
  "discountPercentage": 8.4,
  "rating": 4.26,
  "stock": 65,
  "brand": "Impression of Acqua Di Gio",
  "category": "fragrances",
  "thumbnail": "https://i.dummyjson.com/data/products/11/thumbnail.jpg",
  "images": [
    "https://i.dummyjson.com/data/products/11/1.jpg",
    "https://i.dummyjson.com/data/products/11/2.jpg",
    "https://i.dummyjson.com/data/products/11/3.jpg",
    "https://i.dummyjson.com/data/products/11/thumbnail.jpg"
  ]
}
```

```python
from jsfuzz import inspector

result = inspector.search(payload, "brand")
result.reverse()

pprint(result)
====================

Returns:

[('$.brand', 'Impression of Acqua Di Gio', 75.80645161290323),
 ('$.rating', '4.26', 38.18181818181817),
 ('$.category', 'fragrances', 22.769230769230766),
 ('$.thumbnail',
  'https://i.dummyjson.com/data/products/11/thumbnail.jpg',
  22.033898305084744),
 ('$.description', 'Mega Discount, Impression of A...', 20.657894736842106)]
```


```python
result = inspector.search(payload, "65")
result.reverse()

pprint(result)
====================

Returns:

[('$.stock', '65', 30.0),
 ('$.rating', '4.26', 10.0),
 ('$.discountPercentage', '8.4', 0.0),
 ('$.price', '13', 0.0),
 ('$.description', 'Mega Discount, Impression of A...', 0.0)]
```