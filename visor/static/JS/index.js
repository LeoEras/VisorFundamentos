function AttachID(){
    var list_id = $(".identificadores");

    var rows = $(".rows");
    for(var i = 0; i < rows.length; i++){
        try{
           rows[i].id = list_id[i].innerText;
        } catch(e){
           console.log("YO",e)
        }
    }
}

function getCookie(name) {
       var cookieValue = null;
       if (document.cookie && document.cookie != '') {
         var cookies = document.cookie.split(';');
         for (var i = 0; i < cookies.length; i++) {
         var cookie = jQuery.trim(cookies[i]);
         // Does this cookie string begin with the name we want?
         if (cookie.substring(0, name.length + 1) == (name + '=')) {
             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
             break;
          }
     }
 }
 return cookieValue;
}

function SelectEvent(){
    event.preventDefault();
    var csrftoken = getCookie('csrftoken');
    var selected_folder = $("#select").find(":selected").text();
    $.ajax({
         url : window.location.href, // the endpoint,commonly same url
         type : "POST", // http method
         data : { csrfmiddlewaretoken : csrftoken,
         selected : selected_folder,
    }, // data sent with the post request
    success : function(json) {
        //$("#selectMSG").text("No cumple con especificaciones");
     },

     // handle a non-successful response
     error : function(xhr,errmsg,err) {
        //console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
     }});
}

function ClickEvent(event){
    event.preventDefault();
    AttachID();
    var csrftoken = getCookie('csrftoken');
    var item_id = event.target.id;
    var allrows = $(".rows");
    var allitems = [];
    var selected_folder = $("#select").find(":selected").text();
    console.log(selected_folder);
    for (var i = 0; i < allrows.length; i++) {
        allitems[i] = allrows[i].id;
    }
    var index = allitems.indexOf(item_id);
    var allerrors = $(".errors");
    var line_error = allerrors[index];
    var selected_folder = $("#select").find(":selected").text();
    $.ajax({
         url : window.location.href, // the endpoint,commonly same url
         type : "POST", // http method
         data : { csrfmiddlewaretoken : csrftoken,
         id : item_id,
         selected : selected_folder,
    }, // data sent with the post request
    success : function(json) {
        var file_text = json.file_open;
        file_text = file_text.replace(/(?:\r\n|\r|\n)/g, '<br />');
        file_text = file_text.replace(/(?:\r\t|\r|\t)/g, '&emsp;&emsp;');
        document.getElementById("textarea").innerHTML = file_text;
        var allchildren = document.getElementById("textarea").childNodes;
        var linesOnly = []
        var prev_tag;

        for (var i = 0; i < allchildren.length; i++) {
            if(allchildren[i].tagName != 'BR'){
                var newP = document.createElement("p");
                newP.innerHTML = allchildren[i].data;
                document.getElementById("textarea").replaceChild(newP, allchildren[i]);
            }
        }

        allchildren = document.getElementById("textarea").childNodes;
        for (var i = 0; i < allchildren.length; i++) {
            if (i > 0){
                prev_tag = allchildren[i - 1];
            }
            if((allchildren[i].tagName == 'BR' && prev_tag.tagName != 'BR') || (allchildren[i].tagName == 'BR' && prev_tag.tagName == 'BR')){
                linesOnly.push(allchildren[i - 1]);
            }
        }
        linesOnly.push(allchildren.pop);
        linesOnly[parseInt(line_error.innerText) - 1].style.color = 'red';
     },

     // handle a non-successful response
     error : function(xhr,errmsg,err) {
         console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
     }});
}