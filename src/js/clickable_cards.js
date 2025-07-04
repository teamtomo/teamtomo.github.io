let cardsInitialized = false;

function initializeCards() {
  const cards = document.querySelectorAll('.card');
  
  if (cards.length === 0) {
    cardsInitialized = false;
    return;
  }
  
  if (cardsInitialized) return; // Already initialized
  
  cards.forEach((card, index) => {
    card.addEventListener('click', function() {
      let url;

      const cardContent = this.textContent;
      if (cardContent.includes('Input/Output')) {
        url = '/site/io_packages';
      } else if (cardContent.includes('Primitives')) {
        url = '/site/primitives';
      } else if (cardContent.includes('Algorithms')) {
        url = '/site/algorithms';
      }

      window.location.href = url;
    });
  });
  
  cardsInitialized = true;
}

// Check every 500ms for cards
setInterval(initializeCards, 500);

// Also run on common events
document.addEventListener('DOMContentLoaded', initializeCards);
window.addEventListener('load', initializeCards);
window.addEventListener('popstate', initializeCards); // Browser back/forward
