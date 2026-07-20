### This file will set up how the ai client to summarize / reduce text

# start with openai / cloud calls

from openai import OpenAI
import json
import time

class OpenAIClient():
    def __init__(self, model_name):
        self.model = model_name
        self.client = OpenAI()
        self.system_prompt = ""

    def call_ai(self, input : str):
        # wall speed
        start = time.perf_counter()

        # response object
        response = self.client.responses.create(
            model = self.model,
            instructions=self.system_prompt,
            input = input,
        )
        # end time
        elapsed = time.perf_counter() - start
        
        # metadata
        usage = response.usage
        output_tokens = usage.output_tokens if usage else 0

        # return final dict 
        return {
            "text": response.output_text,
            "input_tokens": usage.input_tokens if usage else 0,
            "output_tokens": output_tokens,
            "total_tokens": usage.total_tokens if usage else 0,
            "latency_seconds": elapsed,
            "tokens_per_second": output_tokens / elapsed if elapsed > 0 else 0.0,
        }