from django.shortcuts import render, redirect
# from IPython import embed

# Create your views here.
def index(request):
  return render(request, 'first_app/index.html')

def form_process(request):
	if request.method == "POST":

		email = request.POST['email']
		print email
		# print "hello"
		# embed()
		# print "hi"
		## process the post information

		## return redirect back to the index
		# return render(request, 'first_app/index.html')
		return redirect("/")


def user_id(request, id):
	if request.session.get(id) == None:
		req_ses = None
	else:
		req_ses = request.session[id]

	# print id
	context = {
		'id' : id,
		'user_info' : request.session['1']
	}
	# print request.session['1']

	return render(request, 'first_app/user.html', context)

def user_id_edit(request, id):
	print id
	context = {
		'id' : id
	}
	return render(request, 'first_app/edit.html', context)

def user_id_update(request, id):
	# print "Hello"
	# print request.POST['email']
	# print request.POST['first_name']
	# print request.POST['occupation']
	request.session['1'] = {
		'email' : request.POST['email'],
		'first_name' : request.POST['first_name'],
		'occupation' : request.POST['occupation']
	}
	# request.session['email'] = request.POST['email']
	print request.session['1']
	# ['first_name']

	return redirect("/user_id/" + id)
