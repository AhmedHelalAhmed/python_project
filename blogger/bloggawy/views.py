from django.shortcuts import render
from bloggawy.models import Post
from django.contrib.auth.models import User
from bloggawy.models import Category
from bloggawy.models import Tag
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from time import gmtime, strftime
import re
from .models import Comment
from .forms import CommentForm
from .models import Like
from .models import Post
from django.core.exceptions import ObjectDoesNotExist


# from django.http import JsonResponse

# just for store the like in the model
def like(request, post_id):
    current_post = Post.objects.get(id=post_id)
    try:
        current_like_object = Like.objects.get(like_post=current_post)
        if current_like_object.like_type == False:
            current_like_object.like_type=True
            current_like_object.save()
        else:
            current_like_object.delete()
    except ObjectDoesNotExist:
        like_object = Like.objects.create(
            like_user=request.user,
            like_post=current_post,
            like_type=True
        )
        like_object.save()

    return HttpResponse("Like Done")


# just for store the dislike in the model
def dislike(request, post_id):
    current_post = Post.objects.get(id=post_id)
    try:
        current_like_object = Like.objects.get(like_post=current_post)
        if current_like_object.like_type == True:
            current_like_object.like_type=False
            current_like_object.save()
        else:
            current_like_object.delete()
    except ObjectDoesNotExist:
        like_object = Like.objects.create(
            like_user=request.user,
            like_post=current_post,
            like_type=False
        )
        like_object.save()

    return HttpResponse("Dislike Done");



# Create your views here.
def all_posts(request):
    return render(request, "posts/all_p.html", {"all_posts": Post.objects.all()})

def post_details(request, p_id):
    return render(request, "posts/post_page.html", {"post": Post.objects.get(id=p_id)})



def new_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post_user = User(1)
            # obj.post_user = request.user
            # obj.time = strftime("%a, %d %b %Y %H:%M:%s", gmtime())
            obj.save()
            words = obj.post_content.split()
            for word in words:
                if re.match(r'^#[a-zA-Z0-9]+',word):
                    tag=Tag()
                    if Tag.objects.filter(tag_name=word):
                        tag=Tag.objects.get(tag_name=word)
                    else:
                        tag.tag_name=word
                        tag.save()
                    tag.tag_posts.add(obj)
        return HttpResponseRedirect('/bloggawy/posts')
    return render(request, "posts/new.html", {"form": form, "all_cats": Category.objects.all()}) 

def index(request):
    return render(request, "web/index.html")  # http://127.0.0.1:8000/opensource/


def success(request):
    return render(request, "web/success.html")


def error(request):
    return render(request, "web/error.html")

# view post
def comment(request, post_id):
    comment_form = CommentForm()
    current_post = Post.objects.get(id=post_id)
    current_user = request.user
    if request.method == "POST":
        comment_form = CommentForm(request.POST, initial={'comment_post_id': post_id})
        if comment_form.is_valid():
            # comment_form.save()
            # current_user = User.objects.get(id=1)
            comment_form.CommentSave(current_post, current_user)
            return HttpResponseRedirect("success")
        #I have fix some problem here to display the recent comment in the top of comments
    comments_of_post = Comment.objects.filter(comment_post=current_post).order_by('-id')
    try:
        like_status = Like.objects.get(like_post=current_post, like_user=current_user)
    except ObjectDoesNotExist:
        like_status = None

    like_count = Like.objects.filter(like_type=True).count()
    dislike_count = Like.objects.filter(like_type=False).count()
    context = {
        "form": comment_form,
        "comments": comments_of_post,
        "like": like_status,
        "likes": like_count,
        "dislikes": dislike_count,
    }
    return render(request, "web/post_page.html", context)

# To send variables implecitly
# form = CreateASomething(request.POST)
# if form.is_valid():
#     obj = form.save(commit=False)
#     obj.field1 = request.user
#     obj.save()


# To check for Authentication
# if request.user.is_authenticated:
#     ... # Do something for logged-in users.
# else:
#     ... # Do something for anonymous users.
