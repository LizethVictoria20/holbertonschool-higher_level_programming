$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (key, value) {
        const title = value.title;
        $('ul#list_movies').append($(`<li>${title}</li>`));
      });
    }
  });
});
