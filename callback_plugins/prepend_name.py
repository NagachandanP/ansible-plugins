# callback_plugins/monitor_callback.py
import threading
import time
from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    """
    This callback plugin monitors and displays the contents of a specified file
    during the execution of any task with 'monitor' in its name.
    """

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'monitor_callback'

    def __init__(self):
        super(CallbackModule, self).__init__()
        self.monitor_thread = None
        self.stop_monitoring = threading.Event()
        self.file_to_monitor = 'monitored_file.txt'

    def v2_runner_on_start(self, host, task):
        task_name = task.get_name().strip().lower()
        if 'monitor' in task_name:
            self.stop_monitoring.clear()
            self.monitor_thread = threading.Thread(target=self.monitor_file)
            self.monitor_thread.daemon = True
            self.monitor_thread.start()

    def v2_runner_on_ok(self, result):
        self.stop_monitoring.set()
        if self.monitor_thread:
            self.monitor_thread.join()

    def monitor_file(self):
        last_position = 0
        while not self.stop_monitoring.is_set():
            try:
                with open(self.file_to_monitor, 'r') as file:
                    file.seek(last_position)
                    new_content = file.read()
                    if new_content:
                        self._display.display(new_content.strip())
                        last_position = file.tell()
            except FileNotFoundError:
                pass
            time.sleep(1)
