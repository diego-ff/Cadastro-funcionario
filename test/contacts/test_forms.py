from contacts.forms import NameForm


def test_name_form_sucess():
    #Given
    data = {"your_name": "john"}
    form = NameForm(data=data)
    #When
    is_valid = form.is_valid()
    #Then
    assert is_valid is True


def test_name_form_your_name_max_length():
    #Given
    data = {"your_name": "John" * 50}
    form = NameForm(data=data)
    #When
    is_valid = form.is_valid()
    #Then
    assert is_valid is False
    assert form.errors == {
        "your_name": ["Certifique-se de que o valor tenha no máximo 100 caracteres (ele possui 200)."]
    }


def test_name_form_fail():
    #Given
    data = {}
    form = NameForm(data=data)
    #When
    result = form.is_valid()

    #Then
    assert result is False

  