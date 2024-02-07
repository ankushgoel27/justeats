from flask_babel import gettext


def text_for_key(key: str) -> str:
    if key == 'empty':
        return gettext('Required field')
    elif key == 'nullable':
        return gettext('Required field')
    elif key == 'invalid_recipe':
        return gettext('Invalid recipe')
    elif key == 'allowed':
        return gettext('Invalid value')
    elif key == 'invalid_prompt_execution':
        return gettext('Invalid prompt execution')
    elif key == 'maxlength':
        return gettext('Maximum length exceeded')
    elif key == 'minlength':
        return gettext('Minimum length not reached')
    elif key == 'invalid_email':
        return gettext('Invalid email')
    elif key == 'unique_email':
        return gettext('Email already in use')
    else:
        raise ValueError(f'Unknown key: {key}')