var selectedrow=0;
var taskid;
$( document ).ready(function() {

  var table = $('#userTable').DataTable({
        "order": [[ 0, "desc" ]],
        "columns": [{
        "title": "Taskid",
        "data": "taskId"
      },
      {
        "title": "Title",
        "data": "taskTitle"
      },
      {
        "title": "Description",
        "data": "taskDescription"
      },
      {
        "title": "Status",
        "data": "status"
      }
    ]

  });
       $('#userTable tbody').on( 'click', 'tr', function () {
        if ( $(this).hasClass('selected') ) {
            $(this).removeClass('selected');
            selectedrow=0;
        }
        else {
            table.$('tr.selected').removeClass('selected');
            $(this).addClass('selected');
            selectedrow=1;
        }
    } );

//load username in for ADD Task
$('#addusername').on('click',function(){
  var response=getAjax("loadusername",{'userid':1})
  $('#taskusername').empty()
  for (var key in response) {
    if (response.hasOwnProperty(key)) {
    $('<option>').val(key).text(response[key]).appendTo('#taskusername');
    }
}

})
//add..
$('#addTask').on('click',function(){

var taskuserid=$('#taskusername').val()
var tasktitle=$('#tasktitle').val().trim()
var taskdescription=$('#taskdesc').val().trim()
var response=postAjax("addtask",{'userID':taskuserid,'taskTitle':tasktitle,'taskDescription':taskdescription,'status':'to be done'})
    alert(response)

})

//update- fetch all the selected attr

$('#updategetselected').click( function () {
 if(checkrowselected()){
      var ids = $.map(table.rows('.selected').data(), function (item) {
        return item[0]
    });
    taskid=table.rows('.selected').data()[0]['taskId'][0]
    var title=table.rows('.selected').data()[0]['taskTitle'][0]
    var taskdesc=table.rows('.selected').data()[0]['taskDescription'][0]
    var status=table.rows('.selected').data()[0]['status'][0]

    var taskuserid=$('#loadusers').val()
    $("#updatetasktitle").val(title)
    $("#updatetaskdesc").val(taskdesc)
    $("#status").val(status)
}else{
alert("Please select a row from DataTable!")
 return false;
}

});


//update..
$('#updateTask').click( function () {
    var response=postAjax("updatetask",{'taskid':taskid,'title':$("#updatetasktitle").val().trim(),'taskdesc':$("#updatetaskdesc").val().trim(),'status':$("#status").val().trim(),'taskuserid':$('#loadusers').val().trim()})
    alert(response)
});

//delete..
$('#button_delete').click( function () {
 if(checkrowselected()){
    var ids = $.map(table.rows('.selected').data(), function (item) {
        return item[0]
    });
    taskid=table.rows('.selected').data()[0]['taskId'][0]

  var response=postAjax("deletetask",{'taskid':taskid,'taskuserid':$('#loadusers').val().trim()})
  alert(response)
  table.row('.selected').remove().draw( false );
  selectedrow=0;
 }else{
    alert("Please select a row from DataTable!")
 return false;

    }
 });

//get user task...
$('#loadusers').change(function(){
  var userid= $(this).val();
  if(userid!=0){
  var response=getAjax("fetchtask",{'userid':userid})
  table.clear();
  table.rows.add(response).draw();
}else{
alert("select a valid user!")
return false;
}

});

function checkrowselected(){
   if(selectedrow==1){
   return true;
   }
   return false;
}


});