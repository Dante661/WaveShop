from django.urls import path
from .views import *


urlpatterns = [
    path("user/", create_user),
    path("login/<str:email>/", check_login),
    path("user/<int:id>/", get_user),
    path("product/", product_list),
    path("product/find", search_product.as_view()),
    path("product/<int:pk>/", product_by_id),
    path("product/seller/<int:storeId/", product_seller),
    path("productImg/", productImg_list),
    path("productImg/<int:productId>/", productImg_product_id),
    path("productImg/<int:id>/", productImg_by_id),
    path("product/<str:category>/", product_by_category),
    path("cart/", cart_list),
    path("cart/<int:userId>/", cart_by_user_id),
    path("cartItem/", cart_item_list),
    path("cartItem/<int:pk>/", cartItem_by_id),
    path("cartItem/<int:cartId>/", cartItem_by_cart_id),
    path("store/", create_store),
    path("store/<int:userId>/", get_store),
    path("uploadfile/", upload_file.as_view()),
    path("deletefile/<str:filename>/", delete_file),
    path("filter/price/<int:minprice>/", filter_min_price),
    path("filter/price/<int:maxprice>/", filter_max_price),
    path("filter/price/<int:minprice>/<int:maxprice>/", filter_maxmin_price),
    path("filter/rating/<int:rating>/", filter_rating),
    path(
        "filter/price_rating/<int:minprice>/<int:maxprice>/<int:rating>/",
        filter_price_rating,
    ),
    path("filter/condition/<str:condition>/", filter_condition),
    path(
        "filter/price_rating/<int:minprice>/<int:maxprice>/<int:rating>/<str:condition>/",
        filter_all,
    ),
    path("viewsItemsCart/<int:cartId>/", get_cart_item_by_cart_id),
]
