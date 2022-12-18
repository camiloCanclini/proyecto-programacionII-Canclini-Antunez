/*   APIKEY = cf09fe5c    */
//const url = 'http://www.omdbapi.com/?apikey=cf09fe5c&s=batman';//Se fija la URL de la API con la que haremos la consulta
console.log("hola");
const form = document.getElementById('form_api_search');
form.addEventListener('submit', event => {
	event.preventDefault();//Evita que el formulario recargue la pagina
	let input_search = document.getElementById('input_search');
	console.log('input_search:', input_search)
	let input_search_text = input_search.value;
    console.log(input_search_text);
	var url = 'http://www.omdbapi.com/?apikey=cf09fe5c&s='+input_search_text;
	console.log('url:', url)
	const HTTPREQUEST = new XMLHttpRequest(); //Se crea objeto HTTPREQUEST
	HTTPREQUEST.open('GET',url, true); //Se configura la petición
    /*Comienzan las operaciones AJAX*/
	HTTPREQUEST.onreadystatechange = function(){
        /*Se verifica que la petición fue exitosa*/
		if(this.readyState == 4 && this.status == 200){
			var response = JSON.parse(this.responseText);//Se obtiene la respuesta de la API y se transforma array
            console.log(response);
			try {
				let movies = response["Search"];
				displayResponse(movies);
			} catch (error) {
				displayResponse(movies=0, 1);
			}
		}
	}
	HTTPREQUEST.send();
});

function displayResponse(movies, error=0){
	let container = document.getElementById('display_movies'); 
	container.removeAttribute("style");
	container.innerHTML = "";
	if(error==1){
		container.innerHTML = "LA BUSQUEDA DE LA PELICULA A FALLADO O NO EXISTE";
	}else{	
		/*Se recorre el ARRAY y se pintan los datos que contiene*/
		for(let i of movies){
			let container_movie = document.createElement("DIV");
			let link = document.createElement("A");
			let movieImg = document.createElement("IMG");
			let movieInfo = document.createElement("DIV");
			let titulo = document.createElement("P");
			let id = document.createElement("P");
	
			movieImg.setAttribute("src",i["Poster"]);
			titulo.innerHTML = i["Title"];
			id.innerHTML = i["imdbID"];
			link.setAttribute("HREF", "/user/addMovie?id="+i["imdbID"])
	
			movieInfo.appendChild(titulo);
			movieInfo.appendChild(id);
			link.appendChild(movieImg);
			link.appendChild(movieInfo);
			container_movie.appendChild(link);
	
			container.appendChild(container_movie);
		}
	}
}