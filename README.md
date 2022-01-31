<p align="left">
  <img width = 70% src="assets/banner.jpg" >
</p>
<sub>Photo by <a href="https://unsplash.com/@jaywennington?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jay Wennington</a> on <a href="https://unsplash.com/s/photos/food-options?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  </sub>

&nbsp;

# **Find a Restaurant API**
Flask RESTful API

A API retorna opções de restaurante ao redor ao fornecer a cidade e o tipo de refeição.

Usa API Google para a geolocalização e API Foursquare para os restaurantes.

&nbsp;

## Endpoints:
---

**`GET /restaurants`**
---

retorna os dados de todos os restaurantes salvos no banco de dados

### Response

```json
{
    "restaurant": [
        {
            "id": 1,
            "image": "https://fastly.4sqi.net/img/general/300x300/9086923_zYhqkrsUN1L6sIkCG1TT1rFSE7LM17NQtilrN8kQMwA.jpg",
            "restaurant_address": "Suipacha 517",
            "restaurant_name": "Suiren Sushi Express"
        },
        {
            "id": 2,
            "image": "https://cdn.pixabay.com/photo/2020/04/11/22/59/restaurant-closed-5032259_960_720.jpg",
            "restaurant_address": "Týnská",
            "restaurant_name": "Crěpes Royales"
        },
        {
            "id": 3,
            "image": "https://cdn.pixabay.com/photo/2020/04/11/22/59/restaurant-closed-5032259_960_720.jpg",
            "restaurant_address": "500 16th St",
            "restaurant_name": "Soup Man"
        }
```



`POST /restaurants`
---

salva novo restaurante no banco de dados

### Response

```json
{
    "restaurant": {
        "id": 1,
        "image": "https://fastly.4sqi.net/img/general/300x300/9086923_zYhqkrsUN1L6sIkCG1TT1rFSE7LM17NQtilrN8kQMwA.jpg",
        "restaurant_address": "Suipacha 517",
        "restaurant_name": "Suiren Sushi Express"
    }
}
```



`GET /restaurant/<int:id>`
---

retorna os dados do restaurante especificado pelo seu *id*

### Response

```json
{
    "restaurant": {
        "id": 2,
        "image": "https://cdn.pixabay.com/photo/2020/04/11/22/59/restaurant-closed-5032259_960_720.jpg",
        "restaurant_address": "Týnská",
        "restaurant_name": "Crěpes Royales"
    }
}
```


`PUT /restaurant/<int:id>`
---

edita um ou mais dados do restaurante especificado pelo seu *id*

### Response

```json
{
    "restaurant": [
        {
            "id": 2,
            "image": "https://cdn.pixabay.com/photo/2016/10/03/13/35/cat-1711680_960_720.jpg",
            "restaurant_address": "fake test address",
            "restaurant_name": "fake test name"
        }
```

`DELETE /restaurant/<int:id>`
---

deleta dados do restaurante especificado pelo seu *id*

### Response

```html
Removed restaurant with id 2
```