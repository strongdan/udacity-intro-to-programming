# TODO : Add comments throughout
# TODO : Minimize everything! LESS CODE, more abstraction
# TODO : Change duplicate names! No lines of code that say examples=examples!
# TODO : Change for loops to not ALL be `for element in elements` No Pluralization magic!

import os
import webapp2
import jinja2
from urlparse import urlparse

from content import COURSES, TOPICS, SECTIONS, CODE_PENS, guestbook_key, Submission, DEFAULT_GUESTBOOK_NAME
import urllib


template_dir = os.path.join(os.path.dirname(__file__), 'html_templates')
jinja_env = jinja2.Environment(
	loader = jinja2.FileSystemLoader(template_dir),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, courses=COURSES, sections=SECTIONS, **kw))

class MainPage(Handler):
	def get(self):
		self.render("/main_page.html", page_name="home")

class NanodegreeHandler(Handler):
	def get(self):
		self.render('nanodegree_notes.html', page_name="notes")

class CourseHandler(Handler):
	def get(self, course_number):
		self.render("course.html", course_number=int(course_number), course=COURSES[int(course_number)-1], page_name="notes")

class ResourcesHandler(Handler):
	def get(self):
		self.render('additional_resources.html', topics=TOPICS, page_name="resources")

class CodePenExampleListHandler(Handler):
	def get(self, error=False):
		self.render('code_pen_examples.html', examples=CODE_PENS, page_name="codepen")

class SubmissionListHandler(Handler):
	def get(self):
		guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)
		submissions_query = Submission.query(
			ancestor=guestbook_key(guestbook_name)).order(-Submission.date)
		submissions = submissions_query.fetch(10)
		self.render('guestbook.html', submissions=submissions, page_name="submissions")

class SubmissionHandler(Handler):
	def get(self, **kwargs):
		self.render('add_submission.html', page_name="submissions", **kwargs)

	def post(self):
		guestbook_name = self.request.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)
		submission = Submission(parent=guestbook_key(guestbook_name))
		submission.name = self.request.get('name')
		submission.link = self.request.get('link')
		submission.description = self.request.get('description')
		submission.image_url = self.request.get('image_url')

		query_params = {"guestbook_name" : guestbook_name,
										"name": submission.name,
										"link":submission.link,
										"description":submission.link,
										"image_url":submission.image_url,
										"secret_key" : self.request.get("secret_key") }

		is_valid, errors = validate_submission(submission, self.request.get('secret_key'))
		if is_valid:
			submission.put()
			self.redirect('/student_submissions/')
		else:
			for k, v in errors.items():
				query_params[k] = v
			self.get(**query_params)

def is_appspot_url(url):
	if url.find(".appspot.com") > 5:
		return True
	else:
		return False

def validate_submission(submission, secret_key):
	valid = True
	errors = {}
	if not is_appspot_url(submission.link):
		errors['link_error'] = "Your URL is not a valid appspot.com URL."
		valid = False
	if len(submission.name) < 2:
		errors['name_error'] = "Please enter a name to display."
		valid = False
	if len(submission.description) < 10:
		errors['description_error'] = "Please enter a description for your project (at least 10 characters)"
		valid = False
	appspot_id = get_appspot_id(submission.link)
	correct_key = generate_secret_key(appspot_id)
	if secret_key != correct_key:
		errors['secret_key_error'] = "That key is incorrect. Your Project reviewer should have included a 6-character key in your final project review."
		valid=False
	return valid, errors

def get_appspot_id(url):
	from urlparse import urlparse
	parsed = urlparse(url)
	return parsed.netloc.split('.')[0]

def generate_secret_key(appspot_id):
    import hashlib

    def is_valid_appspot_id(appspot_id):
        """Helper function to help identify invalid IDs"""
        num_chars = len(appspot_id)
        if num_chars < 6 or num_chars > 30:
            print "appspot ids are between 6 and 30 characters"
            return False
        valid_chars = "abcdefghijklmnopqrstuvwxyz0123456789-"
        for char in appspot_id:
            if char not in valid_chars:
                print "appspot ids do not allow: %s" % char
                return False
        return True

    # Check for valid appspot_id
    if not is_valid_appspot_id(appspot_id):
        print "Invalid appspot ID"
        return None

    # appspot_id looks good. Generate key...
    hashed_id = hashlib.sha224(appspot_id).hexdigest()
    secret_key = hashed_id[0:6] # simplicity > security

    print "Secret key is: %s" % secret_key
    return secret_key

