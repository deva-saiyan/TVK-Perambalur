


let lastFlipped = null;

document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', function() {
        if (lastFlipped && lastFlipped !== this) {
            lastFlipped.classList.remove('flipped'); // Reset previous card
        }
        this.classList.toggle('flipped'); // Flip the clicked card
        lastFlipped = this.classList.contains('flipped') ? this : null;
    });
});