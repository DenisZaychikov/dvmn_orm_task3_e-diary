from datacenter.models import Schoolkid, Mark, Chastisement, Commendation, Lesson
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import random

commendation_variants = [
    'Молодец!', 'Отлично!', 'Хорошо!',
    'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!', 'Великолепно!',
    'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!',
    'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!',
    'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!',
    'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!'
]


def get_schoolkid(schoolkid_name):
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except ObjectDoesNotExist:
        print('Такого ученика в базе не существует!')
    except MultipleObjectsReturned:
        print('Учеников в базе несколько! Уточните ученика, введя фамилию, имя, отчество!')


def fix_marks(schoolkid):
    schoolkid_bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for schoolkid_bad_mark in schoolkid_bad_marks:
        schoolkid_bad_mark.points = 5
        schoolkid_bad_mark.save()


def remove_chastisements(schoolkid):
    schoolkid_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for schoolkid_chastisement in schoolkid_chastisements:
        schoolkid_chastisement.delete()


def create_commendation(schoolkid, subject_name):
    year_of_study = schoolkid.year_of_study
    group_letter = schoolkid.group_letter
    final_lesson = Lesson.objects.filter(subject__title=subject_name, year_of_study=year_of_study,
                                         group_letter=group_letter).order_by('-date').first()
    if final_lesson is None:
        print('Неправильный формат записи предмета -', subject_name)
    else:
        subject = final_lesson.subject
        teacher = final_lesson.teacher
        date = final_lesson.date
        text = random.choice(commendation_variants)
        Commendation.objects.create(text=text, created=date, schoolkid=schoolkid, subject=subject, teacher=teacher)
