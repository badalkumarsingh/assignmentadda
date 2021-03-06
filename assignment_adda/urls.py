from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('subjects', views.subjects, name='subjects'),
    path('subjects/<int:topics_id>', views.topics, name="topics"),
    path('subjects/ans/<int:topic_id>', views.topic, name="topic"),
    path('new_question/<subject_id>', views.new_topic, name="new_topic"),
    path('new_answer/<topic_id>', views.new_entry, name="new_entry"),
    path('edit_answer/<edit_id>', views.edit_entry, name="edit_entry"),
    path('delete_answer/<edit_id>', views.delete_entry, name="delete_entry"),
]
