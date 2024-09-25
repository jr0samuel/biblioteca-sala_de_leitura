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
// talvez eu faça essa função para as tabelas da professora

function outroTR() {
    let tabela = document.querySelector('#tabela123')
    tabela.innerHTML += `<tr>
        <td scope="row"><input type="text" class="form-control campos" name="nome_aluno" aria-label="Nome do Aluno" aria-describedby="basic-addon1"></td>
        <td><input type="text" class="form-control campos" name="livro" aria-label="Livro" aria-describedby="basic-addon1"></td>
        <td><input type="text" class="form-control campos" name="data_de_emprestimo" aria-label="Data de Empréstimo" aria-describedby="basic-addon1"></td>
        <td><input type="text" class="form-control campos" name="data_de_devolucao" aria-label="Data de Devolução" aria-describedby="basic-addon1"></td>
    </tr>`
}
// salvarTabela();   depois de </tr>`

// const localStorageKey = 'tabela-prof'
// const campo = document.querySelectorAll('.campos')

// function salvarTabela(){
//     if(campo.value){
//         let infos = JSON.parse(localStorage.getItem(localStorageKey) || "[]")
//         infos.push({info: campo.value})
//         localStorage.setItem(localStorageKey, JSON.stringify(infos))
//         showInfos()
//     }
// }
// function showInfos(){
//     let infos = JSON.parse(localStorage.getItem(localStorageKey) || "[]")
//     let nuevaLinea = document.querySelector('#T_Body')
//     nuevaLinea.innerHTML = ""
//     for(let i=0; i<infos.length; i++){
//         nuevaLinea.innerHTML += `<tr>
//         <td scope="row">
//             <input type="text" class="form-control campos" name="nome_aluno" aria-label="Nome do Aluno" aria-describedby="basic-addon1">
//         </td>
//         <td>
//             <input type="text" class="form-control campos" name="livro" aria-label="Livro" aria-describedby="basic-addon1">
//         </td>
//         <td>
//             <input type="text" class="form-control campos" name="data_de_emprestimo" aria-label="Data de Empréstimo" aria-describedby="basic-addon1">
//         </td>
//         <td>
//             <input type="text" class="form-control campos" name="data_de_devolucao" aria-label="Data de Devolução" aria-describedby="basic-addon1">
//         </td>
//         </tr>`
//     }
// }
// showInfos()





// function outroTR() {
//     var tabela = document.getElementById("minhaTabela").getElementsByTagName('tbody')[0];
//     var novaLinha = tabela.insertRow();

//     for (var i = 0; i < 5; i++) {
//         var novaCelula = novaLinha.insertCell();
//         novaCelula.innerHTML = "";
//     }

//     salvarTabela();

// }

// function salvarTabela() {
//     var tabela = document.getElementById('tabela123').innerHTML;
//     localStorage.setItem("tabela", tabela);
// }
// function carregarTabela() {
//     let tabelaSalva = localStorage.getItem("tabela");
//     if (tabelaSalva) {
//         document.getElementById("tabela123").innerHTML = tabelaSalva;
//     }
// }
// window.onload = carregarTabela;



// $(document).ready(function() {
//     console.log('jQuery carregado!');
// });