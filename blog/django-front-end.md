# Django Front-End

"Front-end" in web development refers to the visual appearance of an application or website. In Django, a web development framework, the front-end is created in DTL (Django Template Language), which is a superset of HTML (Hypertext Markup Language).

<span class = "definition" data-def = "Django Template Language">DTL</span> represents the "what" of the page - the actual contents. The "how" of the page - how the page appears - is defined by CSS (Cascading Style Sheets).  

## <span class = "definition" data-def = "Django Template Language">DTL</span> Files

Here's an example of of a <span class = "definition" data-def = "Django Template Language">DTL</span> file and its corresponding <span class = "definition" data-def = "Cascading Style Sheets">CSS</span> file:


### stats-pane.html

```djangotemplate
{% load static %} <link rel = "stylesheet" href = "{% static 'css/stats-pane.css' %}">
<div class = "stats-pane">
    <div class = "stat-component-A">
        {% include "components/stat-component.html" with title="Cages" numdetail=stats.cage_count %}
    </div>
    <div class = "stat-component-B">
        {% include "components/stat-component.html" with title="Mice" numdetail=stats.mice_count %}
    </div>
    <div class = "stat-component-C">
        {% include "components/stat-component.html" with title="Efficiency Index" numdetail=stats.efficiency green=9 yellow=4 red=0 %}
    </div>
</div>
```

Here is what is happening in this file:  

- The file loads a <span class = "definition" data-def = "Cascading Style Sheets">CSS</span> stylesheet called `stats-pane.css`
- The file defines a framework for containing three components - `stat-component-A`, `stat-component-B`, and `stat-component-C`  
- Each `div.stat-component` includes a template file called `stat-component.html`
  - Information is passed to these templates using the `with` keyword  
  
### stat-component.html 

Here are the contents of the `stat-component.html` file:

```djangotemplate
{% extends "components/generic-square.html" %}
{% block content %}
    {% load static %} <link rel = "stylesheet" href = "{% static 'css/components/stat-component.css' %}">
    <div class = "stat-container">
        <div class = "stat-title">
            {{ title }}
        </div>
        {% if numdetail > green %}
        <div class = "stat-numdetail stat-green">
        {% elif numdetail > yellow %}
        <div class = "stat-numdetail stat-yellow">
        {% elif numdetail > red %}
        <div class = "stat-numdetail stat-red">
        {% else %}
        <div class = "stat-numdetail">
        {% endif %}
            {{ numdetail }}
        </div>
    </div>
{% endblock content %}
```

- The file `extends` an existing template called `generic-square.html`. This means that some pre-existing content has been defined in the `generic-square.html` template, and this file will override some of the content.
- The file loads a <span class = "definition" data-def = "Cascading Style Sheets">CSS</span> stylesheet called `stat-component.css`.
- `{% block content %}` represents the start of the overrideable section. All content from here until `{% endblock content %}` will override the section in the `generic-square.html` file of the same name [^dtl-extends].
- The file defines a framework for containing a single statistic - `stat-title` and multiple `stat-numdetail` components, each wrapped in conditional logic.
  - Conditional logic determines whether particular styles shall be rendered. For example, if the `numdetail` variable is greater than the `green` variable, the statistic shall be displayed with the class `stat-green`. This class merely colors the text of the component in green.

## <span class = "definition" data-def = "Cascading Style Sheets">CSS</span> Files

<span class = "definition" data-def = "Cascading Style Sheets">CSS</span> describes how the elements of the page appear. Here is the <span class = "definition" data-def = "Cascading Style Sheets">CSS</span> file used by the `stats-pane.html` file described in the first section:

### stats-pane.css

```css
.stats-pane {
  display: flex;
  flex-direction: row;
  gap: 10px;
  justify-content: center;
  align-items: center;
}
```

- The text before the `{}`, `.stats-pane`, is called an element selector. We know this element selector applies to classes because the statement begins with a `.`. If this applied to a different selector, such as `id`, it would begin with a different character.

This definition applies styling characteristics to elements that have an attribute of `class = "stats-pane"`. In this case, the stats-pane is defined as a layout style called `flexbox`[^flexbox], and the elements of the flexbox should appear as rows. The gap between each element is set to 10 pixels, and finally the contents are center-aligned.

## Conclusion  

- The <span class = "definition" data-def = "Django Template Language">DTL</span> represents the "what" of the page
  - What are the structural elements (i.e. HTML elements)?
  - What is the basic logic for the page (i.e. embedded scripting)?

- CSS defines the "how" of the page:
  - How are elements rendered (i.e. styles)?
  - How do those elements appear on the page (i.e. animations, transitions)?

While <span class = "definition" data-def = "Django Template Language">DTL</span> contains some Python-esque language features, it only permits a small subset of the Python language to be run. This is a design choice - permitting arbitrary Python code to run can be dangerous. That said, DTL is fairly powerful and extensible via custom filters and tags[^custom-tags]. 

<span class = "definition" data-def = "Cascading Style Sheets">CSS</span> takes some time to become acquainted with and ultimately master. The core specification is constantly improving. [This guide](https://web.dev/learn/css) is a good way to understand the modern contours and best-practices of <span class = "definition" data-def = "Cascading Style Sheets">CSS</span> in 2023.


[^dtl-extends]: Template extensions are part of a larger Django topic called [template inheritance](https://docs.djangoproject.com/en/5.0/ref/templates/language/#id1)  

[^flexbox]: https://css-tricks.com/snippets/css/a-guide-to-flexbox/

[^custom-tags]: https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/