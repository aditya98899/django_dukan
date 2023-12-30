let products = document.querySelectorAll('.product-card')
console.log(products.length)

products.forEach(card =>{
   card.addEventListener('mouseover', () => {
    card.style.transform = 'scale(1.1) rotate(0deg)'
    card.querySelector('.product-img').style.filter = 'grayscale(0)'
   })
   card.addEventListener('mouseout', () => {
    card.style.transform = 'scale(1) rotate(0deg)'
    card.querySelector('.product-img').style.filter = 'grayscale(100)'
   })

})