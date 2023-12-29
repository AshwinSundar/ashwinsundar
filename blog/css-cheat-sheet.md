# <span class = 'definition' data-def = 'Cascading Style Sheets'>CSS</span> Cheat Sheet

## Introduction


I first learned <span class = 'definition' data-def = 'Cascading Style Sheets'>CSS</span> at least ten years ago. Since then, I have acquired knowledge and skills piecemeal. I recently decided to sit down and learn the best practices of the specification in 2023 from [this site](https://web.dev/learn/css/). Here are my summarized notes.

## Table of Contents

- [The Box Model](#box-model)
- [Selectors](#selectors)

## <a name = "box-model"></a>The Box Model  

- `content box`: artwork
- `padding box`: mounting board
- `border box`: frame
- `margin box`: space between each frame

```text
__________     ________border box________    _______________________
          |    |       padding box      |   |                      |
_______   | m  |  ___________________   | m |  _________________   |
       |  | a  |  |                  |  | a | |                 |  |
       |  | r  |  |                  |  | r | |                 |  |
       |  | g  |  |      |\---/|     |  | g | |                 |  |
       |  | i  |  |      | o_o |     |  | i | |                 |  |
       |  | n  |  |       \_^_/      |  | n | |                 |  |
       |  |    |  |                  |  |   | |                 |  |
       |  | b  |  |    content box   |  | b | |                 |  |
       |  | o  |  |                  |  | o | |                 |  |
       |  | x  |  |                  |  | x | |                 |  |
_______|  |    |  |__________________|  |   | |_________________|  |
          |    |                        |   |                      |
__________|    |________________________|   |______________________|
```

## <a name = "selectors"></a>Selectors

- `selector` - what element is being styled
 
- `declaration` - a property-value combination
- `property` - what is being configured
- `value` - the configuration

```css
                    .my-css-rule {
                        __________________
      Declaration -->  | background: red; |
                        ------------------
                         ________   ________
          Property -->  | color: | | beige; | <-- Value
                         --------   --------
                        font-size: 1.2rem;
                    }

```

### Types of Selectors

#### Universal selector

- matches all HTML elements and applies the styles

```css
    * {
        color: green;
    }
```

#### Type selector

- matches an HTML element directly and applies the styles

```html
    <section>...</section>
```

```css
    section {
        padding: 2em;
    }
```

#### Class selector

- matches any element containing `my-class` and applies the styles

```html
    <div class = "my-class">...</div>
```

```css
    .my-class {
        color: red;
    }
```

#### Id selector

-  matches any element with `id = my-id` and applies the styles

```html
    <div id = "my-id">...</div>
```

```css
    #my-id {
        border: 1px solid blue;
    }
```

#### Attribute selector

- matches any element with `{attr} = {value}` and applies the styles

```html
    <div data-type = "primary">...</div>
```

```css
    [data-type = 'primary'] {
        color: red;
    }

    /* matches any element with the data-type attribute, regardless of value */
    [data-type] { 
        background-color: yellow; 
    }
```

#### group selector

- matches multiple elements at once

```html
    <div class = "first">This is important</div>
    <div class = "second">So is this</div>
    <div class = "third">And this</div>
```

```css
    .first,
    .second,
    .third {
        font-size: 2em
    }
```

### Complex Selectors

- composed of multiple selectors and a combinator, which describes the relationship between selectors
  - `{a} {combinator} {b}`

#### Descendant selector

- selects all descendants of `a` that match selector `b` and applies styles to `b`
- combinator is a ` ` (single-space)
- may be applied recursively

```html
    <div>
        <p>This is styled by a descendant selector
            <p>So is this</p>
        </p>
    </div>
```

```css
Descendant combinator
   |
   |
   v
div p {
    color: blue;
}
```

#### Child selector

- selects direct children of `a` that match selector `b` and applies styles to `b`
- combinator is `>`

```html
    <div>
        <span>This span is styled</span>
        <section>
            <span>This one is not, because it's not a direct child of a div</span>
        </section>
    </div>
```

```css
Child combinator
    |
    |
    v
div > span {
    font-size: 2em;
}
```

#### Next-sibling selector

- selects the next element immediately following `a` that matches selector `b` and applies styles to `b`
- combinator is `+`

```html
<p>This is a paragraph</p>
<span>This span is styled by a next-sibling selector</span>
<span>This one isn't</span>
```

```css
Next-sibling combinator
  |
  |
  v
p + span {
    color: red;
    font-weight: bold;
}
```

#### Subsequent-sibling selector

- selects any siblings following `a` and matches selector `b` and applies styles to `b`
- combinator is `~`

```html
<div>
    <p>This paragraph is styled by a subsequent-sibling selector</p>
    <span>I'm not styled</span>
    <p>But I am</p>
</div>
```

```css
Subsequent-sibling combinator
    |
    | 
    v
div ~ p {
    color: green;
}
```

#### Compound selectors

- selectors can be combined

```html
<a class = "my-class">...</a>
```

```css
a.my-class {
    color: red;
}
```