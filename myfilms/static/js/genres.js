function load_more_button_on_click(genre) {
    document.getElementById("load-more-button").remove();
    var genre_ = genre;
    $(document).ready(function () {
  
      function displayNextFilms(page_num = 1, genre) {
        const films_main_container = document.getElementById("films-main");
        var url = "/load-more-films-index/genre/" + genre;
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
                                                  <a href="/films/${film.film_id}" onclick="redirectToFilm()">
                                                  <div class="film-thumb">
                                                    <img src="/${
                                                      film.film_thumb_image
                                                    }" alt="${
                  film.film_title
                }">
                                                  </div>
                                                  <div class="film-title">
                                                    ${film.film_title.toUpperCase()}
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
          displayNextFilms(counter, genre_);
        }
      });
    });
  }