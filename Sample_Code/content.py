# COURSE 2 / COURSE 4:
# This is a complex data structure which consists of
# lists and dictionaries (you learn about those in Course 4). But
# this list allows us to keep all of our content in one place.
# We then inject this content into the HTML templates (you'll learn
# about them in Course 4).

# COURSE 2:
# When you start writing your own functions to automatically
# generate HTML, you are actually writing a simple version of
# an HTML templating engine.
from google.appengine.ext import ndb

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'
COURSES = [
	{"title"    : "Webpages, Documents, and Structure",
		"description" : ("This was my introduction to the world of coding. "
										 "I wrote some simple HTML and CSS to make static web "
										 "pages. I was first introduced to the principle of "
										 "'Don't Repeat Yourself' in this course when I started "
										 "using HTML classes and CSS styling to make similar HTML "
										 "elements look the same."),
		"url" : "https://www.udacity.com/course/viewer#!/c-ud721-nd/",
		"favorite_video": {
			"title"   : "Interview with Jacques",
			"url"     : "https://www.youtube.com/embed/Nj5RCaE_b00",
			"caption" : "Jacques, A professional front-end web developer, explains how he 'boxifies' designs."
		},
		"lessons" : [
			{
			"title"     : "The Basics of the Web and HTML",
			"description"  : "The internet is a bunch of computers communicating over HTTP",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud721-nd/l-3508959201",
			"concepts" : [
					{	"title" 			: "HTML",
					 	"description" : "HyperText Markup Language"},
					{	"title" 			: "Elements",
						"description" : "HTML documents are made up of HTML 'elements'."
					}
				]
			},
			{
			"title"			: "Creating a Structured Document with HTML",
			"description"   : "How elements within elements creates a structured 'box-like' model of a web page.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud721-nd/l-3555039510",
			"concepts"  : [
					{ "title"				: "Divs and Spans",
						"description" : "These are the two 'container' elements that can be used to build the structure of a web page."},
					{ "title"				: "Box Model",
						"description" : "Everything on the web is boxes!"
					}
				]
			},
			{
			"title"			: "Adding CSS Style to HTML Structure",
			"description"   : "By giving similar HTML elements the same 'class', we can write all the styling for that class just ONCE and it will apply to every element. ",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud721-nd/l-3575138706",
			"concepts"  : [
					{ "title"				: "Style",
						"description" : "The 'style' of an HTML element is just a bunch of rules which describe how that element should look. This style can be specified in a CSS file."},
					{ "title"				: "Avoiding Repetition",
						"description" : "It's good to avoid repetition when programming. If you give the same style to similar elements, you can reap the benefits of this when you quickly and easily modify all of them at once just by changing a single line of CSS."
					}
				]
			}
		]
	},
	{ "title"    : "Telling Computers what to do",
		"description" : ("I learned the programming basics: variables, functions "
										 "various data types (strings, numbers, lists...), etc... "
										 "This course was definitely hard and I still don't feel "
										 "like an expert in solving problems with Python, but I "
										 "can at least read and reuse other people's code if I want to. "),
		"url" : "https://www.udacity.com/course/viewer#!/c-ud552-nd",
		"favorite_video": {
			"title"   : "Making vs Using Functions",
			"url"     : "https://www.youtube.com/embed/JJBo7mfgoTs",
			"caption" : "A review of Python functions as well as a good explanation of the difference between making and using functions."
		},
		"lessons" : [
			{
			"title"     : "Introduction to Serious Programming",
			"description"  : "Answers questions like: What's a program? What's a computer? What's a programming language?",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3527838955",
			"concepts" : [
					{	"title" 			: "Computer",
					 	"description" : "A computer is a machine that can carry out instructions given to it by a programmer."},
					{	"title" 			: "Grammar",
						"description" : "Grammar refers to the rules that govern what statements are 'legal' in a language. Python has it's own grammar."
					}
				]
			},
			{
			"title"			: "Variables and Strings",
			"description"   : "We can store textual information (strings) in titled containers (variables)",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3574398630",
			"concepts"  : [
					{ "title"				: "Variable",
						"description" : "A variable is a titled container that holds information. "},
					{ "title"				: "String",
						"description" : "A string is just text. We create strings by using single or double quotes."
					}
				]
			},
			{
			"title"			: "Input --> Function --> Output",
			"description"   : "A function is something that takes input, does something with that input, and then returns something else as output.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3574398630",
			"concepts"  : [
					{ "title"				: "Defining Functions",
						"description" : "In Python, functions are defined by writing the 'def' keyword followed by a name, and then the 'parameters' for the function (inside parentheses), and a colon."},
					{ "title"				: "return vs print",
						"description" : "When functions don't have a 'return' statement, they don't really do anything (even though they may print out some text). You usually want to make sure to end your function with a return statement."
					}
				]
			},
			{
			"title"			: "Decisions and Repetition - If and While",
			"description"   : "Control flow statements (like 'if' and 'else') let us execute different blocks of code depending on some condition. While loops let us repeat a certain block of code many times until a certain condition is met.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3574398630",
			"concepts"  : [
					{ "title"				: "==, !=, >, <, >=, <=",
						"description" : 'These are all Python "comparison operators". They return the "boolean" True when they are correct and False when they are not. For example, 5 != 6 would return True, since 5 is not equal to 6.'},
					{ "title"				: "if, then, else",
						"description" : "These three Python keywords let us tell Python what code we want it to execute in different situations."},
					{ "title"				: "while loops",
						"description" : "A while loop will repeat the indented block of code beneath it as long as the condition on the first line (right after 'while') is true."
					}
				]
			},
			{
			"title"			: "How to Solve Problems",
			"description"   : ("The first step in solving large problems is to understand the problem. We do this by "
				"1) understanding the inputs. 2) understanding the outputs. And 3) writing a function to correctly produce the desired output from the input."),
			"url" : "https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3486769621/m-108325372",
			"concepts"  : [
					{ "title"				: "Understanding Inputs",
						"description" : ("This requires figuring out what inputs your function will be responsible for processing "
						"In the example problem, the inputs were 6 numbers which are used to encode two dates. We also assumed "
						"that the second date would always be after the first.")},
					{ "title"				: "Understanding Outputs",
						"description" : ("This requires figuring out exactly what output your function is responsible for providing. "
						"In the example problem, the output was a single number which represented the number of days between two dates.")
					}
				]
			}
		]
	},
	{ "title"    : "The Power of Abstraction",
		"description" : ("This course taught me how to avoid repetition "
										 "in my code by defining 'Classes' of 'Objects' with "
										 "similar properties. This 'Object-Oriented' style of "
										 "programming also lets me think about programs in a "
										 "way that I'm familiar with"),
		"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd",
		"favorite_video": {
			"title"   : "Vocabulary Recap",
			"url"     : "https://www.youtube.com/embed/11G5sBkY9tQ",
			"caption" : "A review of important vocabulary from the course like class, instance, constructor, instance variables, instance methods, and self."
		},
		"lessons" : [
			{
			"title"     : "Use Functions",
			"description"  : "A review of functions in Python.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd/l-3579538661",
			"concepts" : [
					{	"title" 			: "Computer",
					 	"description" : "A computer is a machine that can carry out instructions given to it by a programmer."},
					{	"title" 			: "Grammar",
						"description" : "Grammar refers to the rules that govern what statements are 'legal' in a language. Python has it's own grammar."
					}
				]
			},
			{
			"title"			: "Use Classes - Draw Turtles",
			"description"   : "Learn how to use Python 'classes' which other programmers have already written.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd/l-3525629753",
			"concepts"  : [
					{ "title"				: "Variable",
						"description" : "A variable is a titled container that holds information. "},
					{ "title"				: "String",
						"description" : "A string is just text. We create strings by using single or double quotes."
					}
				]
			},
			{
			"title"			: "Use Classes - Send Text",
			"description"   : "Use 'Twillio' to send text messages to people with code!",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd/l-3524089779",
			"concepts"  : [
					{ "title"				: "External Libraries",
						"description" : "An 'external library' is just a library that someone has written that does not come packaged with Python (Twillio is an example)."},
					{ "title"				: "from __ import __",
						"description" : "When you write something like 'from twillio.rest import TwilioRestClient', you gain access to TwilioRestClient without having to import all the extra stuff that is in twillio.rest."
					}
				]
			},
			{
			"title"			: "Use Classes - Profanity Editor",
			"description"   : "Learn about how to work with files while making a profanity editor.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd/l-3486659368",
			"concepts"  : [
					{ "title"				: "Reading Documentation",
						"description" : "Since there are SO many tools out there for programmers to use, a big part of programming is finding and learning how to use the right ones. Reading the documentation for the tools you use is VERY important."},
					{ "title"				: "Built-in Functions",
						"description" : "Python has a lot of built-in functions. These functions usually do something that is widely useful to many people. My favorite built-in function is 'enumerate'."
					}
				]
			},
			{
			"title"			: "Make Classes - Movie Website",
			"description"   : "Learn how to make your own Python 'classes' and build a website that displays movie information.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd/l-3567738950/",
			"concepts"  : [
					{ "title"				: "Class vs Instance",
						"description" : "A 'Class' is like a blueprint for a building while an 'instance' is like an ACTUAL building that was made from the blueprint."},
					{ "title"				: "Instance Methods",
						"description" : "Instance methods are special functions that belong to an 'instance' of a 'class.' They usually get or set information about the instance they are attached to."
					}
				]
			},
			{
			"title"			: "Make Classes - Advanced Topics",
			"description"   : "Learn about topics like Class methods, Inheritance, and Method Overriding.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd/l-3572248644",
			"concepts"  : [
					{ "title"				: "Inheritance",
						"description" : "When you use inheritance, you figure out what seemingly different things have in common and then capture that commonality in a 'parent' class."},
					{ "title"				: "Inheritance Example",
						"description" : "In this lesson, we realized that instances of the TvShow class have a lot in common with instances of the Movie class. We put the common elements into a new Video class and had Movie and TvShow inherit from Video."
					}
				]
			}
		]
	},
	{ "title"    : "The Full Stack",
		"description" : ("This course taught me how to actually make a web page! "
										 "I learned about and wrote 'server-side' code and used "
										 "Google AppEngine to host my page."),
		"url" : "https://www.udacity.com/course/viewer#!/c-ud645-nd",
		"favorite_video": {
			"title"   : "Handling HTML Input",
			"url"     : "https://www.youtube.com/embed/K37Ldm4GSPo",
			"caption" : "A great explanation of why it's so important to properly handle user input (and the bad things that could happen if we don't)."
		},
		"lessons" : [
			{
			"title"     : "Introduction to Networks",
			"description"  : "Networks (like the internet) are made of a bunch of links between 'nodes'. Information can be sent on a network by passing it from node to node until it reaches its destination.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud744-nd/l-3550189560",
			"concepts" : [
					{	"title" 			: "Computer",
					 	"description" : "A computer is a machine that can carry out instructions given to it by a programmer."},
					{	"title" 			: "Grammar",
						"description" : "Grammar refers to the rules that govern what statements are 'legal' in a language. Python has it's own grammar."
					}
				]
			},
			{
			"title"			: "Make the Internet Work for You",
			"description"   : "When you type a URL into your browser and hit Enter, a 'request' gets sent to a server. The server handles that request and sends back a 'response'.",
			"url" : "https://www.udacity.com/course/viewer#!/c-ud744-nd/l-3494188878",
			"concepts"  : [
					{ "title"				: "Variable",
						"description" : "A variable is a titled container that holds information. "},
					{ "title"				: "String",
						"description" : "A string is just text. We create strings by using single or double quotes."
					}
				]
			}
		]
	}
	]
CODE_PENS = [
{'title': 'Project Examples',
 'description': """Examples of what your project may look like at various stages of the Nanodegree.""",
 'examples' : [
 	{
	'title':'Stage 0',
	'description':'HTML with <b>, <p>, and <em> tags.',
	'level': 'beginner',
	'code_pen_id':'ByVLVX',
	'user_name':'AndyAtUdacity',
	'votes':0
	},
	{
	'title':'Stage 1 Work Session 2',
	'description':'Structured HTML (no CSS).',
	'level': 'beginner',
	'code_pen_id':'LEjWaj',
	'user_name':'AndyAtUdacity',
	'votes':0
	},
	{
	'title':'Stage 1 Complete',
	'description':'Structured HTML with CSS styling.',
	'level': 'beginner',
	'code_pen_id':'KweNKa',
	'user_name':'AndyAtUdacity',
	'votes':0
	},
 ]
},
{'title': 'HTML and CSS Core Concepts',
 'description': """Demonstrations of various HTML and CSS concepts covered in Nanodegree courses.""",
 'examples' : [
 	{
	'title':'Inline vs Block Demo',
	'description':'A demonstration of various HTML elements to determine which are block-level and which are inline.',
	'level': 'beginner',
	'code_pen_id':'LEqLNz',
	'user_name':'AndyAtUdacity',
	'votes':0
},
{
	'title':'<span> vs <div> Demo',
	'description':'An example showing the difference between spans and divs and what it means to "nest" elements.',
	'level': 'beginner',
	'code_pen_id':'LEqLje',
	'user_name':'AndyAtUdacity',
	'votes':0
	},
	{
	'title':'Using Classes to Style Elements',
	'description':'Simple traffic light demonstrates how to use classes to style certain elements.',
	'level': 'beginner',
	'code_pen_id':'OPdjXy',
	'user_name':'AndyAtUdacity',
	'votes':0
	},
	{
	'title':'Multiple Classes on one Element',
	'description':'More sophisticated traffic light example shows how to give a single element multiple classes.',
	'level': 'intermediate',
	'code_pen_id':'RNvZRX',
	'user_name':'AndyAtUdacity',
	'votes':0
	},
	{
	'title':'Making Reusable CSS Classes',
	'description':'Demonstrates how to create reusable CSS classes (comes from Codepen user mandybee).',
	'level': 'intermediate',
	'code_pen_id':'EapyqV',
	'user_name':'mandybee',
	'votes':0
	},
 ]
},
{'title': 'Additional Topics',
 'description': """JavaScript, Advanced HTML / CSS, and anything else.""",
 'examples' : [
 	{
	'title':'JavaScript Clickable Traffic Light',
	'description':'Demonstrates some simple JavaScript.',
	'level': 'intermediate',
	'code_pen_id':'MYxWjY',
	'user_name':'AndyAtUdacity',
	'votes':0
	},
 	{
	'title':'Making Shapes with CSS',
	'description':'Shows how to make various shapes through clever use of borders and rotations.',
	'level': 'intermediate',
	'code_pen_id':'vEbWBp',
	'user_name':'AndyAtUdacity',
	'votes':0
	},
	{
	'title':'Nested Rows and Columns',
	'description':'Shows behavior of nested rows and columns.',
	'level': 'intermediate',
	'code_pen_id':'LEqJaw',
	'user_name':'AndyAtUdacity',
	'votes':0
	},
	{
	'title':'Scratchpad vs. Codepen vs. Sublime',
	'description':'A table that breaks down the pros and cons of these three tools.',
	'level': 'beginner',
	'code_pen_id':'azYrBM',
	'user_name':'AndyAtUdacity',
	'votes':0
	},
	{
	'title':'Drawing with CSS',
	'description':'Warning: you will spend hours tweaking attribute values if you go down this road.',
	'level': 'intermediate',
	'code_pen_id':'GgzVrK',
	'user_name':'AndyAtUdacity',
	'votes':0
	},
	{
	'title':'RGB Playground',
	'description':'Shows how different amounts of red, green, and blue can create colors.',
	'level': 'intermediate',
	'code_pen_id':'wBOBrG',
	'user_name':'AndyAtUdacity',
	'votes':0
	},
]
},
]
TOPICS = [
	{"title" : "HTML Resources",
	"description" : ("Learn more about HTML elements, tags, attributes, and forms"),
	"resources" : [
		{
		"title" : "HTML Elements, Tags, and Attributes",
		"url" : "https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Introduction#Elements_.E2.80.94_the_basic_building_blocks",
		"description" : ("The Mozilla Developer Network (aka MDN, and a good resource in general), "
						 "explains key HTML vocabulary. ")
		},
		{
		"title" : "HTML Forms",
		"url" : "https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms/My_first_HTML_form",
		"description" : ("Forms are one way users interact with your page. "
			"This is a tutorial for beginners.")
		},
		{
		"title" : "List of every HTML Element",
		"url" : "https://developer.mozilla.org/en-US/docs/Web/HTML/Element",
		"description" : ("Scan through to get a feel for all the HTML elements "
			"that exist from <a> to <video>.")
		},
		{
		"title" : "Udacity's Intro to HTML and CSS",
		"url" : "https://www.udacity.com/course/ud304",
		"description" : ("The first lesson of this Udacity course is already "
						 "in the Nanodegree, but the rest of the course does "
						 "a good job of thoroughly explaining how to make web "
						 "pages look the way you want them to.")
		}
	]
	},
	{"title" : "CSS Resources", #Positioning, Layout, Priority Rules, Selection, Inheritance
	"description" : ("Learn how to make your web page look good."),
	"resources" : [
		{
		"title" : "CSS Layout",
		"url" : "http://learnlayout.com/position.html",
		"description" : ("A good walk through of the `position` "
						 "property, including static, relative, fixed, "
						 "and absolute positioning.")
		},
		{
		"title" : "Using Multiple Selectors",
		"url" : "https://css-tricks.com/multiple-class-id-selectors/",
		"description" : ('By using "Multiple Selectors" you can apply styling '
			'only to elements which meet multiple criteria.')
		},
		{
		"title" : "Specificity Rules",
		"url" : "http://www.smashingmagazine.com/2007/07/27/css-specificity-things-you-should-know/",
		"description" : ('What happens when multiple conflicting rules apply '
			'to the same element? CSS Specificity rules are what decide which rule '
			'"wins". If you are having trouble getting rules to work, this is probably '
			'the resource you need.')
		},
		{
		"title" : "Flexbox Explanation",
		"url" : "https://css-tricks.com/snippets/css/a-guide-to-flexbox/",
		"description" : ("Flexbox is a flexible box! It gives you "
						 "a way to have your HTML elements easily adjust "
						 "their size based on the size of the page.")
		},
		{
		"title" : "Bootstrap",
		"url" : "http://getbootstrap.com/getting-started/#examples",
		"description" : ('Bootstrap is a popular CSS "framework" which provides you with '
			'pre-written CSS to make your page look good.')
		},
		{
		"title" : "Color Palette Examples",
		"url" : "http://www.dtelepathy.com/blog/inspiration/beautiful-color-palettes-for-your-next-web-project",
		"description" : ("It's hard to find colors that look good together. "
			"This is a list of 50 color palettes.")
		}
	]
	},
	{"title" : "Accessibility",
	"description" : ("At its core, the internet is about connecting people. Practice accessible design to ensure that all users of your site have the best experience."),
	"resources" : [
		{
		"title" : "The alt Attribute",
		"url" : "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-alt",
		"description" : ('Blind people use the web too! And when they do, they often use "screen readers" '
			'which read the text of your page to them. When your visual content (like <img> or <video> elements) '
			"has an alt tag these screen readers will read the descriptive text that you've added.")
		},
		{
		"title" : "Accessibility Best Practices",
		"url" : "http://accessibility.arl.org/standards-best-practices/#technical-standards",
		"description" : ('A list of 12 easy-to-implement accessibile design guidelines.')
		}
	]
	},
	{"title" : "Python Resources",
	"description" : ("Get more Python practice and read more about important Python "
		"concepts."),
	"resources" : [
		{
		"title" : "29 Common Beginner Python Errors",
		"url" : "http://pythonforbiologists.com/index.php/29-common-beginner-python-errors-on-one-page/",
		"description" : ("A super-helpful flowchart for when your code isn't working.")
		},
		{
		"title" : "Learn Python the Hard Way",
		"url" : "http://learnpythonthehardway.org/book/",
		"description" : ("A free online book by Zed Shaw. It's written "
						 "for novice programmers looking to learn Python. It's "
						 "organized by topic and has very good explanations and example "
						 "code throughout. Each section ends with helpful 'Study Drills.'")
		},
		{
		"title" : "Project Euler",
		"url" : "https://projecteuler.net/",
		"description" : ("This site provides a lot of highly mathematical "
						 "problems which can be solved with programming. It's a "
						 "good place for building your 'Procedural Thinking'.")
		},
		{
		"title" : "More Resources from python.org",
		"url" : "https://wiki.python.org/moin/ProblemSets",
		"description" : ("The organization that manages the Python language also "
						 "maintains a list of practice resources as well. Some are "
						 "better than others.")
		}]},
	{"title" : 'Python "Web Frameworks"',
	"description" : ("The frameworks listed here can make it easier to build large web "
		"applications by taking care of a lot of the ugly details for you."),
	"resources" : [
		{
		"title" : "Flask",
		"url" : "http://flask.pocoo.org/",
		"description" : ("The Django homepage says: \n\n"
			"Flask is a 'microframework'. It's simple to learn, easy to understand, and "
			"well-documented. It's great for small to medium sized projects.")
		},
		{
		"title" : "Django",
		"url" : "https://www.djangoproject.com/",
		"description" : ("The Django homepage says: \n\n"
			"Django is a high-level Python Web framework that encourages rapid "
			"development and clean, pragmatic design. Built by experienced developers, "
			"it takes care of much of the hassle of Web development, so you can focus on "
			"writing your app without needing to reinvent the wheel. It's free and open source.")
		},
		{
		"title" : "Flask vs. Django (Quora thread)",
		"url" : "http://www.quora.com/Should-I-learn-Flask-or-Django",
		"description" : ("Flask and Django are both very popular. This thread has "
			"some great discussion about the pros and cons of each. Summary: Django has more "
			"features, but Flask is easier to learn.")
		}
	]},
	{"title" : 'Cool Tools',
	"description" : ("Great tools to make you a more powerful programmer."),
	"resources" : [
		{
		"title" : "Web Developer Browser Extension",
		"url" : "http://chrispederick.com/work/web-developer/",
		"description" : ("""Chris Pederick's "Web Developer Extenstion """
			"is a tool to make web development easier. You can see the box-like "
			"structure of a page, easily disable CSS, and more.")
		},
		{
		"title" : "iPython and iPython Notebook",
		"url" : "http://ipython.org/notebook.html",
		"description" : ("Wow. These tools changed how I code. Do youself a favor: visit "
			"this page, install iPython Notebook, and make your programming life 100 times better.")
		},
		{
		"title" : "External Libraries for Python",
		"url" : "http://pythonhackers.com/top-python-projects/",
		"description" : ("A list of popular external libraries for Python ordered by votes.")
		},
		{
		"title" : "Useful Modules from Python Standard Library",
		"url" : "http://stackoverflow.com/questions/1453952/most-useful-python-modules-from-the-standard-library",
		"description" : ("A thread on stackoverflow about the most useful modules "
			"that come with Python.")
		}
	]},
	{"title" : 'Other Udacity Nanodegrees',
	"description" : ("After the Intro Programming Nanodegree, you'll "
		"be ready to take most (if not all) of Udacity's other Nanodegrees."),
	"resources" : [
		{
		"title" : "Front-End Web Developer Nanodegree",
		"url" : "https://www.udacity.com/course/nd001",
		"description" : ("Learn more about Front-end web development: responsive "
			"design, JavaScript, jQuery, and more.")
		},
		{
		"title" : "iOS Developer Nanodegree",
		"url" : "https://www.udacity.com/course/nd003",
		"description" : ("Learn to make apps for iPhone and iPad.")
		},
		{
		"title" : "Full Stack Web Developer Nanodegree",
		"url" : "https://www.udacity.com/course/nd004",
		"description" : ('Learn how to make bigger and better "full-stack" web applications.')
		}
	]}]
SECTIONS = [
	{"title"     : "Andy's Notes",
	 "image_url" : "/images/computer_notes.jpg",
	 "href"      : "nanodegree_notes/",
	 "short_title":"Notes",
	 "id"        : "notes",
	 "alt"       : "open laptop next to a paper notebook"
	},
	{"title"     : "Student Notes",
	 "image_url" : "/images/colored_papers.jpg",
	 "href"      : "student_submissions/",
	 "short_title":"Projects",
	 "id"        : "submissions",
	 "alt"			 : "stack of brightly colored folders seen from above"
	},
	{"title"     : "More Resources",
	 "image_url" : "/images/tools.jpg",
	 "href"      : "additional_resources/",
	 "short_title":"Resources",
	 "id"        : "resources",
	 "alt"			 : "various carpentry tools neatly arranged on white background"
	},
	{"title"     : "Codepen Examples",
	 "image_url" : "/images/pen.jpg",
	 "href"      : "code_pen_examples/",
	 "short_title":"Codepens",
	 "id"        : "codepen",
	 "alt"			 : "closeup of fountain pen on paper"
	}]

def get_application_id(url):
	begin_app_id = url.find('http://') + 7
	end_app_id = url.find('.appspot.com')
	return url[begin_app_id : end_app_id]

def is_submission_valid(student_name, description, url):
	if len(student_name) < 2:
		# Not a valid name if there's less than 2 letters
		return False

	if len(description) < 20:
		# Description should be at least 20 letters
		return False

	if len(description) > 250:
		# Description shouldn't be too long
		return False

	if url.find('.appspot.com') == -1:
		# All submissions should be hosted on appspot.com
		return False

	# If none of the previous return statements have been triggered
	# than this is a valid submission!
	return True

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
	return ndb.Key('Guestbook', guestbook_name)

class Submission(ndb.Model):
  """A main model for representing an individual Guestbook entry."""
  # author = ndb.StructuredProperty(Author)
  link = ndb.StringProperty(indexed=False, required=True)
  description = ndb.StringProperty(indexed=False, required=True)
  date = ndb.DateTimeProperty(auto_now_add=True)
  image_url = ndb.StringProperty(indexed=False)
  name = ndb.StringProperty(indexed=False, required=True)

