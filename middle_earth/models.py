from django.db import models


class Verses(models.Model):
    class Meta:
        verbose_name_plural = "Verses"

    SILMARILLION = "SI"
    HOBBIT = "HO"
    FELLOWSHIP = "FR"
    TOWERS = "TO"
    KING = "RK"
    UNFINISHED = "UT"
    CHILDREN = "CH"
    BEREN = "BL"
    GONDOLIN = "FG"
    NUMENOR = "FN"
    BOOK_CHOICES = {
        SILMARILLION: "The Silmarillion",
        HOBBIT: "The Hobbit",
        FELLOWSHIP: "The Fellowship of the Ring",
        TOWERS: "The Two Towers",
        KING: "The Return of the King",
        UNFINISHED: "Unfinished Tales",
        CHILDREN: "The Children of Hurin",
        BEREN: "Beren and Luthien",
        GONDOLIN: "The Fall of Gondolin",
        NUMENOR: "The Fall of Numenor"
        }
    
    text = models.TextField()
    speaker = models.CharField(max_length=100)
    context = models.TextField()
    book = models.CharField(max_length=100, choices=BOOK_CHOICES)
    sub_book = models.CharField(max_length=20, blank=True, null=True)
    chapter = models.CharField(max_length=10, blank=True, null=True)
    page = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.text[:50]}"