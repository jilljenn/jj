Anime Sheet Music - {{ mode }}
======================================

Here are some game and anime sheet music I transcribed.

Sort by: `All <index.html>`_ / `Latest <latest.html>`_ / `Top <top.html>`_ / `YouTube-only <youtube.html>`_ / `Piano-only <piano.html>`_ / `Piano & Voice-only <piano-voice.html>`_

The following list {{ description }}.

.. toctree::
   :maxdepth: 1

{% for sheet in sheet_list %}
   {{ sheet.section }} - {{ sheet.nom }} <{{ sheet.section_slug }}/{{ sheet.nom_slug }}>
{% endfor %}
