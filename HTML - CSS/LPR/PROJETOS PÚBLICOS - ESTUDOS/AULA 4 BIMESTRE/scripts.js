
//Funções para alterar o background-color do título do Formulário
function alterar_back_titulo() {
  let back_titulo = document.getElementById("botao");
  back_titulo.style.backgroundColor = "#000";
}

function padrão_back_titulo() {
  let back_titulo = document.getElementById("botao");
  back_titulo.style.backgroundColor = "#9125f0";
}




 function buscarProduto() {
   let tbody = document.getElementById("tbody");

   let response = fetch("https://fakestoreapi.com/products")
     .then(function (responseData) {
       return responseData.json();
     })
     .then(function (jsonData) {
       console.log(jsonData);
       for (const post of jsonData) {
         let tr = tbody.insertRow();
         let td_id = tr.insertCell();
         let td_title = tr.insertCell();
         let td_descricao = tr.insertCell();
         let td_price = tr.insertCell();
         let td_image = tr.insertCell();

         var img = document.createElement("img");
         img.src = td_image.image;
         img.width = img.clientWidth;
         console.log(td_image.image);
         td_id.innerText = post.id;
         td_title.innerText = post.title;
         td_descricao.innerText = post.description;
         td_price.innerText = post.price;
         td_image.innerHTML = "<img width='55' src='" + post.image + "'</img>";
         //"<img src='" + td_image.image + "'</img>";

         console.log(post.id);
         console.log(post.title);
         console.log(post.description);
       }
     })
     .catch(function (e) {
       console.log("Deu erro");
     });
 }
