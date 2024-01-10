import pytest
from processing import remove_links,remove_hastags,remove_numbers,remove_users, apply_lemmatization, apply_stemming

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Check out this #awesome link: http://example.com", "Check out this  link: "),
        ("No hashtags or links here!", "No hashtags or links here!"),
        (123, 123),  
    ],
)
def test_remove_hashtags_and_links(input_text, expected_output):
    processed_text = remove_hastags(remove_links(input_text))
    assert processed_text == expected_output
    
    
@pytest.mark.parametrize("input_text, expected_output", [
    ("Testing @user123 regex 456removal", "Testing  regex removal"),
    ("No changes needed", "No changes needed"),
    ("1234567890", ""),
    ("@user1 @user2 @user3", '  '),
])
def test_remove_numbers_and_users(input_text, expected_output):
    processed_text = remove_numbers(remove_users(input_text))
    assert processed_text == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
    ("corriendo a la playa va un perrito, cuyo dueño se durmió por tanto cansancio.", "corr a el play ir uno perrito , cuy dueñ él durm por tant cansancio ."),
    ("ayer te vi comiendo un rico mango en la esquina del parque", "ayer tú vi com uno ric mang en el esquin del parqu"),
    ("un día como hoy salimos a la playa a surfear, a disfrutar de las olas de la vida", "uno dia com hoy sal a el play a surfear , a disfrut de el ola de el vid"),
])
def test_apply_stemming_lemmatization(input_text, expected_output):
    processed_text = apply_lemmatization(apply_stemming(input_text))
    assert processed_text == expected_output
