var updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var productID = this.dataset.product;
        var action = this.dataset.action;
        
        if (user == 'AnonymousUser') {
            console.log('Not authenticated');
        } else {
            updateUserOrder(productID, action);
        }
    })
}

function updateUserOrder(productID, action){

    var url = '/update_item/'

    fetch(
        url,
        {
            method:'POST',
            headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body:JSON.stringify({'productID':productID, 'action':action}),
        }
    ).then(
        (response) => { return response.json(); }
    ).then(
        (data) => { 
            location.reload();
        }
    )
}