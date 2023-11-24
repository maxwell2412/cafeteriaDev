function add_pedido(){

    container = document.getElementById("form-pedido")

    html = "<br><div class='row'> <div class='col-md'> <input type='text' placeholder='Tipo de pedido' class='form-control' name='pedido'></div> <div class='col-md'><input type='number' placeholder='Tamanho 100, 250, 500' class='form-control' name='tamanho'> </div><div class='col-md'><input type='number' placeholder='Mesa do cliente' class='form-control' name='mesa'></div></div>"

    container.innerHTML += html


}

function exibir_form(tipo){
    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att_cliente')

    if(tipo == "1"){
        att_cliente.style.display = "none" 
        add_cliente.style.display = "block"
    }else{
        if(tipo == "2"){
        att_cliente.style.display = "block"
        add_cliente.style.display = "none"
    }
}
}