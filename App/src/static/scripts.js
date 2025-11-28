document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card-animate");

    // Efeito de entrada com atrasos em cascata
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.15}s`;
    });

    // Animação sutil de flutuação
    cards.forEach(card => {
        card.addEventListener("mouseenter", () => {
            card.style.transition = "transform 0.25s ease";
            card.style.transform = "translateY(-6px) scale(1.03)";
        });

        card.addEventListener("mouseleave", () => {
            card.style.transform = "translateY(0) scale(1)";
        });
    });
});

function listar() {
    window.location.href = "http://127.0.0.1:5000/listaSkins";
}


