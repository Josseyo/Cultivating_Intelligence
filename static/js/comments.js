document.addEventListener("DOMContentLoaded", function() {
    const deleteModalElement = document.getElementById("deleteModal");
    if (!deleteModalElement) {
        console.error("Delete modal not found.");
        return;
    }
    const deleteModal = new bootstrap.Modal(deleteModalElement);
    
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    const deleteConfirm = document.getElementById("deleteConfirm");

    // Add event listeners for edit buttons
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

    // Add event listener for delete buttons using event delegation
    document.addEventListener("click", (e) => {
        if (e.target.classList.contains("btn-delete")) {
            const commentId = e.target.getAttribute("data-comment_id");
            deleteConfirm.href = `delete_comment/${commentId}`;
            deleteModal.show();
        }
    });
});
