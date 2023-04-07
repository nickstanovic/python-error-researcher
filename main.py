import collections
import win32evtlog


log_handle = win32evtlog.OpenEventLog(None, "System")
event_counts = collections.defaultdict(int)

while True:
    events = win32evtlog.ReadEventLog(log_handle,
                                      win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
    if not events:
        break
    for event in events:
        # Check if the event is a warning or an error
        if event.EventType in (win32evtlog.EVENTLOG_ERROR_TYPE, win32evtlog.EVENTLOG_WARNING_TYPE):
            # Get the event ID (0xFFFF is needed otherwise some event ids turn into negatives numbers)
            event_id = str(event.EventID & 0xFFFF)
            level = event.EventType
            event_counts[(event_id, level)] += 1

most_common = collections.Counter(event_counts).most_common(5)

print(f"Event ID\tLevel\t\tOccurrences")
for (event_id, level), count in most_common:
    level_name = {win32evtlog.EVENTLOG_ERROR_TYPE: 'Error', win32evtlog.EVENTLOG_WARNING_TYPE: 'Warning'}[level]
    print(f"{event_id} \t\t{level_name}\t\t{count}")

win32evtlog.CloseEventLog(log_handle)
