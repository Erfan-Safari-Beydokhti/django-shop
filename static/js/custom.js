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
            document.getElementById("related_product")
                .scrollIntoView({ behavior: "smooth" });
        })
        .catch(err => console.error("Error sorting:", err));
}

function AddBlogComment(blog_id){
    var comment=$('#comment').val();
    var parentId=$('#parent_id').val();
    $.get("/blogs/add-blog-comment",{
        blog_comment:comment,
        blog_id:blog_id,
        parent_id:parentId
    }).then(res=>{
        $("#comment_area").html(res);
        $("#parent_id").val('');
        $("#comment").val('');
    })
}

function FillParentComment(parentId){
    $('#parent_id').val(parentId);
    document.getElementById('comment').focus();
    document.getElementById('scroll_comment').scrollIntoView({behavior:"smooth"});
}
