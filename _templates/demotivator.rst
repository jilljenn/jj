Demotivational posters
======================

.. raw:: html

    <style>
    .body li {
        display: inline;
        padding: 0;
    }

    .body li a {
        border: none;
    }

    .body li img {
        padding: 5px;
        border: none;
        vertical-align: middle;
    }
    </style>

{% if poster %}
.. image:: /_static/demotivators/{{ poster }}.jpg
   :alt: {{ poster }}
{% else %}
.. toctree::
   :hidden:

 {% for poster in posters %}
   {{ poster }}/index
 {% endfor %}
{% endif %}

{% for poster in posters %}
- .. image:: /_static/demotivators/{{ poster }}.jpg
     :target: /demotivators/{{ poster }}/
     :alt: {{ poster }}
     :width: 140
{% endfor %}
