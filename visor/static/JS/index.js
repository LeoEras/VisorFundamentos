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

function ClickEvent(event){
    AttachID();
    var list_id = $(".identificadores");
    for(var i = 0; i < list_id.length; i++){
        list_id[i] = list_id[i].innerText;
    }
    alert(event.target.id);
}