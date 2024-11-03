from openai import OpenAI


REDIS_HOST= 'redis-16428.c329.us-east4-1.gce.redns.redis-cloud.com'
REDIS_PORT= '16428'
REDIS_PASSWORD= 'bFkt8Jxjs1UZZnnovLMJ3Bk9baRfRDyp'

GCS_BUCKET='ux_ai_test'

# Initialize OpenAI client
OPENAI_API_KEY = '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'
OPENAI_CLIENT = OpenAI(api_key=OPENAI_API_KEY)


PROJECT_ID='breezecart-development'


MJ_SCHEMA ={
    "prompt" : "INSERT PROMPT HERE"
}

GCS_PREFIX = 'interviews'