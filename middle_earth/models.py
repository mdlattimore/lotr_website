from django.db import models


class Verses(models.Model):
    """Page numbers for The Lord of the Rings (The Fellowship of the Ring, The Two Towers, 
    and The Return of the King) are taken from 
    Tolkien, J. R. R. 2021. The Lord of the Rings Illustrated. William Morrow & Company.
    Also, while the printed LOTR version referenced has the entire LOTR in one volume, references 
    are given in the name of each of the individual books (The Fellowship of the Ring, containing
    Books I and II; The Two Towers, containing Books III and IV; and The Return of the King,
    containing Books V and VI). 
    
    Unless necessary to avoid confusion or (as in the case of Tom Bombadil), the speaking character 
    is almost always referred to by his/her entire name, the speaker should only be listed using 
    the first or commonly used name. For example, Frodo instead of Frodo Baggins or Sam instead of
    Sam Gamgee. Where a speaker may have more than one common name, the name the speaker uses at
    the time of speaking the verse should be used. For example, the gray wizard may be called
    Mithrandir in The Silmirillion but Gandalf in The Hobbit.

    To address difficulties in searching texts containing unicode escape codes, all words have been 
    normalized to remove any diacritical marks so common in Middle Earth literature. So, for example,
    instead of Túrin, the character's name is saved and shown as Turin.

    For all books, there are also references to "Books" and Chapters
    to facilitate use of other printed versions that may not follow the same pagination as
    the cited versions. 
    """
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