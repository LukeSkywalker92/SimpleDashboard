from SimpleDashboard import Dashboard
from SimpleDashboard.elements import *
from SimpleDashboard.tools import Poller
import psutil
import eventlet

dashboard = Dashboard('System Monitor')

# CPU

cpu_card = Card(title='CPU', width='1-2')
cpu_grid = Grid()
cpu_card.append_child(cpu_grid)

cpu_percent_p = Paragraph('CPU Percent', width='1-2')
cpu_percent_label = Paragraph(0, unit='%', digits=2, width='1-2')
cpu_percent_chart = Chart(y=[], title='CPU Percent', xlabel='Seconds', ylabel='CPU Percent (%)')
cpu_percent_poller = Poller(psutil.cpu_percent, cpu_percent_label, cpu_percent_chart)
cpu_percent_poller.start()
cpu_grid.append_child(cpu_percent_p)
cpu_grid.append_child(cpu_percent_label)


cpu_freq_p = Paragraph('CPU Frequency', width='1-2')
cpu_freq_label = Paragraph(0, unit='GHz', digits=2, width='1-2')
def get_cpu_freq():
    return psutil.cpu_freq()._asdict()['current']/1000
cpu_freq_poller = Poller(get_cpu_freq, cpu_freq_label)
cpu_freq_poller.start()
cpu_grid.append_child(cpu_freq_p)
cpu_grid.append_child(cpu_freq_label)

cpu_grid.append_child(cpu_percent_chart)

dashboard.add_element(cpu_card)

# Memory

memory_card = Card(title='Memory', width='1-2')
memory_grid = Grid()
memory_card.append_child(memory_grid)


stats = dict(psutil.virtual_memory()._asdict())
elements = {}
for stat in stats:
    elements[stat] = {
        'p': Paragraph(stat.capitalize(), width='1-2'),
        'label': Paragraph(stats[stat], width='1-2')
    }

for element in elements:
    memory_grid.append_child(elements[element]['p'])
    memory_grid.append_child(elements[element]['label'])

def memory():
    while True:
        stats = dict(psutil.virtual_memory()._asdict())
        for stat in stats:
            elements[stat]['label'].update(stats[stat])
        eventlet.sleep(1)

eventlet.greenthread.spawn(memory)
dashboard.add_element(memory_card)

dashboard.run()
