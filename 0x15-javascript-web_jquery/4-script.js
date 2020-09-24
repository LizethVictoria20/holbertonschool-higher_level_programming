$('div#toggle_header').click(() => {
  $('header').addClass('red');
  if ($('header').hasClass('red')) {
    $('header').toggleClass('green');
  } else {
    $('header').toggleClass('red');
  }
});
