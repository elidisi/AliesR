// Sample data for the menu items
const menuItems = [
    // All Day Breakfast
    { name: 'Hotsilog', price: 85, imageURL: './menupics/breakfast/hotsilog.png', category: 'breakfast' },
    { name: 'Cornsilog', price: 100, imageURL: './menupics/breakfast/cornsilog.png', category: 'breakfast' },
    { name: 'Spamsilog', price: 110, imageURL: './menupics/breakfast/spamsilog.jpg', category: 'breakfast' },
    { name: 'Tocilog ', price: 100, imageURL: './menupics/breakfast/tocilog.png', category: 'breakfast' },
    { name: 'Longsilog ', price: 100, imageURL: './menupics/breakfast/longsilog.png', category: 'breakfast' },
    { name: 'Tapsilog ', price: 130, imageURL: './menupics/breakfast/tapsilog.jpg', category: 'breakfast' },
    { name: 'Porksilog ', price: 140, imageURL: './menupics/breakfast/porksilog.jpg', category: 'breakfast' },
    { name: 'Bangsilog ', price: 150, imageURL: './menupics/breakfast/bangsilog.jpg', category: 'breakfast' },
    { name: 'Chicksilog ', price: 140, imageURL: './menupics/breakfast/chicsilog.jpg', category: 'breakfast' },
    { name: 'Coffee ', price: 20, imageURL: './menupics/breakfast/coffee.jpg', category: 'breakfast' },
    { name: 'Ice Tea ', price: 20, imageURL: './menupics/breakfast/icetea.jpeg', category: 'breakfast' },

    // Noodles
    { name: 'Pancit Bihon', price: 150, imageURL: 'menupics/noodles/bihon.jpg', category: 'noodles' },
    { name: 'Pancit Canton', price: 150, imageURL: 'menupics/noodles/canton.jpg', category: 'noodles' },
    { name: 'Mixed Bihon', price: 170, imageURL: 'menupics/noodles/mbihon.jpg', category: 'noodles' },

    // Sisig
    { name: 'Pork Sisig', price: 100, imageURL: 'menupics/sisig/psisig.jpg', category: 'sisig' },
    { name: 'Bangus Sisig', price: 100, imageURL: 'menupics/sisig/bsisig.png', category: 'sisig' },
    { name: 'Chicken Sisig', price: 100, imageURL: 'menupics/sisig/csisig.png', category: 'sisig' },
    { name: 'Kangkong Sisig', price: 90, imageURL: 'menupics/sisig/ksisig.jpg', category: 'sisig' },
    { name: 'Group Pork Sisig', price: 180, imageURL: 'menupics/sisig/gpsisig.jpg', category: 'sisig' },
    { name: 'Group Bangus Sisig', price: 180, imageURL: 'menupics/sisig/gbsisig.png', category: 'sisig' },
    { name: 'Group Chicken Sisig', price: 180, imageURL: 'menupics/sisig/gcsisig.png', category: 'sisig' },
    { name: 'Group Kangkong Sisig', price: 170, imageURL: 'menupics/sisig/gksisig.png', category: 'sisig' },

    // Yangchow
    { name: 'Pork Siomai', price: 85, imageURL: 'menupics/yangchow/psiomai.png', category: 'yangchow' },
    { name: 'Beef Siomai', price: 85, imageURL: 'menupics/yangchow/bsiomai.png', category: 'yangchow' },
    { name: 'Shanghai', price: 85, imageURL: 'menupics/yangchow/shanghai.png', category: 'yangchow' },
    { name: 'Dumpling', price: 85, imageURL: 'menupics/yangchow/dumpling.png', category: 'yangchow' },

    // Wings
    { name: '3 Pieces Wings', price: 130, imageURL: 'menupics/wings/3wings.jpg', category: 'wings' },
    { name: '6 Pieces Wings', price: 240, imageURL: 'menupics/wings/6wings.jpg', category: 'wings' },
    { name: '12 Piece Wings', price: 430, imageURL: 'menupics/wings/12wings.png', category: 'wings' },

    // Pork Dishes
    { name: 'Bagnet', price: 120, imageURL: 'menupics/pork/bagnet.png', category: 'pork' },
    { name: 'Bagnet Kare Kare', price: 180, imageURL: 'menupics/pork/bagnetkk.jpg', category: 'pork' },
    { name: 'Sinigang na Bagnet', price: 150, imageURL: 'menupics/pork/sbagnet.png', category: 'pork' },
    { name: 'Tortang Giniling', price: 100, imageURL: 'menupics/pork/giniling.png', category: 'pork' },
    { name: 'Bagnet Binagoongan', price: 150, imageURL: 'menupics/pork/bagnetb.jpg', category: 'pork' },
    { name: 'Pork Adobo', price: 130, imageURL: 'menupics/pork/padobo.png', category: 'pork' },
    { name: 'Pork ', price: 110, imageURL: 'menupics/pork/psteak.png', category: 'pork' },
    { name: 'Bicol Express', price: 130, imageURL: 'menupics/pork/bicole.jpg', category: 'pork' },
    { name: 'Group Bagnet', price: 230, imageURL: 'menupics/pork/gbagnet.png', category: 'pork' },
    { name: 'Group Bagnet Kare Kare', price: 350, imageURL: 'menupics/pork/gbagnetkk.png', category: 'pork' },
    { name: 'Group Sinigang na Bagnet', price: 290, imageURL: 'menupics/pork/gsbagnet.png', category: 'pork' },
    { name: 'Group Bagnet Binagoongan', price: 290, imageURL: 'menupics/pork/gbagnetb.png', category: 'pork' },
    { name: 'Group Pork Adobo', price: 250, imageURL: 'menupics/pork/gpadobo.png', category: 'pork' },
    { name: 'Group Pork ', price: 200, imageURL: 'menupics/pork/gpsteak.jpg', category: 'pork' },
    { name: 'Group Bicol Express', price: 200, imageURL: 'menupics/pork/gbicole.png', category: 'pork' },

    // Chicken Dishes
    { name: 'Chicken Tinola', price: 150, imageURL: 'menupics/chicken/ctinola.png', category: 'chicken' },
    { name: 'Chicken Curry', price: 150, imageURL: 'menupics/chicken/ccurry.png', category: 'chicken' },
    { name: 'Chicken Adobo', price: 120, imageURL: 'menupics/chicken/cadobo.jpg', category: 'chicken' },
    { name: 'Chicken Fillet', price: 140, imageURL: 'menupics/chicken/cfillet.jpg', category: 'chicken' },
    { name: 'Group Chicken Tinola', price: 230, imageURL: 'menupics/chicken/gctinola.png', category: 'chicken' },
    { name: 'Group Chicken Curry', price: 200, imageURL: 'menupics/chicken/gccurry.jpg', category: 'chicken' },
    { name: 'Group Chicken Adobo', price: 230, imageURL: 'menupics/chicken/gcadobo.png', category: 'chicken' },
    { name: 'Group Chicken Fillet', price: 270, imageURL: 'menupics/chicken/gcfillet.png', category: 'chicken' },

    // Beef Dishes
    { name: 'Beef Bulalo', price: 150, imageURL: 'menupics/beef/bulalo.png', category: 'beef' },
    { name: 'Beef with Brocoli', price: 110, imageURL: 'menupics/beef/beefb.png', category: 'beef' },
    { name: 'Beef Salpicao', price: 130, imageURL: 'menupics/beef/salpicao.png', category: 'beef' },
    { name: 'Beef ', price: 120, imageURL: 'menupics/beef/bsteak.jpg', category: 'beef' },
    { name: 'Group Beef Bulalo', price: 290, imageURL: 'menupics/beef/gbulalo.png', category: 'beef' },
    { name: 'Group Beef with Brocoli', price: 215, imageURL: 'menupics/beef/gbeefb.png', category: 'beef' },
    { name: 'Group Beef Salpicao', price: 250, imageURL: 'menupics/beef/gsalpicao.png', category: 'beef' },
    { name: 'Group Beef ', price: 230, imageURL: 'menupics/beef/gbsteak.png', category: 'beef' },

    // Seafoods
    { name: 'Fried Tilipia', price: 120, imageURL: 'menupics/seafood/tilapia.png', category: 'seafood' },
    { name: 'Sinigang na Bangus', price: 140, imageURL: 'menupics/seafood/sbangus.jpg', category: 'seafood' },
    { name: 'Adobong Pusit', price: 190, imageURL: 'menupics/seafood/apusit.png', category: 'seafood' },
    { name: 'Fish Fillet', price: 100, imageURL: 'menupics/seafood/ffillet.png', category: 'seafood' },
    { name: 'Paksiw na Bangus', price: 140, imageURL: 'menupics/seafood/pbangus.jpg', category: 'seafood' },
    { name: 'Group Sinigang na Bangus', price: 140, imageURL: 'menupics/seafood/gsbangus.jpg', category: 'seafood' },
    { name: 'Group Adobong Pusit', price: 190, imageURL: 'menupics/seafood/gapusit.jpg', category: 'seafood' },
    { name: 'Group Fish Fillet', price: 100, imageURL: 'menupics/seafood/gffillet.jpg', category: 'seafood' },
    { name: 'Group Paksiw na Bangus', price: 140, imageURL: 'menupics/seafood/gpbangus.png', category: 'seafood' },

    // Vegetable Dishes
    { name: 'Chopseuy', price: 80, imageURL: 'menupics/vegetable/chopseuy.png', category: 'vegetable' },
    { name: 'Pinakbet', price: 90, imageURL: 'menupics/vegetable/pinakbet.png', category: 'vegetable' },
    { name: 'Adobong Sitaw', price: 80, imageURL: 'menupics/vegetable/asitaw.jpg', category: 'vegetable' },
    { name: 'Spicy Kangkong', price: 80, imageURL: 'menupics/vegetable/skangkong.png', category: 'vegetable' },
    { name: 'Ginisang Ampalaya', price: 100, imageURL: 'menupics/vegetable/gampalaya.jpg', category: 'vegetable' },
    { name: 'Ginataang Sitaw', price: 85, imageURL: 'menupics/vegetable/gsitaw.jfif', category: 'vegetable' },
    { name: 'Monggo', price: 90, imageURL: 'menupics/vegetable/monggo.jfif', category: 'vegetable' },
    { name: 'Enseladang Talong', price: 85, imageURL: 'menupics/vegetable/talong.png', category: 'vegetable' },
    { name: 'Group Chopseuy', price: 150, imageURL: 'menupics/vegetable/gchopseuy.png', category: 'vegetable' },
    { name: 'Group Pinakbet', price: 170, imageURL: 'menupics/vegetable/gpinakbet.jpg', category: 'vegetable' },
    { name: 'Group Adobong Sitaw', price: 150, imageURL: 'menupics/vegetable/gasitaw.jpg', category: 'vegetable' },
    { name: 'Group Spicy Kangkong', price: 150, imageURL: 'menupics/vegetable/gskangkong.jfif', category: 'vegetable' },
    { name: 'Group Ginisang Ampalaya', price: 190, imageURL: 'menupics/vegetable/ggampalaya.jpg', category: 'vegetable' },
    { name: 'Group Ginataang Sitaw', price: 165, imageURL: 'menupics/vegetable/ggsitaw.jfif', category: 'vegetable' },
    { name: 'Group Monggo', price: 170, imageURL: 'menupics/vegetable/gmonggo.jpeg', category: 'vegetable' },
    
    

    // Snacks 
    { name: 'Beef Nachos', price: 150, imageURL: 'menupics/snacks/nachos.jpg', category: 'snacks' },
    { name: 'Shoesting Fries', price: 80, imageURL: 'menupics/snacks/sfries.jpg', category: 'snacks' },
    { name: 'Curly Fries', price: 80, imageURL: 'menupics/snacks/cfries.jpg', category: 'snacks' },
    { name: 'Criscross Fries', price: 80, imageURL: 'menupics/snacks/ccfries.jpg', category: 'snacks' },

    // Add Ons
    { name: 'Plain Rice', price: 15, imageURL: 'menupics/addons/price.jpg', category: 'addon' },
    { name: 'Garlic Rice', price: 20, imageURL: 'menupics/addons/grice.jpg', category: 'addon' },
    { name: 'Egg', price: 15, imageURL: 'menupics/addons/egg.jpg', category: 'addon' },

    // Drinks
    { name: 'Bottled Water', price: 20, imageURL: 'menupics/drinks/water.jpg', category: 'drinks' },
    { name: 'Ice Tea', price: 25, imageURL: 'menupics/breakfast/icetea.jpeg', category: 'drinks' },
    { name: 'Coffee', price: 25, imageURL: 'menupics/breakfast/coffee.jpg', category: 'drinks' },
    { name: 'Soda Mismo', price: 20, imageURL: 'menupics/drinks/sodam.jpg', category: 'drinks' },
    { name: 'Soda Liter ', price: 75, imageURL: 'menupics/drinks/sodal.jpg', category: 'drinks' },
];

function renderMenu(category) {
    const menuSide = document.querySelector('.menu-side');
    menuSide.innerHTML = '';
  
    menuItems.forEach((item) => {
      if (item.category === category) {
        const menuItem = document.createElement('div');
        menuItem.classList.add('menu-item');
  
        const imageContainer = document.createElement('div');
        imageContainer.classList.add('image-container');
  
        const image = document.createElement('img');
        image.src = `${item.imageURL}`;
        image.alt = `${item.name}`;
        image.dataset.itemName = item.name;
        image.dataset.itemPrice = item.price;
        image.addEventListener('click', () => addToCart(item));
  
        imageContainer.appendChild(image);
  
        const itemName = document.createElement('div');
        itemName.classList.add('item-name');
        itemName.textContent = item.name;
        imageContainer.appendChild(itemName);
  
        menuItem.appendChild(imageContainer);
        menuSide.appendChild(menuItem);
      }
    });
  }

function selectCategory(category) {
    const categories = document.querySelectorAll('.category');
    categories.forEach((cat) => cat.classList.remove('active'));
    const selectedCategory = document.querySelector(`[data-category="${category}"]`);
    selectedCategory.classList.add('active');

    renderMenu(category);
}

function addToCart(item) {
    const cartItems = document.querySelector('.cart-items');

    const cartItem = document.createElement('div');
    cartItem.classList.add('cart-item');
    cartItem.textContent = `${item.name} - ₱${item.price.toFixed(2)}`;
    cartItem.dataset.itemPrice = item.price;

    const removeButton = document.createElement('button');
    removeButton.textContent = 'Remove';
    removeButton.addEventListener('click', () => removeFromCart(cartItem));

    cartItem.appendChild(removeButton);
    cartItems.appendChild(cartItem);

    updateTotal();
}

function removeFromCart(cartItem) {
    cartItem.remove();
    updateTotal();
}

function updateTotal() {
    const cartItems = document.querySelectorAll('.cart-item');
    let total = 0;

    cartItems.forEach((item) => {
        const price = parseFloat(item.dataset.itemPrice);
        total += price;
    });

    const cartTotal = document.querySelector('.cart-total');
    cartTotal.textContent = `Total: ₱${total.toFixed(2)}`;
}

function clearCart() {
    const cartItems = document.querySelector('.cart-items');
    cartItems.innerHTML = '';
    updateTotal();
}

function renderSearchResults(items) {
    // Function to render search results
    const menuSide = document.querySelector('.menu-side');
    menuSide.innerHTML = '';
  
    items.forEach(item => {
      const menuItem = document.createElement('div');
      menuItem.classList.add('menu-item');
      const image = document.createElement('img');
      image.src = `${item.imageURL}`;
      image.alt = `${item.name}`;
      image.dataset.itemName = item.name;
      image.dataset.itemPrice = item.price;
      image.addEventListener('click', () => addToCart(item));
  
      menuItem.appendChild(image);
      menuSide.appendChild(menuItem);
    });
  }
  
  // Event listener for the clear cart button
  const clearCartBtn = document.querySelector('.clear-cart-btn');
  clearCartBtn.addEventListener('click', clearCart);
  
  // Event listener for the checkout button
  const checkoutBtn = document.querySelector('.checkout-btn');
  checkoutBtn.addEventListener('click', () => alert('Implement your checkout logic here!'));
  
  // Event listeners for category selection and search
  document.addEventListener('DOMContentLoaded', () => {
    // Initialize the page with the default category
    selectCategory('breakfast');
  
    // Event listeners for category selection
    const categories = document.querySelectorAll('.category');
    categories.forEach((category) => {
      category.addEventListener('click', () => {
        const selectedCategory = category.dataset.category;
        selectCategory(selectedCategory);
      });
    });
  
    // Event listener for search button
    const searchButton = document.querySelector('.search-category');
    searchButton.addEventListener('click', () => {
      const searchTerm = prompt('Enter the item you want to search for:');
      if (searchTerm) {
        const matchingItems = menuItems.filter(item =>
          item.name.toLowerCase().includes(searchTerm.toLowerCase())
        );
        renderSearchResults(matchingItems);
      }
    });
  })
