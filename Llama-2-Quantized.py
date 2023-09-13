
from transformers import pipeline
from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

## Here we use Llama2 Quantized model. You can change to any other Models 
def generate_summary(input_text):
    # Load the model and tokenizer
    # Callbacks support token-wise streaming
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

    llm = LlamaCpp(
        model_path="*path to any GGUD/GGML/GPTQ models*",
        callback_manager=callback_manager, 
        max_tokens=250, # Change according to response length
        n_ctx=2048, # Change according to input length
        verbose=True,
        )  

    # Generate a response
    response = llm(f"*Necessary Prompt* '{input_text}'")
    
    return response