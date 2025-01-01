document.addEventListener('DOMContentLoaded', function () {
    const imageFields = document.querySelectorAll('input[type="file"]');
    imageFields.forEach(field => {
        field.addEventListener('change', function () {
            const reader = new FileReader();
            reader.onload = function (e) {
                const imgPreview = document.createElement('img');
                imgPreview.src = e.target.result;
                imgPreview.style.maxWidth = '200px';
                imgPreview.style.marginTop = '10px';
                field.parentNode.appendChild(imgPreview);
            };
            reader.readAsDataURL(field.files[0]);
        });
    });
});
