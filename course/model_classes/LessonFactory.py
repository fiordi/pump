from django.db import models
import datetime

"""
LessonFactory Class (Abstract)
"""
class LessonFactory(models.Model):

	"""
    It decides if lessons must be created using RepeatedLessonFactory or SingleLessonFactory

    Course => Course()
    startDate => dateTime
    endDate => dateTime
    startTime => dateTime
    endTime => dateTime
    frequency => int
    weekDayOfLesson => int
    """
	def createLesson(self, Course, startDate, endDate, startTime, endTime, frequency, weekDayOfLesson):

		if (startDate == endDate):
			#gli import sono stati inseriti nel metodo e non nell'header per evitare CIRCULAR DEPENDENCE
			from course.model_classes.SingleLessonFactory import SingleLessonFactory

			date = startDate
			singlelesson = SingleLessonFactory().createLesson(date, startTime, endTime)
			singlelesson.course = Course
			singlelesson.save()

		else:
			from course.model_classes.SingleLessonFactory import SingleLessonFactory
			from course.model_classes.RepeatedLessonFactory import RepeatedLessonFactory

			repeatedlesson = RepeatedLessonFactory().createLesson()
			repeatedlesson.setLessonInfo(weekDayOfLesson, startDate, endDate, startTime, endTime)
			repeatedlesson.course = Course
			repeatedlesson.save()

			#nel caso di lezioni ripetute, devo switchare la startDate in base al giorno selezionato

			#controllo il giorno della settimana in cui inizia il corso
			startWeekDay = startDate.isoweekday()

			#sincronizzo la startDate con il WeekDayOfLesson
			if(startWeekDay > weekDayOfLesson):
				deltaDays = (7-startWeekDay) + weekDayOfLesson
			else:
				deltaDays = weekDayOfLesson - startWeekDay
			startDate = startDate + datetime.timedelta(days = deltaDays )

			while startDate <= endDate:
				date = startDate
				singlelesson = SingleLessonFactory().createLesson(date, startTime, endTime)
				singlelesson.repeatedlesson = repeatedlesson
				singlelesson.save()

				startDate = startDate + datetime.timedelta(days=frequency)

	class Meta:
		abstract = True


