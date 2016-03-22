## Logistics, Project 1, and Text Editors

### Forums vs. Google+
We encourage you to use our discussion forums10 to share anything that you'd like to about the Nanodegree program, your journey to learning how to program, and more. Join us!

### Project 1
We've noticed a few recurring issues that we'd like to point out here and discuss, so let's get started!

### Correctly nesting and closing tags

It's important to ensure that HTML tags are nested correctly. This means that everything that starts inside a given tag must end before its outer tag ends. Here's an example where that isn't the case:

<strong><a href="https://www.udacity.com">This site rocks!</strong></a>
Here, we start bolding text and start a link, but we stop bolding text before we end the link. This is what we should do instead:

<strong><a href="https://www.udacity.com">This site rocks!</a></strong>
And, here's an example of us forgetting to close some tags, which is also a good opportunity for us to show you how to create a list. A list is a standard element in HTML -- you can create an ordered (numbered) list with ol and a bulleted list with ul. These tags start a list, and, once you're in a list, it's up to you to create items in your list with li, as you can see below:

<ol>
  <li>Apples
  <li>Bananas
  <li>Mandarins
</ol>
We forgot to close each of our list items, so let's fill them in:

<ol>
  <li>Apples</li>
  <li>Bananas</li>
  <li>Mandarins</li>
</ol>
Curiously, both of these examples look the same if you compare the incorrect and correct versions in a browser (or in CodePen1). So, why should we bother to make sure our code is correct? What does it even mean for code to be correct?

One way to assess correctness is by using a validator.

HTML is similar to English in this way: even though native English speakers are often able to understand grammatically incorrect English, it's still worth trying to follow the rules as closely as we can.

Browsers are very good at putting together something reasonable when given malformed HTML, but we, as programmers, shouldn't take that for granted. Just because your page looks fine to us in Chrome or Safari or IE doesn't mean that it looks good everywhere. People communicate with webpages in many different ways -- through mobile apps, technology that allows handicapped people to interact with the Internet, and much, much more. Making the Internet work for all of us requires us to be mindful of that!

Correctly spelling tags

Instead of giving you an indication that you've made a mistake, misspelling a tag will either not change anything or make the text on your webpage look "unstyled."

For instance, if you misspell the p tag by calling it paragraph instead, paragraphs don't come with a predefined style, so your page will probably look exactly the same either way (assuming you aren't yourself defining a style for
the p element.).

If, instead, you try to insert a header into your page with h1 but accidentally call it h12, the text inside an h12 tag won't look very header-like because h12 isn't a real header tag.

b vs. strong (semantics vs. style)

Best practices today dictate that HTML tags should be used more for semantics (the meaning of your content) rather than the style of your content (is this bold?). The b tag is a "style" tag whereas the strong tag is a "semantic" tag that means that you want to emphasize the content inside that tag. It just so happens that the standard way to style that is by bolding it.

This goes the other way too. We've seen some students use the blockquote element in attempts to indent text in a certain way, especially since any spaces after the first space do not matter in HTML. It turns out that blockquote should only be used in cases where something is being quoted (i.e. a novel or movie).

Showing HTML inside a webpage

The less than sign (<) and greater than signs (>) are special characters in HTML because they're what we use to denote tags. How do we insert them as text into our page so that they show up? We have to use a special sequence of characters to get them to show up.

&lt; will show up as < and &gt; will show up as >.

Putting head elements inside the body

We've seen a few instances of the title element ending up in the body instead of the head. This element corresponds to what shows up in a browser's tab when someone visits your site rather than something on your page, which is why it should go into the head rather than the body.

Getting images to show up

It's important to make sure that img tags point to locations that the thing that is displaying our page has access to. It's perfectly fine to point to images on your computer when you are working on your site on your computer, but those images don't exist (yet) on the Internet, so once you try to put your site on CodePen1, you have to put your images in places that it can access.

One easy way to do this is to upload your images to a site on the Internet called imgur47. Once you upload an image there, it will give you a direct link to the image, which you can use in the src attribute instead of the path
to a file on your own computer.

Old:

<img src="/Users/Chrisna/Downloads/awesome.jpg" alt="An awesome picture">
New:

<img src="http://chrisna.org/images/night-over-new-york.jpg" alt="An awesome picture">
Text Editors
Sublime Text14 is pretty cool! A working setup we like involves the following steps to transition from CodePen1:

Copy HTML into an empty tab in Sublime Text. Save the HTML file somewhere.
Open a new tab in Sublime Text and copy CSS into it, if you have any. Save that file in the same folder as the HTML file and remember its name.
Ensure that a link element exists in the head of the HTML file that points to any CSS files that you have: <link rel="stylesheet" href="main.css">
Open HTML file in your favorite browser.
You'll have to refresh your browser and save your HTML and CSS file periodically, but other than that, it's a pretty nice way to get some programming done!


## CSS Summary and Reference
There was a lot of information in the previous video and you don't need to remember it all. This is a text summary. Quickly skim through it (just look at the headings so you know what's here) and come back when you need to.

### What is CSS?

CSS is code written to control the "style" of HTML elements.

### How does CSS "control" HTML?

If you want to write CSS that makes all h1 elements have a black background and white text, you would write:

h1 {
  background-color : black;
  color: white;
}
In this example, the h1 is a selector. It says to the browser "I want you to apply the rules I'm about to tell you to every h1 element."

After the h1 there is a left curly brace { and at the bottom there is a matching right curly brace }. Everything between these curly braces will be interpreted as a "rule" that should be applied to every h1 element.

The line of code that says background-color : black; is a declaration. background-color is a property and black is the value of that property.

### CSS Vocabulary

CSS: Cascading Style Sheets.

Style: This word can refer to many things and so it can be confusing. It can refer to:

The HTML element. For example: <style>div {color:blue}</style>

The HTML attribute. For example: <div style="color : blue">this text would be blue</div>

The general look of a web page. For example: "I like that site's style."

A verb. For example: "I'm making progress on my page. The structure is all done but now I have to style it."
Rule: a line of CSS code describing the value that a certain attribute should take.

Property: The property you want to change.

Value: The value that you want to assign to the attribute.

Selector: The name that you use to in order to target the elements that are assigned to a class or id attribute in the HTML.

Class: A class refers to a group of elements that can be styled together. Class names should not contain periods or any other punctuation marks such as class="1.1"

ID: ID's are unique identifiers that uniquely identifies an element in HTML.

### Selecting by class

In the example above, we set the background-color of every h1 to black. If we only want to add style to certain h1s, we can use class selectors. Try copying the following code into scratchpad.io to see how this works.

<div class="stop"></div>
<div class="slow"></div>
<div class="go"></div>

<style>
  div {
    height : 50px;
    width : 50px;
    border-radius: 25px;
  }
  .stop {
    background-color: red;
  }
  .slow {
    background-color: yellow;
  }
  .go {
    background-color: green;
  }
</style>
We should see a traffic light. Note how in the <style> element we refer to an HTML element's class name by writing .class-name

Also note how we can apply rules to all divs or just certain divs by using the appropriate selector.

How do I include CSS Styling in my web page?

There are three ways you can do this.

Method 1: write CSS in the <head> of your HTML

This method is good for very small projects (like what you'd do in scratchpad.io). To do this: 1. At the top of your HTML document, add a <head> element. 2. Inside the <head> element, add a <style> element. 3. Write your CSS in the <style> element and then put the HTML for the rest of your page below.

For example:

<head>
  <style>
    div {
      background-color : red;
    }
  </style>
</head>
<body>
  <div>
    This will have a red background.
  </div>
</body>
Method 2: Link your HTML to a separate CSS file

This adds another step, but it lets you stay more organized when working on larger projects. To do this: 1. Write all of your structural HTML in one file (let's call it main.html). 2. In a separate file (let's call it main.css), put all of your CSS code. 3. Add a <head> element to the top of your HTML. 4. Add a <link> tag inside the <head> element. Since <link> is a "void tag" you don't need to add a closing </link>. 5. Add the following attributes to your <link>: * rel="stylesheet" * href="main.css"

For example, you would have a main.html file that looked like this:

<head>
   <link rel="stylesheet" href="main.css">
</head>
<body>
  <div>
    This will have a red background.
  </div>
</body>
and in the same folder you would have a file called main.css like this:

div {
  background-color : red;
}
Method 3: Write your style inline with your HTML

This is generally a very bad idea because it leads to lots of repeated code. But you may see code that uses this method so it's good to be familiar with it. If you want to know more, check out the question and answers in this conversation on Stack Overflow (Stack Overflow is the most widely used programming Q&A community out there).

With this method, you modify the style attributes of every individual HTML element. For example:

<body>
  <div style="background-color: red; color: white">
    This div will have a red background and white text.
  </div>
  <div style="background-color: red; color: white">
    So will this one.
  </div>
  <div style="background-color: red; color: white">
    Now, what if I change my mind?
  </div>
  <div style="background-color: red; color: white">
    I'd rather have a black background...
  </div>
  <div style="background-color: red; color: white">
    Never do this!
  </div>
</body>.

NOTE: there are a lot of little mistakes you can and will at some point make that will cause any of these methods not to work. For example, when I was writing the code for method 2 I had main.html and main.css in different folders on my computer, and it didn't work at all.
