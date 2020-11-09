from blessed import Terminal
from .timer import Timer
from datetime import timedelta


def main():
    t = Terminal()
    timer = Timer()

    with t.fullscreen(), t.cbreak(), t.hidden_cursor():
        while True:
            t.move_xy(0, 0)
            timestamp = timedelta(seconds=timer.current_time)

            print(f'{t.home}{t.clear}{str(timestamp)} ({timer.ballast} in ballast)')

            key = t.inkey(timeout=0.1)

            if not key:
                continue

            key = key
            lower = key.lower()

            if lower == 'q':
                break

            if lower == 's':
                timer.start()

            if lower == 'e':
                timer.end()

            if lower == 'r':
                timer.clear()

            if lower == ' ':
                if timer.paused:
                    timer.resume()
                else:
                    timer.pause()


if __name__ == '__main__':
    main()
