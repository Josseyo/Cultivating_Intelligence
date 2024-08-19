const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Add event listeners for edit buttons
Array.from(editButtons).forEach(button => {
    button.addEventListener("click", (e) => {
        const commentId = e.target.getAttribute("data-comment_id");
        const commentContent = document.getElementById(`comment${commentId}`).innerText;
        
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
        
        console.log(`edit_comment/${commentId}`);
    });
});

// Add event listeners for delete buttons
Array.from(deleteButtons).forEach(button => {
    button.addEventListener("click", (e) => {
        const commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
});
