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




// function outroTR1() {
//     let tabela1 = document.querySelector('#tabela_1')
//     tabela1.innerHTML += `<tr><td scope="row"><input type="text" class="form-control" aria-describedby="basic-addon1"></td>`
// }

const localStorage1 = 'tabela-um'
const input_display = document.querySelector('#inputDisplay')

function salvarInput1(){
    if(input_display.value){
        let infos = JSON.parse(localStorage.getItem(localStorage1) || "[]")
        infos.push({info: input_display.value})
        localStorage.setItem(localStorage1, JSON.stringify(infos))
        showInfos()
        console.log(input_display.value)
    }
}

function showInfos(){
    let infos = JSON.parse(localStorage.getItem(localStorage1) || "[]")
    let listagem = document.getElementById('planilha')
    listagem.innerHTML = ""
    for(let i = 0; i < infos.length; i++){
        listagem.innerHTML += `<li>${values[i]['info']}</li>`
    }
}
showInfos()
