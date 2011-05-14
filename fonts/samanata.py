""" Font definition module
    To create a new font definition, simply copy this file into a new one
    and change the name and sizes variables.

    While not strictly necessary, you may also change the options in the base
    dictionary for more fine-grained control.
"""

# Must edit for new fonts
name = 'Samanata'


# Optional parameters for new font
# 12 pt Font is included y default, so there is no need to add it here
sizes = [8, 9, 10]
base = dict(
    typename = 'truetype',
    antialias = 1,
    color = [0, 0, 0]
)
    
# DO NOT Change anything below this line
fontdefs = [{'name': name, 
             'size': 12}] + [{'name': '{0}_{1}'.format(name, size),
                              'size': size} for size in sizes]

[fontdef.update(base) for fontdef in fontdefs[:]]
