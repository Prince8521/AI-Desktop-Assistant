import os
import openai
import apikey
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

#
#
# {
#   "warning": "This model version is deprecated. Migrate before January 4, 2024 to avoid disruption of service. Learn more https://platform.openai.com/docs/deprecations",
#   "id": "cmpl-7pIf1lSQLlwJqCOF6NeOwjUxiGaX7",
#   "object": "text_completion",
#   "created": 1692460815,
#   "model": "text-davinci-003",
#   "choices": [
#     {
#       "text": "\n\nSubject Line: Resignation Notice \u2013 Your Name\n\nDear [Manager Name],\n\nThis email is to formally submit my resignation from [company name] effective [date].\n\nI am extremely appreciative of the opportunities I have had here and the experience I have gained since I started working here. I am certain that this will prove beneficial to my career. I will take this experience and use it for my advancement.\n\nI am available to finish any projects and provide assistance as needed until [date]. If there is anything else I can do to prepare for my departure, please do not hesitate to let me know.\n\nSincerely,\n\nYour Name",
#       "index": 0,
#       "logprobs": null,
#       "finish_reason": "stop"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 9,
#     "completion_tokens": 138,
#     "total_tokens": 147
#   }
# }
#

print(response)
