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

    $.get('/products/products-sort/partial/', {sort: sort})
        .then(res => {
            $("#products_list").html(res.html);
            document.getElementById("related_product")
                .scrollIntoView({behavior: "smooth"});
        })
        .catch(err => console.error("Error sorting:", err));
}

function AddBlogComment(blog_id) {
    var comment = $('#comment').val();
    var parentId = $('#parent_id').val();

    $.get("/blogs/add-blog-comment", {
        blog_comment: comment,
        blog_id: blog_id,
        parent_id: parentId
    }).then(res => {
        $("#comment_area").html(res);


        if (res.includes("Your comment has been submitted successfully")) {
            $("#comment").val('');
            $("#parent_id").val('');
        }
        document.getElementById('d_messages').scrollIntoView({behavior: "smooth"});

        bindAlertClose();
    });
}


function bindAlertClose() {
    $(".js-dismiss-alert").off("click").on("click", function () {
        $(this).closest(".gl-alert").fadeOut(300);
    });
}

$(document).ready(bindAlertClose);


function FillParentComment(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('comment').focus();
    document.getElementById('scroll_comment').scrollIntoView({behavior: "smooth"});
}


let commentOffset = 10

function LoadMoreComments(blog_id) {
    $.get("/blogs/load-more-comment", {
        blog_id: blog_id,
        offset: commentOffset
    }).then(res => {
        $("#load_more_btn").before(res);
        commentOffset += 10;
        if (!res.includes("data-has-more")) {
            $("#load_more_btn").hide();
        }

    })
}


function changeQuantity(itemId, operation) {

    $.get("/cart/change-cart-item?item_id=" + itemId + "&state=" + operation).then(res=>{
        if (res.status==="success"){
            $("#cart-item-content").html(res.data);
        }
    })

}

function removeCartItem(itemId){
    $.get('/cart/remove-cart-item?item_id='+itemId).then(res=>{
        if(res.status==='success'){
            $("#cart-item-content").html(res.data);
        }
    })
}