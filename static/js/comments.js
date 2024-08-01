document.addEventListener("DOMContentLoaded", () => {
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    /*const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteConfirm = document.getElementById("deleteConfirm");*/

    /* Event delegation for edit and delete buttons */
    document.addEventListener("click", (e) => {
        // Handle edit button click
        if (e.target.classList.contains("btn-edit")) {
            const commentId = e.target.getAttribute("comment_id");
            const commentContent = document.getElementById(`comment${commentId}`).innerText;
            
            commentText.value = commentContent;
            submitButton.innerText = "Update";
            commentForm.setAttribute("action", `edit_comment/${commentId}`);
        }

        // Handle delete button click
        if (e.target.classList.contains("btn-delete")) {
            const commentId = e.target.getAttribute("comment_id");
            deleteConfirm.href = `delete_comment/${commentId}`;
            deleteModal.show();
        }
    });
});
