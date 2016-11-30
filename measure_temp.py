import subprocess
import re
from checks import AgentCheck

class MeasureTemp(AgentCheck):
    def check(self, instance):
        self.gauge('system.cpu.temp', re.compile(r'[^\d.]+').sub('', subprocess.Popen(["vcgencmd", "measure_temp"], stdout=subprocess.PIPE).stdout.read()))
