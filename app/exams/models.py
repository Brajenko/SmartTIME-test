from django.db import models


class Room(models.Model):
    class Meta:
        db_table = "rooms"
        ordering = ["room_number"]

    room_number = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return str(self.room_number)


class Exam(models.Model):
    class Meta:
        db_table = "exams"
        ordering = ["subject_name"]

    subject_name = models.CharField(max_length=127)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, db_column="room_id")

    def __str__(self) -> str:
        return self.subject_name


class Registration(models.Model):
    class Meta:
        db_table = "registrations"
        unique_together = ["user", "exam"]

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="registrations")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} - {self.exam}"
