from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):
    
    all_data = Post.objects.all()[:6]
    all_data1= Post.objects.all()[:3]
    all_data2= Post.objects.all()[:5]
        
    context = {'all_data': all_data}
    context1 = {'all_data1': all_data1}
    context2 = {'all_data2': all_data2}
    
    combined_context = {
        'context': context,
        'context1': context1,
        'context2': context2
    }
    return render(request, 'home.html', combined_context)

def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post': post})



def olderPost(request):
    
    all_data = Post.objects.all()
    for x in all_data:
        print(x.post_title)
        print(x.post_image)
    context = {'all_data': all_data}
    return render(request, 'olderpost.html', context)


def tags(request):
    all_data = Post.objects.all()
    for x in all_data:
        print(x.post_title)
        print(x.post_image)
    context = {'all_data': all_data}
    return render(request, 'tags.html', context)

def tagSpecific(request, tag):
    tag_specific_data= Post.objects.filter(post_tag= tag)
    
    return render(request, 'tag_specific.html', {'tag_specific_data':tag_specific_data})


