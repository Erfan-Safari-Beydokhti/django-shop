window.SortProductReviews = function (product_id) {
    var sort = $("#sort-review").val();
    $.get(`/products/${product_id}/reviews_partial/`, {sort: sort})
        .then(res => {
            $("#review_area").html(res);
            document.getElementById("tabs").scrollIntoView({behavior: "smooth"});
        })
        .catch(err => console.error("Error loading reviews:", err));
};

window.SortProductList = function () {
    var sort = $("#sort_product").val();

    $.get('/products/products-sort/partial/', { sort: sort })
        .then(res => {
            $("#products_list").html(res.html);
            document.getElementById("products_list")
                .scrollIntoView({ behavior: "smooth" });
        })
        .catch(err => console.error("Error sorting:", err));
}