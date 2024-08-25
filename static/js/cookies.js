document.addEventListener("DOMContentLoaded", function() {
    window.cookieconsent.initialise({
        palette: {
            popup: { background: "#AFDBF6" },
            button: { background: "#F4F4F4" }
        },
        theme: "edgeless",
        content: {
            header: "We use cookies",
            message: "This website uses cookies to ensure you get the best experience.",
            dismiss: "I agree",
        }
    });
});