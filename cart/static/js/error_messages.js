document.getElementById('applyPromoButton').addEventListener('click', function() {
    var promoCode = document.getElementById('promoCode').value.trim();
    var promoErrorMessage = document.getElementById('promoErrorMessage');
    promoErrorMessage.textContent = 'The promo code is invalid.';
    promoErrorMessage.style.display = 'block';
});

document.getElementById('applyGiftCardButton').addEventListener('click', function() {
    var giftCardCode = document.getElementById('giftCardCode').value.trim();
    var giftCardErrorMessage = document.getElementById('giftCardErrorMessage');
    giftCardErrorMessage.textContent = 'The gift card code is invalid.';
    giftCardErrorMessage.style.display = 'block';
});