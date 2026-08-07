function copyHash(textareaId) {

    const textarea = document.getElementById(textareaId);

    if (!textarea) return;

    navigator.clipboard.writeText(textarea.value)
        .then(() => {

            alert("Hash copied successfully!");

        })
        .catch(() => {

            alert("Unable to copy hash.");

        });

}
