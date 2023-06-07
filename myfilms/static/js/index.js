// CSS



// /CSS

// GLOBALS - NOT SAFE

var counter = 1;

// /GLOBALS - NOT SAFE

function redirectToFilm() {
  document.location.hash = "page"
}

function load_more_button_on_click() {
  document.getElementById("load-more-button").remove();
  $(document).ready(function () {

    function displayNextFilms(page_num = 1) {
      const films_main_container = document.getElementById("films-main");
      var url = "load-more-films-index/?page=" + page_num;
      $.ajax({
        url: url,
        type: "GET",
        contentType: "application/JSON",
        dataType: "json",
        data: {
          page: page_num,
        },
        beforeSend: function () {},
        success: function (response) {
          const films = response.page_obj;
          if (films) {
            films.map((film) => {
              films_main_container.innerHTML += `<div class="film-elem">
                                                <a href="/films/${film.pk}" onclick="redirectToFilm()">
                                                <div class="film-thumb">
                                                  <img src="${
                                                    film.fields.film_thumb_image
                                                  }" alt="${
                film.fields.film_title
              }">
                                                </div>
                                                <div class="film-title">
                                                  ${film.fields.film_title.toUpperCase()}
                                                </div>
                                                </a>
                                              </div>`;
            });
          }
        },
        error: function (error) {
          console.log(error);
        },
      });
    }

    var bottom_margin = 100;

    $(window).scroll(function () {
      if ($(window).scrollTop() > $(document).height() - $(window).height() - bottom_margin) {
        counter++;
        displayNextFilms(counter);
      }
    });
  });
}
