from django.core.exceptions import ValidationError


def validate_phone_number(value):
    '''
    ##################################################################################
    validating phone number value
    ##################################################################################

    '''
    sane = ['0','1','2','3','4','5','6','7','8','9','+']
    for comp in value:
        if comp not in sane:
            raise ValidationError("Enter a valid number")


        