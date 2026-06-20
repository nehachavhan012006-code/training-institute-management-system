from django.shortcuts import render, redirect, get_object_or_404

from .models import Feedback
from .forms import FeedbackForm


def feedback_list(request):

    search = request.GET.get('search')

    if search:

        feedbacks = Feedback.objects.filter(
            comment__icontains=search
        )

    else:

        feedbacks = Feedback.objects.all()

    return render(
        request,
        'feedback/feedback_list.html',
        {'feedbacks': feedbacks}
    )


def add_feedback(request):

    if request.method == 'POST':

        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/feedback/')

    else:

        form = FeedbackForm()

    return render(
        request,
        'feedback/add_feedback.html',
        {'form': form}
    )


def edit_feedback(request, id):

    feedback = get_object_or_404(
        Feedback,
        id=id
    )

    if request.method == 'POST':

        form = FeedbackForm(
            request.POST,
            instance=feedback
        )

        if form.is_valid():
            form.save()
            return redirect('/feedback/')

    else:

        form = FeedbackForm(instance=feedback)

    return render(
        request,
        'feedback/edit_feedback.html',
        {'form': form}
    )


def delete_feedback(request, id):

    feedback = get_object_or_404(
        Feedback,
        id=id
    )

    feedback.delete()

    return redirect('/feedback/')