document.addEventListener('DOMContentLoaded', function() {
    const moveButtons = document.querySelectorAll('.move-button');
    const statusElements = document.querySelectorAll('.status');

    function toggleStatus(index) {
        const statusElement = statusElements[index];
        if (statusElement.textContent === 'Available') {
            statusElement.textContent = 'With Collector';
            statusElement.classList.remove('available');
            statusElement.classList.add('collector');
        } else {
            statusElement.textContent = 'Available';
            statusElement.classList.remove('collector');
            statusElement.classList.add('available');
        }
    }

    moveButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            toggleStatus(index);
        });
    });
});

