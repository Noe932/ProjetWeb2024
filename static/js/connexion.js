document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Empêche l'envoi du formulaire

    const nom = document.getElementById('nom').value;
    const prenom = document.getElementById('prenom').value;

    // Vérifier si le nom et le prénom correspondent à un compte existant
    console.log(`Tentative de connexion avec le nom: ${nom}, prénom: ${prenom}`);

    // Simuler une vérification : afficher un message dans la console
    alert(`Vous êtes connecté(e) en tant que ${prenom} ${nom}`);

    // Rediriger vers la page principale ou le tableau de bord (si l'utilisateur est validé)
    window.location.href = 'index.html';
});
