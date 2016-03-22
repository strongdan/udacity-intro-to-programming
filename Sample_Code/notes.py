import webapp2
import cgi
from handlers import *

application = webapp2.WSGIApplication([
	('/code_pen_examples/', CodePenExampleListHandler),
	('/additional_resources/', ResourcesHandler),
	('/nanodegree_notes/', NanodegreeHandler),
  (r'/nanodegree_notes/course/(\d+)/', CourseHandler),
  ('/student_submissions/add', SubmissionHandler),
  ('/student_submissions/', SubmissionListHandler),
  ('/*', MainPage)
], debug=True)