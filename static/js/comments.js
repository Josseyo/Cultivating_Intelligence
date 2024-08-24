document.addEventListener("DOMContentLoaded", function() {
    const deleteModalElement = document.getElementById("deleteModal");
    console.log(deleteModalElement); // Check if this is null or undefined
    const deleteModal = new bootstrap.Modal(deleteModalElement);

    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    const deleteButtons = document.getElementsByClassName("btn-delete");
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

    // Add event listeners for delete buttons
    Array.from(deleteButtons).forEach(button => {
        button.addEventListener("click", (e) => {
            const commentId = e.currentTarget.getAttribute("data-comment_id");
            deleteConfirm.href = `delete_comment/${commentId}`;
            deleteModal.show();
        });
    });
});
