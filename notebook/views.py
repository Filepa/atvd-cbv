from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Note
from .forms import NoteForm

# Create your views here.
class NoteListView(ListView):
    model = Note
    template_name = 'note/list.html'
    context_object_name = 'notes'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'note/detail.html'
    context_object_name = 'note'

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note/form.html'
    success_url = reverse_lazy('list_note')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note/form.html'
    success_url = reverse_lazy('list_note')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note/delete.html'
    success_url = reverse_lazy('list_note')