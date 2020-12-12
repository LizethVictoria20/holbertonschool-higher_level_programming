$(document).ready(function () {
  $('div#add_item').click(() => {
    $('ul').append('<li>Item</li>');
  });

  $('div#remove_item').click(() => {
    $('.my_list li').last().remove();
  });

  $('div#clear_list').click(() => {
    $('.my_list li').remove();
  });
});
