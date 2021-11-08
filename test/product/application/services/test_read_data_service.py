from product.application.services.read_data_service import ReadDataService
from product.domain.product import Product
from product.domain.product import ProductImage


def test_read_data_ok(
    read_data_service: ReadDataService,
) -> None:
    text = """{"product_categories_mapped": ["99"], "product_id": 769727985, 
    "url": "https://api.shopstyle.com/action/apiVisitRetailer?id=769727985&pid=uid8521-40402211-57", "gender": "men", 
    "price": 5.99, "product_description": "Cap in cotton twill with an adjustable strap at back with metal 
    fastener.colour:  Blue", "image_urls": [
    "https://img.shopstyle-cdn.com/pim/43/49/4349bdc3e26ee9b900fede407e9f9de5_best.jpg"], "product_imgs_src": [
    "https://img.shopstyle-cdn.com/pim/43/49/4349bdc3e26ee9b900fede407e9f9de5_best.jpg"], "source": "H&M", 
    "product_categories": ["mens-hats"], "images": [{"url": 
    "https://img.shopstyle-cdn.com/pim/43/49/4349bdc3e26ee9b900fede407e9f9de5_best.jpg", 
    "path": "full/d4c0b469d423ade33f9547c43e016f5e1d1e460d.jpg", "checksum": "9b901fac32079a6ab689c795f6689011"}], 
    "position": ["front"], "product_title": "H&M - Cotton Twill Cap - Blue", "brand": "H&M", "currency_code": "USD", 
    "stock": 1}
{"product_categories_mapped": [6], "product_id": 768212205, "source": "H&M", 
"url": "https://api.shopstyle.com/action/apiVisitRetailer?id=768212205&pid=uid8521-40402211-57", "gender": "men", 
"price": 12.99, "product_description": "Long-sleeved jersey shirt. Slim fit.colour:  Red", "image_urls": [
"https://img.shopstyle-cdn.com/pim/96/90/9690c8b4ee17b57d37283606d7cede92_best.jpg"], "product_imgs_src": [
"https://img.shopstyle-cdn.com/pim/96/90/9690c8b4ee17b57d37283606d7cede92_best.jpg"], "discount": 53, 
"product_categories": ["mens-shirts"], "images": [{"url": 
"https://img.shopstyle-cdn.com/pim/96/90/9690c8b4ee17b57d37283606d7cede92_best.jpg", 
"path": "full/e4d236bfdc02308cbb6e079f180fb5a9c7f8fef0.jpg", "checksum": "aca8e5f7900708fe656535e65ff8cb08"}], 
"position": ["front"], "product_title": "H&M - Long-sleeved Jersey Shirt - Red", "brand": "H&M", "currency_code": 
"USD", "stock": 1}
"""  # noqa: E501
    products = read_data_service.read_data(text=text)
    expected = [
        Product(
            product_categories_mapped=["99"],
            product_id=769727985,
            url="https://api.shopstyle.com/action/apiVisitRetailer?id=769727985&pid=uid8521-40402211-57",
            gender="men",
            price=5.99,
            product_description="Cap in cotton twill with an adjustable strap at back with metal fastener.colour:  Blue",
            image_urls=["https://img.shopstyle-cdn.com/pim/43/49/4349bdc3e26ee9b900fede407e9f9de5_best.jpg"],
            product_imgs_src=["https://img.shopstyle-cdn.com/pim/43/49/4349bdc3e26ee9b900fede407e9f9de5_best.jpg"],
            source="H&M",
            product_categories=["mens-hats"],
            images=[
                ProductImage(
                    url="https://img.shopstyle-cdn.com/pim/43/49/4349bdc3e26ee9b900fede407e9f9de5_best.jpg",
                    path="full/d4c0b469d423ade33f9547c43e016f5e1d1e460d.jpg",
                    checksum="9b901fac32079a6ab689c795f6689011"
                ),
            ],
            position=["front"],
            product_title="H&M - Cotton Twill Cap - Blue",
            brand="H&M",
            currency_code="USD",
            stock=1,
        ),
        Product(
            product_categories_mapped=[6],
            product_id=768212205,
            source="H&M",
            url="https://api.shopstyle.com/action/apiVisitRetailer?id=768212205&pid=uid8521-40402211-57",
            gender="men",
            price=12.99,
            product_description="Long-sleeved jersey shirt. Slim fit.colour:  Red",
            image_urls=["https://img.shopstyle-cdn.com/pim/96/90/9690c8b4ee17b57d37283606d7cede92_best.jpg"],
            product_imgs_src=["https://img.shopstyle-cdn.com/pim/96/90/9690c8b4ee17b57d37283606d7cede92_best.jpg"],
            discount=53,
            product_categories=["mens-shirts"],
            images=[
                ProductImage(
                    url="https://img.shopstyle-cdn.com/pim/96/90/9690c8b4ee17b57d37283606d7cede92_best.jpg",
                    path="full/e4d236bfdc02308cbb6e079f180fb5a9c7f8fef0.jpg",
                    checksum="aca8e5f7900708fe656535e65ff8cb08"
                ),
            ],
            position=["front"],
            product_title="H&M - Long-sleeved Jersey Shirt - Red",
            brand="H&M",
            currency_code="USD",
            stock=1
        )
    ]
    assert products == expected
