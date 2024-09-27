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




function outroTR() {
    let tabela = document.querySelector('#tabela123')
    tabela.innerHTML += `<tr>
        <td scope="row"><input type="text" class="form-control campos" name="nome_aluno" aria-label="Nome do Aluno" aria-describedby="basic-addon1"></td>
        <td><input type="text" class="form-control campos" name="livro" aria-label="Livro" aria-describedby="basic-addon1"></td>
        <td><input type="text" class="form-control campos" name="data_de_emprestimo" aria-label="Data de Empréstimo" aria-describedby="basic-addon1"></td>
        <td><input type="text" class="form-control campos" name="data_de_devolucao" aria-label="Data de Devolução" aria-describedby="basic-addon1"></td>
    </tr>`
}
