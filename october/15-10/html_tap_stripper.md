HTML Tag Stripper
Given a string of HTML code, remove the tags and return the plain text content.

The input string will contain only valid HTML.
HTML tags may be nested.
Remove the tags and any attributes.
For example, '<a href="#">Click here</a>' should return "Click here".

Tests:
strip_tags('<a href="#">Click here</a>') should return "Click here".
strip_tags('<p class="center">Hello <b>World</b>!</p>') should return "Hello World!".
strip_tags('<img src="cat.jpg" alt="Cat">') should return an empty string ("").
strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>') should return sectionsection.