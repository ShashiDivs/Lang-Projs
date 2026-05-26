from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.4,
    max_tokens=200
)

# Simple fatcual prompt
#response = llm.invoke("What is the capital of Telangana?")

#Creative prompt
# response = llm.invoke("Write a small essay on the topic of AI and its impact on the world.")
# print(response.content)

# Summarisation prompt
# response = llm.invoke("""
# Firstly, the economic transformation driven by AI is profound. Businesses are increasingly leveraging AI to optimize operations, improve customer experiences, and drive innovation. For instance, in the manufacturing sector, AI-powered automation is streamlining production processes, reducing costs, and increasing efficiency. In finance, algorithms analyze vast datasets at unprecedented speeds to identify market trends, assess risks, and make investment decisions.This ability to process information rapidly and accurately allows companies to make data-driven decisions, fostering a competitive edge in the global market. However, this transformation also raises concerns about job displacement, as automation may replace certain roles, particularly those involving repetitive tasks. While AI generates new job opportunities in tech-driven fields, the transition may lead to significant workforce disruptions.

# Secondly, AI is having significant social implications. In healthcare, AI technologies such as machine learning and natural language processing are revolutionizing diagnostics and treatment plans. Predictive analytics can identify patient risks based on historical data, allowing for earlier interventions. Additionally, AI-powered telemedicine platforms are making healthcare more accessible, particularly in underserved areas. However, the integration of AI in sensitive sectors also raises questions about privacy, data security, and equity in access to these innovations. The algorithms that underpin AI systems can sometimes perpetuate biases present in the data they are trained on, leading to inequitable outcomes that disproportionately affect marginalized communities.

# Finally, the ethical considerations surrounding AI cannot be overlooked. As AI systems become more autonomous, questions arise about accountability and transparency. Who is responsible when an AI system makes an error? How can we ensure that AI technologies are developed and deployed ethically? The potential for misuse of AI, such as in surveillance or the creation of deepfakes, poses significant risks to civil liberties and societal trust. Addressing these ethical dilemmas requires a concerted effort from technologists, policymakers, and ethicists to establish frameworks that promote responsible AI use.
# """)
# print(response.content)


# Translation prompt
response = llm.invoke("Translate the following text from English to Hindi: 'Hello, how are you?'")
print(response.content)