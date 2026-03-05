```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python deploy.py
python invoke_with_boto3.py
deactivate
```
