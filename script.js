let cart = [];
let totalCost = 0;

document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', (event) => {
        const productElement = event.target.closest('.bg-gray-100');
        const productName = productElement.querySelector('h3').textContent;
        const productPrice = parseFloat(productElement.querySelector('.text-red-500').textContent.replace('KSHS ', '').replace(',', ''));

        // Add product to cart
        cart.push({ name: productName, price: productPrice });
        totalCost += productPrice;

        // Update cart count
        let cartCount = document.getElementById('cart-count');
        cartCount.textContent = cart.length;

        // Optional: Add animation or feedback for the user
        alert(`${productName} added to cart! Total cost: KSHS ${totalCost.toFixed(2)}`);
    });
});

// Function to remove item from cart
function removeFromCart(productName) {
    const index = cart.findIndex(item => item.name === productName);
    if (index > -1) {
        totalCost -= cart[index].price;
        cart.splice(index, 1);
        updateCartDisplay();
    }
}

function updateCartDisplay() {
    const cartItemsContainer = document.getElementById('cart-items');
    cartItemsContainer.innerHTML = ''; // Clear existing items
    cart.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - KSHS ${item.price.toFixed(2)}`;
        const removeButton = document.createElement('button');
        removeButton.textContent = 'Remove';
        removeButton.className = 'ml-2 text-red-500';
        removeButton.onclick = () => removeFromCart(item.name);
        li.appendChild(removeButton);
        cartItemsContainer.appendChild(li);
    });
    document.getElementById('total-cost').textContent = `Total Cost: KSHS ${totalCost.toFixed(2)}`;
}
