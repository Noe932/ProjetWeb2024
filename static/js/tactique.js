document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('container');
    const listeItems = document.querySelectorAll('.liste-item');
    const template = document.getElementById('draggable-template');

    // Création du bouton de sauvegarde
    const saveButton = document.createElement('button');
    saveButton.textContent = 'Sauvegarder la tactique';
    saveButton.style.position = 'fixed';
    saveButton.style.bottom = '20px';
    saveButton.style.right = '20px';
    saveButton.style.padding = '10px 20px';
    saveButton.style.backgroundColor = '#4CAF50';
    saveButton.style.color = 'white';
    saveButton.style.border = 'none';
    saveButton.style.borderRadius = '4px';
    saveButton.style.cursor = 'pointer';
    saveButton.style.zIndex = '1000';
    document.body.appendChild(saveButton);



    // Fonction pour récupérer les positions
function collectPositions() {
    const elements = document.querySelectorAll('.draggable-container');
    const positions = [];

    elements.forEach((element) => {
        const joueurNom = element.querySelector('.player-name').textContent;
        const roleButton = element.querySelector('.main-button');
        
        // Ne pas inclure les éléments par défaut
        if (joueurNom && roleButton.textContent !== 'Afficher la Liste' && roleButton.textContent !== 'Fermer') {
            // Enlever le "px" des positions et convertir en nombres
            const x = parseFloat(element.style.left) || 0;
            const y = parseFloat(element.style.top) || 0;

            // Récupération du rôle sélectionné via le bouton principal
            const selectedRole = roleButton.textContent.trim();
            const selectedItem = items.find(item => item.name === selectedRole);
            const roleId = selectedItem ? selectedItem.id : null;

            if (!roleId) {
                console.warn(`RoleId non trouvé pour le rôle: ${selectedRole}`);
            }

            positions.push({
                joueur: joueurNom.trim(),
                roleId: roleId,
                x: x,
                y: y
            });
        }
    });

    console.log("Positions collectées:", positions);
    return positions;
}


saveButton.addEventListener('click', async () => {
    const tactiqueName = prompt("Nom de la tactique :");
    if (!tactiqueName) return;

    const positions = collectPositions();

    // Debug: Afficher les positions collectées
    console.log("Positions à sauvegarder:", positions);

    if (positions.length === 0) {
        alert("Aucune position de joueur à sauvegarder !");
        return;
    }

    try {
        const response = await fetch('/save_tactique/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                nom: tactiqueName,
                positions: positions
            })
        });

        console.log("Réponse du serveur:", response.status);

        const data = await response.json();
        console.log("Données reçues:", data);

        if (response.ok) {
            alert(data.message);
        } else {
            throw new Error(data.message || 'Erreur lors de la sauvegarde');
        }
    } catch (error) {
        console.error("Erreur complète:", error);
        alert('Erreur lors de la sauvegarde : ' + error.message);
    }
});

// Fonction pour vérifier le CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



    listeItems.forEach(item => {
        const createButton = document.createElement('button');
        createButton.textContent = 'Créer un Joueur';
        createButton.style.marginLeft = '10px';
        createButton.style.backgroundColor = '#4CAF50';
        createButton.style.color = 'white';
        createButton.style.border = 'none';
        createButton.style.padding = '5px 10px';
        createButton.style.borderRadius = '4px';

        createButton.addEventListener('click', () => {
            const existingElements = document.querySelectorAll('.draggable-container');
            if (existingElements.length >= 11) {
                alert('Nombre maximum de joueurs atteint (11)');
                return;
            }

            const itemName = item.querySelector('span').textContent.trim();
            const draggableElement = template.content.cloneNode(true).firstElementChild;
            // Ajout du nom du joueur dans l'élément draggable
            const playerNameElement = draggableElement.querySelector('.player-name');
            playerNameElement.textContent = itemName;

            draggableElement.style.left = `${Math.random() * (container.clientWidth - 200)}px`;
            draggableElement.style.top = `${Math.random() * (container.clientHeight - 200)}px`;

            const mainButton = draggableElement.querySelector('.main-button');
            const listContainer = draggableElement.querySelector('.list-container');

            mainButton.textContent = 'Afficher la Liste';

            let isListVisible = false;
            let selectedItem = null;

            draggableElement.addEventListener('mousedown', dragElement);

            mainButton.addEventListener('click', () => {
                if (!isListVisible) {
                    listContainer.innerHTML = items.map(listItem => `
                        <div class="list-item" data-name="${listItem.name}">
                            ${listItem.name}
                            <div class="hover-card">
                                <h4>${listItem.name}</h4>
                                <p>${listItem.description}</p>
                            </div>
                        </div>
                    `).join('');
                    listContainer.style.display = 'block';
                    isListVisible = true;
                    mainButton.textContent = 'Fermer';

                    const listItems = listContainer.querySelectorAll('.list-item');
                    listItems.forEach(listItem => {
                        listItem.addEventListener('click', () => {
                            selectedItem = { name: listItem.dataset.name };
                            mainButton.textContent = selectedItem.name;

                            listContainer.style.display = 'none';
                            isListVisible = false;
                        });
                    });
                } else {
                    listContainer.style.display = 'none';
                    mainButton.textContent = selectedItem ? selectedItem.name : 'Afficher la Liste';
                    isListVisible = false;
                }
            });

            container.appendChild(draggableElement);
        });

        item.appendChild(createButton);
    });

    // Fonction utilitaire pour récupérer le cookie CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

function dragElement(e) {
    if (e.target.tagName.toLowerCase() === 'button') return;

    const element = e.currentTarget;
    const container = document.getElementById('container');
    let startX = e.clientX - element.offsetLeft;
    let startY = e.clientY - element.offsetTop;

    function moveElement(e) {
        let newLeft = e.clientX - startX;
        let newTop = e.clientY - startY;

        const containerRect = container.getBoundingClientRect();
        const elementRect = element.getBoundingClientRect();

        if (newLeft < 0) newLeft = 0;
        if (newTop < 0) newTop = 0;
        if (newLeft + elementRect.width > containerRect.width) {
            newLeft = containerRect.width - elementRect.width;
        }
        if (newTop + elementRect.height > containerRect.height) {
            newTop = containerRect.height - elementRect.height;
        }

        element.style.left = `${newLeft}px`;
        element.style.top = `${newTop}px`;
    }

    function stopMove() {
        document.removeEventListener('mousemove', moveElement);
        document.removeEventListener('mouseup', stopMove);
    }

    document.addEventListener('mousemove', moveElement);
    document.addEventListener('mouseup', stopMove);
}

// Gestion des détails dans la liste principale
document.addEventListener('DOMContentLoaded', () => {
    const listeItems = document.querySelectorAll('.liste-item');

    listeItems.forEach(item => {
        const toggleIcon = item.querySelector('.logo-plus');
        const details = item.querySelector('.details');

        item.addEventListener('click', (e) => {
            if (e.target === toggleIcon) return;

            item.classList.toggle('active');

            if (item.classList.contains('active')) {
                toggleIcon.classList.remove('fa-plus');
                toggleIcon.classList.add('fa-minus');
                details.style.display = 'block';
            } else {
                toggleIcon.classList.remove('fa-minus');
                toggleIcon.classList.add('fa-plus');
                details.style.display = 'none';
            }
        });
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('container');
    const template = document.getElementById('draggable-template');
    const loadButton = document.getElementById('loadTactiqueButton');

    loadButton.addEventListener('click', async () => {
        try {
            const response = await fetch('/get_tactiques/');
            const data = await response.json();

            // Logs de débogage
            console.log('Status de la réponse:', response.status);
            console.log('Response OK:', response.ok);
            console.log('Données reçues:', data);
            console.log('Nombre de tactiques:', data.tactiques ? data.tactiques.length : 'undefined');

            if (response.ok && data.tactiques && data.tactiques.length > 0) {
                const tactiquesList = data.tactiques.map(t =>
                    `${t.nom} (${t.positions.length} joueurs)`
                ).join('\n');

                console.log('Liste des tactiques:', tactiquesList); // Debug log

                const tactiqueNom = prompt(
                    `Choisissez une tactique à charger:\n${tactiquesList}`
                );

                if (tactiqueNom) {
                    const tactique = data.tactiques.find(t => t.nom === tactiqueNom);
                    console.log('Tactique sélectionnée:', tactique); // Debug log

                    if (tactique) {
                        // Nettoyer les positions existantes
                        const existingPositions = container.querySelectorAll('.draggable-container');
                        existingPositions.forEach(el => el.remove());

                        // Charger les nouvelles positions
                        tactique.positions.forEach(pos => {
                            console.log('Position en cours de traitement:', pos); // Debug log

                            const draggableElement = template.content.cloneNode(true).firstElementChild;
                            const playerNameElement = draggableElement.querySelector('.player-name');
                            playerNameElement.textContent = pos.joueur;

                            draggableElement.style.left = `${pos.x}px`;
                            draggableElement.style.top = `${pos.y}px`;

                            const mainButton = draggableElement.querySelector('.main-button');
                            const listContainer = draggableElement.querySelector('.list-container');

                            mainButton.textContent = 'Afficher la Liste';
                            let isListVisible = false;

                            mainButton.addEventListener('click', () => {
                                if (!isListVisible) {
                                    listContainer.innerHTML = items.map(listItem => `
                                        <div class="list-item" data-name="${listItem.name}" data-id="${listItem.id}">
                                            ${listItem.name}
                                            <div class="hover-card">
                                                <h4>${listItem.name}</h4>
                                                <p>${listItem.description}</p>
                                            </div>
                                        </div>
                                    `).join('');
                                    listContainer.style.display = 'block';
                                    isListVisible = true;
                                    mainButton.textContent = 'Fermer';

                                    const listItems = listContainer.querySelectorAll('.list-item');
                                    listItems.forEach(listItem => {
                                        listItem.addEventListener('click', () => {
                                            const selectedName = listItem.dataset.name;
                                            mainButton.textContent = selectedName;
                                            listContainer.style.display = 'none';
                                            isListVisible = false;
                                        });
                                    });
                                } else {
                                    listContainer.style.display = 'none';
                                    isListVisible = false;
                                }
                            });

                            // Présélectionner le rôle correspondant
                            const roleItem = items.find(item => item.id === pos.roleId);
                            console.log('Role trouvé:', roleItem); // Debug log
                            if (roleItem) {
                                mainButton.textContent = roleItem.name;
                            }

                            draggableElement.addEventListener('mousedown', dragElement);
                            container.appendChild(draggableElement);
                        });
                    }
                }
            } else {
                console.log('Condition non remplie:');
                console.log('- response.ok:', response.ok);
                console.log('- data.tactiques existe:', !!data.tactiques);
                console.log('- data.tactiques length:', data.tactiques ? data.tactiques.length : 'N/A');
                alert('Aucune tactique disponible.');
            }
        } catch (error) {
            console.error('Erreur complète:', error);
            alert('Erreur lors du chargement des tactiques');
        }
    });
});