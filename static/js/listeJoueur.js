
document.addEventListener('DOMContentLoaded', () => {
    const listeItems = document.querySelectorAll('.liste-item');
    
    listeItems.forEach(item => {
        const toggleIcon = item.querySelector('.logo-plus'); // Sélection de l'icône à changer
        const details = item.querySelector('.details'); // Section des détails
        
        item.addEventListener('click', (e) => {
            // Vérifiez si l'élément cliqué est autre que l'icône pour gérer l'action sur l'élément
            if (e.target === toggleIcon) return; // Si on clique sur l'icône, on ne fait rien ici

            item.classList.toggle('active'); // Active ou désactive l'élément

            // Changement de l'icône
            if (item.classList.contains('active')) {
                toggleIcon.classList.remove('fa-plus');
                toggleIcon.classList.add('fa-minus');
                details.style.display = 'block'; // Affiche les détails
            } else {
                toggleIcon.classList.remove('fa-minus');
                toggleIcon.classList.add('fa-plus');
                details.style.display = 'none'; // Masque les détails
            }
        });
    });
});


