let imgInp= document.getElementById('img-inp');
let imgTag = document.getElementById('img-tag');
imgInp.addEventListener('change', () => {
    let fileName = document.querySelector('input[type=file]').files[0];
    imgTag.innerHTML = fileName.name;
    imgTag.style.color = '#0c800c';
})