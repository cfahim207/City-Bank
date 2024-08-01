from django.shortcuts import render
from .models import BookModel
from django.views.generic import DetailView
from .import forms

# Create your views here.

class DetailsBook(DetailView):
    model=BookModel
    pk_url_kwarg='id'
    template_name='details.html'
    
    
    def post(self,request,*args, **kwargs):
        comment_form=forms.CommentForms(data=self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.books=post
            new_comment.save() 
        return self.get(request,*args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        post=self.object
        comments=post.comments.all()
        comment_form=forms.CommentForms()  
            
        context['comments']=comments
        context['comment_form']=comment_form
        return context
