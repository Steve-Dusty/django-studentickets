from django.urls import path
from .views import HomePageView, ClassListView, ClassDetailView, ClassCreateView, ClassDeleteView, ClassStudentCreateView, ClassNameEditView, ClassStudentDeleteView, add_ticket, delete_ticket


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', ClassListView.as_view(), name='class-list'),
    path('dashboard/create/', ClassCreateView.as_view(), name='class-create'),
    path('dashboard/<int:pk>/delete/',
         ClassDeleteView.as_view(), name='class-delete'),
    path('dashboard/<int:pk>/', ClassDetailView.as_view(),
         name='class-student-list'),
    path('dashboard/<int:pk>/add', ClassStudentCreateView.as_view(),
         name='class-student-create'),
    path('dashboard/<int:student_id>/add_ticket/',
         add_ticket, name="class-ticket-add"),
    path('dashboard/<int:student_id>/delete_ticket/',
         delete_ticket, name="class-ticket-delete"),
    path('dashboard/<int:pk>/edit',
         ClassNameEditView.as_view(), name="class-name-edit"),
    path('dashboard/<int:pk>/delete_student/',
         ClassStudentDeleteView.as_view(), name="class-student-delete"),
]
