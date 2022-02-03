from functools import lru_cache

import settings


@lru_cache
def get_color(value, colors, colorized=True, regular_color=settings.REGULAR_COLOR):
    if colorized:
        color_index = value % len(colors)
        return colors[color_index]
    return regular_color
