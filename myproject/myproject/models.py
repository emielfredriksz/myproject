from typing import Any
from django.db import models
from django import forms
from .sentiment import GetNeg, GetNeu, GetPos, GetComp



class Review(models.Model):
    text = models.CharField(max_length=100, blank=False)
    neg = models.FloatField()
    neu = models.FloatField()
    pos = models.FloatField()
    comp = models.FloatField()

    def __str__(self):
        return self.text
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.neg = GetNeg(self.text)
        self.neu = GetNeu(self.text)
        self.pos = GetPos(self.text)
        self.comp = GetComp(self.text)
