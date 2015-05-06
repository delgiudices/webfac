$(".delete_icon").click(function() {
  var delete_icon_clicked = $(this);
  $("#delete_modal").modal('show');
  $("#confirm_delete_button").click(function(){
    delete_icon_clicked.children('form').submit();
  });
});
