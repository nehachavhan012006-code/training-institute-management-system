from django.shortcuts import render, redirect, get_object_or_404

from .models import Trainer
from .forms import TrainerForm


def trainer_list(request):

    search = request.GET.get('search')

    if search:
        trainers = Trainer.objects.filter(
            full_name__icontains=search
        )
    else:
        trainers = Trainer.objects.all()

    return render(
        request,
        'trainers/trainer_list.html',
        {'trainers': trainers}
    )


def add_trainer(request):

    if request.method == 'POST':

        form = TrainerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/trainers/')

    else:
        form = TrainerForm()

    return render(
        request,
        'trainers/add_trainer.html',
        {'form': form}
    )


def edit_trainer(request, id):

    trainer = get_object_or_404(
        Trainer,
        id=id
    )

    if request.method == 'POST':

        form = TrainerForm(
            request.POST,
            instance=trainer
        )

        if form.is_valid():
            form.save()
            return redirect('/trainers/')

    else:
        form = TrainerForm(instance=trainer)

    return render(
        request,
        'trainers/edit_trainer.html',
        {'form': form}
    )


def delete_trainer(request, id):

    trainer = get_object_or_404(
        Trainer,
        id=id
    )

    trainer.delete()

    return redirect('/trainers/')