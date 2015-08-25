# Lecture information is configured below
# There are 5 fields
# 1. Title
# 2. Reading list
# 3. URL for slides
# 4. URL for video
# 5. Homework

LECTURE_FIELD_COUNT = 5

LECTURES = """

A Brief history of genetics
Pub 1
Slides 1
Video 1
HW 1

A Brief history of molecular biology
Pub 2
Slides 2
Video 2
HW 2

"""

def lectures():
	lines = LECTURES.splitlines()
	lines = map(lambda x: x.strip(), lines)
    lines = filter(None, lines)
    group = [iter(lines)] * LECTURES_FIELD_COUNT
    return zip(*group)