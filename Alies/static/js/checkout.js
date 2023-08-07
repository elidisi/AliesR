document.addEventListener('DOMContentLoaded', () => {
    const cartItems = document.querySelector('.cart-items');
    const total = document.querySelector('.total');

    // Get cart items from localStorage
    const storedCartItems = JSON.parse(localStorage.getItem('cartItems'));

    if (storedCartItems && storedCartItems.length > 0) {
        storedCartItems.forEach(item => {
            const cartItem = document.createElement('div');
            cartItem.classList.add('cart-item');
            cartItem.textContent = `${item.name} - ₱${item.price.toFixed(2)}`;

            const removeButton = document.createElement('button');
            removeButton.textContent = 'Remove';
            removeButton.classList.add('cart-item-remove');
            removeButton.addEventListener('click', () => removeFromCart(item));

            cartItem.appendChild(removeButton);
            cartItems.appendChild(cartItem);
        });

        // Calculate total
        const totalAmount = storedCartItems.reduce((acc, item) => acc + item.price, 0);
        total.textContent = `Total: ₱${totalAmount.toFixed(2)}`;
    } else {
        cartItems.textContent = 'No items in cart.';
    }
});

function removeFromCart(item) {
    const storedCartItems = JSON.parse(localStorage.getItem('cartItems'));

    const updatedCartItems = storedCartItems.filter(cartItem => cartItem.name !== item.name);
    localStorage.setItem('cartItems', JSON.stringify(updatedCartItems));

    location.reload(); // Refresh the page to reflect changes
}
