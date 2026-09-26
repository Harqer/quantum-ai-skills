# Job recovery

~~~python
job = fo.execute(...)
action_id = job.action_id

# Nonblocking:
status = job.status()

# Later, even after kernel loss:
fo.activity_monitor(limit=20)
result = fo.get_result(action_id)
metadata = fo.get_action_metadata(limit=20)
~~~

Persist the action ID when the job is created. Fire Opal retrieval preserves post-processing that provider-native result retrieval does not.
