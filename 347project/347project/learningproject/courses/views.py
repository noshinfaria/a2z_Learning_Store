from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
import uuid
from django.utils.text import slugify
from .models import Course, Question, Reply
from .forms import QuestionForm, ReplyForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.


class CourseList(ListView):
    context_object_name = 'course_list'
    model = Course
    template_name = 'courses/course_list.html'
    paginate_by = 6

    def get_queryset(self):
        filter_val = self.request.GET.get("filter", "")
        order_by = self.request.GET.get("orderby", "id")
        if filter_val != "":
            cat = Course.objects.filter(
                Q(course_title__contains=filter_val) | Q(course_article__contains=filter_val)).order_by(order_by)
        else:
            cat = Course.objects.all().order_by(order_by)

        return cat

    def get_context_data(self, **kwargs):
        context = super(CourseList, self).get_context_data(**kwargs)
        context["filter"] = self.request.GET.get("filter", "")
        context["orderby"] = self.request.GET.get("orderby", "id")
        context["all_table_fields"] = Course._meta.get_fields()
        return context


class PublishCourse(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'courses/publish_course.html'
    fields = ('course_title', 'course_poster', 'video', 'course_article')

    def form_valid(self, form):
        course_obj = form.save(commit=False)
        course_obj.teacher = self.request.user
        title = course_obj.course_title
        course_obj.slug = slugify(title.replace(" ", "-") + str(uuid.uuid4()))
        course_obj.save()
        return HttpResponseRedirect(reverse('courses:courses'))


@login_required
def course_details(request, slug):
    course = Course.objects.get(slug=slug)
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.course = course
            question.save()
            return HttpResponseRedirect(reverse('courses:course_details', kwargs={'slug': slug}))

    return render(request, 'courses/course_details.html', {'course': course, 'form': form})


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    template_name = 'courses/course-update.html'
    fields = ('course_title', 'course_poster', 'video', 'course_article')

    def form_valid(self, form):
        course_obj = form.save(commit=False)
        course_obj.teacher = self.request.user
        title = course_obj.course_title
        course_obj.slug = slugify(title.replace(" ", "-") + str(uuid.uuid4()))
        course_obj.save()
        return HttpResponseRedirect(reverse('courses:course_details', kwargs={'slug': course_obj.slug}))

    def test_func(self):
        course = self.get_object()
        return self.request.user == course.teacher


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    template_name = 'courses/course-delete.html'
    success_url = reverse_lazy('courses:courses')

    def test_func(self):
        course = self.get_object()
        return self.request.user == course.teacher


class MyCourses(LoginRequiredMixin, ListView):
    context_object_name = 'course_list'
    model = Course
    template_name = 'courses/my_courses.html'

    def test_func(self):
        course = self.get_object()
        return self.request.user == course.teacher


@login_required
def question(request, pk):
    form = ReplyForm()
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.question = question
            reply.save()
            return HttpResponseRedirect(reverse('courses:question', kwargs={'pk': pk}))
    return render(request, 'courses/question.html', {'form': form, 'question': question})
