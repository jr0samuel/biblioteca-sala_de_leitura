function buscar_livro() {
    let input = document.getElementById('buscarlivros').value
    input=input.toLowerCase();
    let x = document.getElementsByClassName('cartao');
    
    for (i = 0; i < x.length; i++) {
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].style.display="none";
        }
        else {
            x[i].style.display="list-item";
        }
    }
}
