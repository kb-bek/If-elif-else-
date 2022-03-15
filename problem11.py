def get_extension(filename):
    filename_parts = filename.split('.')
    if len(filename_parts) < 2:  # filename has no dots
        raise ValueError('the file has no extension')
    first, *middle, last = filename_parts
    if not last or not first and not middle:
        # example filenames: .filename, filename., file.name.
        raise ValueError('the file has no extension')
    return filename_parts[-1]
print(get_extension('abc.py'))
print(get_extension('abc'))  # raises ValueError
print(get_extension('.abc'))   # raises ValueError
print(get_extension('.abc.def.'))   # raises ValueError