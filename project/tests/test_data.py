"""
Test data for the AI Text Summarizer.
Contains various text samples for testing different summarization scenarios.
"""

# Short text (simple concept)
SHORT_TEXT = """
Photosynthesis is the process by which plants convert sunlight into energy. 
During this process, plants take in carbon dioxide and water, and using sunlight, 
convert these into glucose and oxygen. The oxygen is released into the atmosphere, 
while the glucose is used by the plant for growth and energy storage.
"""

# Medium text (technical concept)
TECHNICAL_TEXT = """
Neural networks are computing systems inspired by biological neural networks in animal brains. 
The system learns to perform tasks by analyzing training examples, generally without task-specific programming. 
For example, in image recognition, they might learn to identify images containing cats by analyzing example 
images that have been manually labeled as "cat" or "no cat" and using the results to identify cats in other 
images. They do this without any prior knowledge of cats, e.g., that they have fur, tails, and whiskers. 
Instead, they automatically generate identifying characteristics from the learning material that they process.
"""

# Long text (historical event)
HISTORICAL_TEXT = """
The Industrial Revolution, which took place from the 18th to 19th centuries, was a period during which 
predominantly rural societies in Europe and America became industrial and urban. Prior to the Industrial 
Revolution, which began in Britain in the late 1700s, manufacturing was often done in people's homes, 
using hand tools or basic machines. Industrialization marked a shift to powered, special-purpose machinery, 
factories and mass production. The iron and textile industries, along with the development of the steam 
engine, played central roles in the Industrial Revolution, which also saw improved systems of transportation, 
communication and banking. While industrialization brought about an increased volume and variety of manufactured 
goods and an improved standard of living for some, it also resulted in often grim employment and living 
conditions for the poor and working classes. The effects of industrialization drew criticism from many observers, 
including Karl Marx, who believed that the industrial revolution would eventually lead to a socialist revolution.
"""

# News article style
NEWS_TEXT = """
In a groundbreaking development announced today, scientists have successfully created a quantum computer 
that can perform calculations in 200 seconds that would take the world's fastest supercomputer 10,000 years 
to complete. This achievement, known as quantum supremacy, represents a major milestone in computing technology. 
The team, comprising researchers from multiple universities, used a 53-qubit quantum computer to solve a 
complex mathematical calculation. While the practical applications of this specific achievement are limited, 
it demonstrates the enormous potential of quantum computing for solving complex problems in fields such as 
cryptography, drug development, and climate modeling. However, experts caution that significant challenges 
remain before quantum computers can be used for practical applications.
"""

# Scientific paper abstract
SCIENTIFIC_TEXT = """
Recent advances in artificial intelligence have enabled unprecedented progress in protein structure prediction. 
Here we present AlphaFold, a deep learning system that can predict protein structures with atomic accuracy 
even where no similar structure is known. This has been a grand challenge in biology for decades, and our 
solution has been validated in the challenging 14th Critical Assessment of Protein Structure Prediction (CASP14). 
The system uses a novel neural network architecture that processes multiple sequence alignments and pairwise 
features to predict structures. In CASP14, AlphaFold achieved a median score of 92.4 GDT across all targets. 
This breakthrough demonstrates the potential of AI to significantly advance scientific discovery and its 
application to complex biological problems.
"""

# Multi-topic text
MULTI_TOPIC_TEXT = """
Climate change and technological innovation are reshaping our world in unprecedented ways. Rising global 
temperatures are affecting weather patterns, leading to more frequent extreme weather events and shifting 
agricultural zones. Meanwhile, advances in artificial intelligence and renewable energy are offering potential 
solutions. Electric vehicles are becoming mainstream, with global sales doubling in the past year. AI systems 
are helping to optimize energy grids and predict weather patterns with greater accuracy. However, these 
solutions also present new challenges, such as the need for rare earth minerals for batteries and the 
increasing energy consumption of data centers. The intersection of these environmental and technological 
trends will likely define many of the challenges and opportunities of the 21st century.
"""

# Text with quotes and dialogue
DIALOGUE_TEXT = """
During the historic Apollo 11 mission briefing, Neil Armstrong explained their objective: "Our mission is 
to land on the Moon and return safely to Earth." The tension in the room was palpable as he continued, 
"The risks are significant, but the potential benefits to science and humanity are immeasurable." Mission 
Control responded with their iconic phrase, "All systems are go." On July 20, 1969, as Armstrong stepped 
onto the lunar surface, he uttered the famous words, "That's one small step for man, one giant leap for 
mankind." This moment marked not only a triumph of human engineering and courage but also the beginning 
of a new era in space exploration. Upon their return, President Nixon declared, "This is the greatest 
week in the history of the world since the Creation."
""" 