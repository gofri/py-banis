#!/usr/bin/python3.6
# encoding: utf-8

def join_lines(data):
    return '<br>'.join(data)

def generate_buttons(props, fill_gaps=True):
    TEMPLATE = '<a href="{href}" id={id} class="ui-btn">{title}</a>'
    DEFAULT = {'href':'#', 'title':'', 'id':''}
    
    def fix_defaults(but_props, fill_gaps):
        if not fill_gaps: 
            return but_props
        
        new_but = dict(DEFAULT)
        for k,v in but_props.items():
            new_but[k] = v
        return new_but
    
    def formatted(but_props):
        return TEMPLATE.format(**but_props)

    return join_lines(formatted(fix_defaults(but_props, fill_gaps=fill_gaps)) for but_props in props)

def generate_inputs(props, fill_gaps=True):    
    TEMPLATE = '<div class="ui-field-contain">' + \
                '<label for="{name}">{title}</label>' + \
                '<input type="{type}" name="{name}" value="{default}">' + \
                '</div>'
    DEFAULT = {'title':'', 'name':'', 'default':'', 'type':'text'}

    def fix_defaults(input_props, fill_gaps):
        if not fill_gaps: 
            return input_props
        
        new_input = dict(DEFAULT)
        for k,v in input_props.items():
            new_input[k] = v
        return new_input

    def formatted(props):
        return TEMPLATE.format(**props)

    return join_lines(formatted(fix_defaults(input_props, fill_gaps=fill_gaps)) for input_props in props)

def generate_form(action='', content='', submit_text='שלח', method='get'):
    return  f'<form action="{action}" method="{method}">' + \
            content + \
            f'<input type="submit" name="submit" value="{submit_text}">' + \
            '</form>'