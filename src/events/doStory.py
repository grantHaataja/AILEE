"""
Check for, and run, story events.
"""

import events

'''
This is the function
  checkAndRunStoryScript()
talked about in the main.py discussion.
I called it doStory.py -- the function effectively takes that name, and checkAndRunStoryScript.py was too long.
'''

EVENTS = [e for e in events.__all__ if e.startswith('event')]
EVENTS.sort()


def run(*args, **kwargs):
    # TODO: get that events list VVV
    # print("Beginning event checking")
    game = kwargs['game']
    for event in EVENTS:
        event = getattr(events, event)
        eventready = event.check_run(*args, **kwargs)
        ename = event.__name__.split('.')[-1]
        nodup = ename not in game.events_run
        if eventready and nodup:
            game.events_run.append(event.__name__.split('.')[-1])
            event.run(*args, **kwargs)
            return  # prevent multiple runs with same command
