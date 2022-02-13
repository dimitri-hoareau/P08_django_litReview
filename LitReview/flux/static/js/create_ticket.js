window.onload = function () {
    document.getElementById("id_rating").setAttribute("max", "5")

    let bodyInput = document.getElementById("id_body");
    let textarea = document.createElement('textarea');
    textarea.setAttribute('id',bodyInput.id);
    textarea.setAttribute('type',bodyInput.type);
    textarea.setAttribute('name',bodyInput.name);
    textarea.setAttribute('maxlength',bodyInput.maxlength);
    textarea.innerHTML = bodyInput.innerHTML;
    bodyInput.parentNode.replaceChild(textarea, bodyInput);

}

