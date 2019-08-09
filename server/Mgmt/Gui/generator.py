#!/usr/bin/python3.6
# encoding: utf-8

def generate_buttons(props, fill_gaps=True):
    TEMPLATE = '<a href="{href}" class="ui-btn">{title}</a>'
    DEFAULT = {'href':'#', 'title':''}
    
    def fix_defaults(but_props, fill_gaps):
        if not fill_gaps: 
            return but_props
        
        new_but = dict(DEFAULT)
        for k,v in but_props.items():
            new_but[k] = v
        return new_but
    
    def formatted(but_props):
        return TEMPLATE.format(**but_props)

    return '\n'.join(formatted(fix_defaults(but_props, fill_gaps=fill_gaps)) for but_props in props)