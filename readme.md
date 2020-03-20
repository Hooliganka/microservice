Для запуска:

- ```$ sudo docker-compose up```

Для теста по сценарию:

- ```$ curl -d '{"title": "Телефон","description": "Очень красивый телефон", "parameters": {"color": "green","size": 153}}' -H 'Content-Type: application/json' 127.0.0.1:8080/api/create/```  Создать товар
- ```$ curl 127.0.0.1:8080/api/products/``` Получение всех товаров
- ```$ curl 127.0.0.1:8080/api/products_title/?title=Телефон``` Получаем список названий товаров, с фильтрацией по названию
- ```$ curl 127.0.0.1:8080/api/products_title/?parameters.size=153&parameters.color=green``` Получаем список названий товаров, с фильтрацией по параметрам 
- ```$ curl 127.0.0.1:8080/api/product/5e74288423509978e1505dc1/``` Получение деталей найденного товара
