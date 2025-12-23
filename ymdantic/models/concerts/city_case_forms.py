from ymdantic.models.base import YMBaseModel


class CityCaseForms(YMBaseModel):
    """Pydantic модель, представляющая падежные формы названия города."""

    genitive_case: str
    # Родительный падеж.
    preposition: str
    # Предлог.
    instrumental_case: str
    # Творительный падеж.
    accusative_case: str
    # Винительный падеж.
    prepositional_case: str
    # Предложный падеж.
    dative_case: str
    # Дательный падеж.
    nominative_case: str
    # Именительный падеж.
