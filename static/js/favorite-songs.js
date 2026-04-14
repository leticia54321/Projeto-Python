const openModalButtons = document.querySelectorAll('.btn-addMusic');

openModalButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modalId = button.getAttribute('data-modal');
        const modal = document.getElementById(modalId);
        modal.showModal();
    });
});

const closeMoldaButtons = document.querySelectorAll('.btn-closeModal');
closeMoldaButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modalId = button.getAttribute('data-modal');
        const modal = document.getElementById(modalId);
        modal.close();
    });
});