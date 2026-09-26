# Execute

~~~python
import os, fireopal as fo
from qiskit import qasm3

fo.authenticate_qctrl_account(api_key=os.environ["QCTRL_API_KEY"])

credentials = fo.credentials.make_credentials_for_ibm_cloud(
    token=os.environ["IBM_CLOUD_API_KEY"],
    instance=os.environ["IBM_QUANTUM_CRN"],
)

qasm = qasm3.dumps(qc)
backend = fo.show_supported_devices(credentials)["supported_devices"][0]

check = fo.validate([qasm], credentials, backend)
if check.get("results"):
    raise RuntimeError(check["results"])

job = fo.execute([qasm], 2048, credentials, backend)
print(job.action_id)
result = job.result()
~~~
