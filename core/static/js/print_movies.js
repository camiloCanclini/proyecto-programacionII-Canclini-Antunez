(function (){
    var url = 'http://127.0.0.1:5000/services/get_movies';
    const container = document.getElementById('container__cajas');
    console.log('url:', url)
    const HTTPREQUEST = new XMLHttpRequest(); //Se crea objeto HTTPREQUEST
    HTTPREQUEST.open('GET',url, true); //Se configura la petición
    /*Comienzan las operaciones AJAX*/
    HTTPREQUEST.onreadystatechange = function(){
        /*Se verifica que la petición fue exitosa*/
        if(this.readyState == 4 && this.status == 200){
            const response = JSON.parse(this.responseText);//Se obtiene la respuesta de la API y se transforma array
            console.log(response);

            for (const i of response["Movies"]){

                /*Creacion elementos*/

                const cajas = document.createElement("DIV");
                cajas.setAttribute("class","cajas");

                const caja_principal = document.createElement("DIV");
                caja_principal.setAttribute("class","caja-principal");
                cajas.appendChild(caja_principal);
                

                const cajas_p1 = document.createElement("DIV");
                cajas_p1.setAttribute("class","cajas-p1");
                caja_principal.appendChild(cajas_p1);

                const imagen = document.createElement("IMG");
                imagen.setAttribute("src",i['Poster']);
                cajas_p1.appendChild(imagen);

                const cajas_p2 = document.createElement("DIV");
                cajas_p2.setAttribute("class","cajas-p2");
                caja_principal.appendChild(cajas_p2);

                const delete_ = document.createElement("DIV");
                delete_.setAttribute("id","delete");
                cajas_p2.appendChild(delete_);

                const icono_delete = document.createElement("i");
                icono_delete.setAttribute("class","fa-regular fa-pen-to-square");
                delete_.appendChild(icono_delete);

                const movie_title = document.createElement("H3");
                movie_title.setAttribute("class","movie-title");
                cajas_p2.appendChild(movie_title);

                const movie_info = document.createElement("DIV");
                movie_info.setAttribute("class","movie-info");
                cajas_p2.appendChild(movie_info);

                const a = document.createElement("SPAN");
                a.setAttribute("id","sinopsis");
                const b = document.createElement("SPAN");
                const c = document.createElement("SPAN");
                const d = document.createElement("SPAN");

                movie_info.appendChild(a);
                movie_info.appendChild(b);
                movie_info.appendChild(c);
                movie_info.appendChild(d);
                
                const comments = document.createElement("DIV");
                comments.setAttribute("id","comments");
                cajas.appendChild(comments);

                comentarios = document.createElement("H3");
                comments.appendChild(comentarios);

                const comments_container = document.createElement("DIV");
                comments_container.setAttribute("class","comments-container");
                comments.appendChild(comments_container);

                for (const j of i["Comments"]) {

                    const comment = document.createElement("DIV");
                    comment.setAttribute("class","comment");
                    comments_container.appendChild(comment);
                    
                    const nombre_comment = document.createElement("SPAN");
                    comment.appendChild(nombre_comment);
                    nombre_comment.innerHTML = j["Username"];

                    const text_comment = document.createElement("SPAN");
                    comment.appendChild(text_comment);
                    text_comment.innerHTML = j["Comment"];
                }

                movie_title.innerHTML = i["Title"];
                a.innerHTML = i["Plot"];
                b.innerHTML = "Director: "+i["Director"];
                c.innerHTML = "Año: "+i["Year"];
                d.innerHTML = "Genero: "+i["Genre"];
                container.appendChild(cajas);
            }
        }
    }
    HTTPREQUEST.send();
})();
