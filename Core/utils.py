#!/usr/bin/python3.6
# encoding: utf-8

def list_move_entry(lst, index, direction):
    assert direction in ('up', 'down'), "Invalid direction"
    dst_index = index + (-1 if direction == 'up' else 1)
    tmp_entry = lst[dst_index]
    lst[dst_index] = lst[index]
    lst[index] = tmp_entry

def unique_combine(lst1, lst2):
    return lst1 + [e for e in lst2 if e not in lst1]