document.addEventListener("DOMContentLoaded", function () {
    /**
     * Initializes the delete modal and sets up event listeners for editing
     * and deleting comments once the DOM is fully loaded.
     */
    
    const deleteModalElement = document.getElementById("deleteModal");
    
    if (!deleteModalElement) {
        console.error("Delete modal not found.");
        return;
    }
    
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModa"));
  
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    const deleteConfirm = document.getElementById("deleteConfirm");

    /**
     * Adds event listeners to each edit button to handle comment editing.
     * When an edit button is clicked, it retrieves the comment ID and 
     * populates the comment text input for editing.
     */
    Array.from(editButtons).forEach(button => {
        button.addEventListener("click", (e) => {
            const commentId = e.currentTarget.getAttribute("data-comment_id");
            const commentContent = document.getElementById(`comment${commentId}`);

            if (commentContent) {
                commentText.value = commentContent.innerText;
                submitButton.innerText = "Update";
                commentForm.setAttribute("action", `edit_comment/${commentId}`);
            } else {
                console.error(`Comment with ID ${commentId} not found.`);
            }
        });
    });

    /**
     * Adds an event listener for delete buttons using event delegation.
     * When a delete button is clicked, it retrieves the comment ID and 
     * updates the delete confirmation link's href, then displays the modal.
     */
    document.addEventListener("click", (e) => {
        if (e.target.classList.contains("btn-delete")) {
            const commentId = e.target.getAttribute("data-comment_id");
            deleteConfirm.href = `delete_comment/${commentId}`;
            deleteModal.show();
        }
    });
});
