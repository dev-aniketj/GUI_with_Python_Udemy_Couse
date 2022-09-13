# create your custom theme

import PySimpleGUIQt as sg

# Add your new theme colors and settings
sg.LOOK_AND_FEEL_TABLE['MyNewTheme'] = {'BACKGROUND': '#0066ff',
                                        'TEXT': '#232323',
                                        'INPUT': 'white',
                                        'TEXT_INPUT': '#232323',
                                        'SCROLL': 'gray',
                                        'BUTTON': ('white', '#ff0066'),
                                        'PROGRESS': ('#01826B', '#D0D0D0'),
                                        'BORDER': 1,
                                        'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0,
                                        }
# Switch to use your newly created theme
sg.theme('MyNewTheme')
# Call a popup to show what the theme looks like
sg.popup_get_text('Hello world')
