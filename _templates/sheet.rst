{{ nom }} sheet music
{{ h1_nom_row }}

From the anime `{{ section }} <index.html>`_.

    :Instruments: {{ instruments }}
{% if tempo %}
    :Tempo: {{ tempo }}
{% endif %}
    :Description: {{ description }}
    :Last updated: {{ date2 }}

{% if lienrpgsoluce %}
- `Download high-quality sheet music </anime-sheet-music/rpg/{{ nom_slug }}.html>`_
{% endif %}
- `Download sheet music </anime-sheet-music/pdf/{{ nom_slug }}.html>`_
- `Get midi file </anime-sheet-music/mid/{{ nom_slug }}.html>`_

{% if youtube %}I also recorded it on YouTube (my channel name is `Xnihpsel <https://youtube.com/Xnihpsel>`_, nice to meet you):

.. youtube:: {{ youtube }}{% endif %}

Hey, don't leave that quickly, there is `plenty of anime sheet music </anime-sheet-music>`_ on this website.

Also, I am the pianist of `Trio ELM <https://youtube.com/trioelm>`_. We perform anime and game music in concerts.

.. image:: /_static/trioelm.png
   :target: https://youtube.com/trioelm

{% if related_sheets|count > 1 %}
Also from {{ section }}
{{ h2_row }}

{% for title, slug in related_sheets %}
    {% if title != nom %}
- `{{ title }} <{{ slug }}.html>`_
    {% endif %}
{% endfor %}
{% endif %}

.. raw:: html

    <script src="/_static/microajax.js"></script>
    <script>
    li = document.querySelectorAll('.body div li p');
    document.addEventListener("DOMContentLoaded", function(event) {
        {% if lienrpgsoluce %}
        new microAjax('https://jill-jenn.net/anime-sheet-music/rpg/{{ nom_slug }}.txt', function(data) {li[0].innerHTML += '<span class="badge">' + data + '</span>';});
        new microAjax('https://jill-jenn.net/anime-sheet-music/pdf/{{ nom_slug }}.txt', function(data) {li[1].innerHTML += '<span class="badge">' + data + '</span>'});
        new microAjax('https://jill-jenn.net/anime-sheet-music/mid/{{ nom_slug }}.txt', function(data) {li[2].innerHTML += '<span class="badge">' + data + '</span>';});
        {% else %}
        new microAjax('https://jill-jenn.net/anime-sheet-music/pdf/{{ nom_slug }}.txt', function(data) {li[0].innerHTML += '<span class="badge">' + data + '</span>';});
        new microAjax('https://jill-jenn.net/anime-sheet-music/mid/{{ nom_slug }}.txt', function(data) {li[1].innerHTML += '<span class="badge">' + data + '</span>';});
        {% endif %}
    });
    </script>

.. isso-comments:: en
