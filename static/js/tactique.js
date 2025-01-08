const circles = document.querySelectorAll('.circle');

circles.forEach(circle => {
    let offsetX, offsetY;
    const dropdown = circle.querySelector('.dropdown');
    const dropdownText = dropdown.querySelector('.dropdown__text');
    const dropdownItems = dropdown.querySelectorAll('.dropdown__items li');
    const dropdownCheckbox = dropdown.querySelector('input[type="checkbox"]');

    // Gestion du clic sur les éléments de la liste
    dropdownItems.forEach(item => {
        item.addEventListener('click', () => {
            // Remplacer le texte du dropdown
            dropdownText.textContent = item.textContent;
            
            // Fermer le dropdown
            dropdownCheckbox.checked = false;
        });
    });

    circle.addEventListener('mousedown', (event) => {
        // Vérifier si le clic n'est pas sur le dropdown
        if (event.target.closest('.dropdown')) {
            return;
        }

        // Calculer l'écart entre la souris et le coin supérieur gauche du cercle
        offsetX = event.clientX - circle.offsetLeft;
        offsetY = event.clientY - circle.offsetTop;

        // Activer le suivi de la souris
        const onMouseMove = (event) => {
            circle.style.left = `${event.clientX - offsetX}px`;
            circle.style.top = `${event.clientY - offsetY}px`;
        };

        // Ajouter les écouteurs pour le mouvement et la fin du clic
        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('mouseup', () => {
            document.removeEventListener('mousemove', onMouseMove);
        }, { once: true });
    });

    // Fermer tous les dropdowns si on clique en dehors
    document.addEventListener('click', (event) => {
        const dropdowns = circle.querySelectorAll('.dropdown input[type="checkbox"]');
        dropdowns.forEach(dropdown => {
            if (!circle.contains(event.target)) {
                dropdown.checked = false;
            }
        });
    });
});

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


document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('container') || document.body;
    const listeItems = document.querySelectorAll('.liste-item');

    listeItems.forEach(item => {
        const createCircleButton = document.createElement('button');
        createCircleButton.textContent = 'Créer un Joueur';
        createCircleButton.style.marginLeft = '10px';
        createCircleButton.style.backgroundColor = '#4CAF50';
        createCircleButton.style.color = 'white';
        createCircleButton.style.border = 'none';
        createCircleButton.style.padding = '5px 10px';
        createCircleButton.style.borderRadius = '4px';

        createCircleButton.addEventListener('click', () => {
            // Vérifier le nombre de cercles existants
            const existingCircles = document.querySelectorAll('.circle');
            if (existingCircles.length >= 11) {
                alert('Nombre maximum de cercles atteint (11)');
                return;
            }

            // Extraire le texte du span
            const itemName = item.querySelector('span').textContent.trim();
            
            const circle = document.createElement('div');
            circle.classList.add('circle');
            
            // Position aléatoire
            circle.style.left = `${Math.random() * (container.clientWidth - 50)}px`;
            circle.style.top = `${Math.random() * (container.clientHeight - 50)}px`;
            
            // Dropdown avec le nom exacte de l'item
            circle.innerHTML = `
                <div class="dropdown">
                    <input type="checkbox" id="dropdown-${Date.now()}">
                    <label for="dropdown-${Date.now()}" class="dropdown__text">${itemName}</label>
                    <div class="dropdown__arrow"></div>
                    <ul class="dropdown__items">
                        <li>${itemName}</li>
                        <li>Option</li>
                        <li>Option</li>
                    </ul>
                </div>
            `;
            
            container.appendChild(circle);
            
            // Réutilisation de la logique d'interaction existante
            const circles = document.querySelectorAll('.circle');
            
            circles.forEach(circleEl => {
                let offsetX, offsetY;
                const dropdown = circleEl.querySelector('.dropdown');
                const dropdownText = dropdown.querySelector('.dropdown__text');
                const dropdownItems = dropdown.querySelectorAll('.dropdown__items li');
                const dropdownCheckbox = dropdown.querySelector('input[type="checkbox"]');

                // Gestion du clic sur les éléments de la liste
                dropdownItems.forEach(dropdownItem => {
                    dropdownItem.addEventListener('click', () => {
                        dropdownText.textContent = dropdownItem.textContent;
                        dropdownCheckbox.checked = false;
                    });
                });

                circleEl.addEventListener('mousedown', (event) => {
                    if (event.target.closest('.dropdown')) {
                        return;
                    }

                    offsetX = event.clientX - circleEl.offsetLeft;
                    offsetY = event.clientY - circleEl.offsetTop;

                    const onMouseMove = (event) => {
                        circleEl.style.left = `${event.clientX - offsetX}px`;
                        circleEl.style.top = `${event.clientY - offsetY}px`;
                    };

                    document.addEventListener('mousemove', onMouseMove);
                    document.addEventListener('mouseup', () => {
                        document.removeEventListener('mousemove', onMouseMove);
                    }, { once: true });
                });
            });
        });

        item.appendChild(createCircleButton);
    });
});