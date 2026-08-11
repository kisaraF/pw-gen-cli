import string
from pw_gen_cli.password_gen import pwd_gen


def test_pwdgen_10():
    stdout = pwd_gen(10)

    stdout_len = len(stdout)
    stdout_int = len([i for i in list(stdout) if i.isdigit()])
    stdout_lower = len([i for i in list(stdout) if i.islower()])
    stdout_upper = len([i for i in stdout if i.isupper()])
    stdout_punc = len(
        [i for i in list(stdout) if any(letter in string.punctuation for letter in i)]
    )

    # check password length matches
    assert stdout_len == 10

    # check number of int characters
    assert stdout_int == round(10 * 0.2)

    # check number of lowercase characters
    assert stdout_lower == round(10 * 0.3)

    # check number of uppercase characters
    assert stdout_upper == round(10 * 0.3)

    # check number of uppercase characters
    assert stdout_punc == round(10 * 0.2)


def test_pwdgen_16():
    stdout = pwd_gen(16)

    stdout_len = len(stdout)
    stdout_int = len([i for i in list(stdout) if i.isdigit()])
    stdout_lower = len([i for i in list(stdout) if i.islower()])
    stdout_upper = len([i for i in stdout if i.isupper()])
    stdout_punc = len(
        [i for i in list(stdout) if any(letter in string.punctuation for letter in i)]
    )

    # check password length matches
    assert stdout_len == 16

    # check number of int characters
    assert stdout_int == round(16 * 0.2)

    # check number of lowercase characters
    assert stdout_lower == round(16 * 0.3)

    # check number of uppercase characters
    assert stdout_upper == round(16 * 0.3)

    # check number of uppercase characters
    assert stdout_punc == round(16 * 0.2)


def test_pwdgen_30():
    stdout = pwd_gen(30)

    stdout_len = len(stdout)
    stdout_int = len([i for i in list(stdout) if i.isdigit()])
    stdout_lower = len([i for i in list(stdout) if i.islower()])
    stdout_upper = len([i for i in stdout if i.isupper()])
    stdout_punc = len(
        [i for i in list(stdout) if any(letter in string.punctuation for letter in i)]
    )

    # check password length matches
    assert stdout_len == 30

    # check number of int characters
    assert stdout_int == round(30 * 0.2)

    # check number of lowercase characters
    assert stdout_lower == round(30 * 0.3)

    # check number of uppercase characters
    assert stdout_upper == round(30 * 0.3)

    # check number of uppercase characters
    assert stdout_punc == round(30 * 0.2)
