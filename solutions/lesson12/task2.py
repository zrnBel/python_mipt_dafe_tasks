from typing import Any, Generator, Iterable, Sized


def circle(iterable: Iterable) -> Generator[Any, None, None]:
    
    cache = []

    for elem in iterable:
        cache.append(elem)
        yield elem

    if not cache:
        return
        
    while True:
        for elem in cache:
            yield elem