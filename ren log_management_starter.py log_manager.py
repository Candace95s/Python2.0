import time
import random
from threading import Thread, Condition

class LogBuffer:
    def __init__(self):
        self.current_log = None
        self.is_empty = True
        self.condition = Condition()

    def write_log(self, log_msg):
        with self.condition:
            while self.is_empty == False:
                self.condition.wait()

            self.current_log = log_msg
            self.is_empty = False
            print("Generator wrote:", self.current_log)

            self.condition.notify()

    def archive_log(self):
        with self.condition:
            while self.is_empty == True:
                self.condition.wait()

            print("Archiver processed:", self.current_log)
            self.current_log = None
            self.is_empty = True

            self.condition.notify()


class LogGenerator(Thread):
    def __init__(self, buffer, log_count):
        Thread.__init__(self)
        self.buffer = buffer
        self.log_count = log_count

    def run(self):
        for i in range(1, self.log_count + 1):
            time.sleep(random.random())
            log_msg = "Log Entry " + str(i)
            self.buffer.write_log(log_msg)


class LogArchiver(Thread):
    def __init__(self, buffer, log_count):
        Thread.__init__(self)
        self.buffer = buffer
        self.log_count = log_count

    def run(self):
        for i in range(self.log_count):
            time.sleep(random.random())
            self.buffer.archive_log()


def main():
    LOG_COUNT = 5
    buffer = LogBuffer()

    gen = LogGenerator(buffer, LOG_COUNT)
    arc = LogArchiver(buffer, LOG_COUNT)

    gen.start()
    arc.start()

    gen.join()
    arc.join()

    print("\nLog Maintenance Complete.")


if __name__ == "__main__":
    main()
    