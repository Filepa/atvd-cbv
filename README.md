# Bloco de Notas - Class-Based Views

## Principais Rotas:

Criação e Edição de Notas:

```python
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
```

Detalhamento das Notas:

```python
class NoteDetailView(DetailView):
    model = Note
    template_name = 'note/detail.html'
    context_object_name = 'note'
```

Listagem de Notas:

```python
class NoteListView(ListView):
    model = Note
    template_name = 'note/list.html'
    context_object_name = 'notes'
```

Deletar Notas:

```python
class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note/delete.html'
    success_url = reverse_lazy('list_note')
```

## URLs

```python
from django.contrib import admin
from django.urls import path
from notebook.views import (
    NoteListView, NoteDetailView, NoteDeleteView, NoteUpdateView, NoteCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NoteListView.as_view(), name='list_note'),
    path('produtos/', NoteListView.as_view(), name='list_note'),
    path('produtos/<int:pk>/', NoteDetailView.as_view(), name='detail_note'),
    path('produtos/<int:pk>/editar/', NoteUpdateView.as_view(), name='update_note'),
    path('produtos/<int:pk>/excluir/', NoteDeleteView.as_view(), name='delete_note'),
    path('produtos/criar/', NoteCreateView.as_view(), name='create_note'),
]
```

## Estrutura do Principal do Projeto:

```
notebook
├── templates
│   └── note       
│       ├── delete.html
│       ├── detail.html
│       ├── form.html
│       └── list.html
└── views.py
```

## Imagens Ilustrativas:

