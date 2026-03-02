## EVALUATIONS

bucket name: christian-bedrock-evaluations

**Evaluator:** Amazon nova pro

inference, eli ketä evaluoidaan:

- **Nova Micro**  *1.0*
- Nova Lite

Create evaluations **LLM as a judge**
christian-evaluation-job

input select the bucket

evaluation results need to be inserted as text like this:
s3://christian-bedrock-evaluations/output/

evaluations-role

JOS VALITSET MUITA KUIN AWS TARJOAMIA MALLEJA TULEE ERROR:

**ValidationException**

Access to this model is not available for channel program accounts. Reach out to your AWS Solution Provider or AWS Distributor for more information.
