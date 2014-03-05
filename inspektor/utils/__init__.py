import logging
import random
import string

import download
import process

log = logging.getLogger('inspektor.utils')


def ask(question, auto=False, options="y/n"):
    """
    Raw input with a prompt.

    :param question: Question to be asked
    :param auto: Whether to return "y" instead of asking the question
    """
    if auto:
        log.info("%s (%s) y" % (question, options))
        return "y"
    return raw_input("%s (%s) " % (question, options))


def random_string(length, ignore_str=string.punctuation,
                  convert_str=""):
    """
    Return a random string using alphanumeric characters.

    :param length: Length of the string that will be generated.
    :param ignore_str: Characters that will not include in generated string.
    :param convert_str: Characters that need to be escaped (prepend "\\").

    :return: The generated random string.
    """
    r = random.SystemRandom()
    result = ""
    chars = string.letters + string.digits + string.punctuation
    if not ignore_str:
        ignore_str = ""
    for i in ignore_str:
        chars = chars.replace(i, "")

    while length > 0:
        tmp = r.choice(chars)
        if convert_str and (tmp in convert_str):
            tmp = "\\%s" % tmp
        result += tmp
        length -= 1
    return str
