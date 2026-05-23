# Ad Copywriting Assistant

## Overview
This app is an AI-powered ad copywriting assistant, built using Python, LangChain, an open-source LLM from HuggingFace (DeepSeek V4 Flash), and prompt engineering. It takes a product name and a target audience, and generates a social media caption, an ad headline, and a CTA (Call to action), in a structured JSON format.

## Objectives
The main focus was to generate effective, audience aware marketing content in a structured way using an LLM.

Another key objective was to explore how prompt structure, role definition, constraints and formatting instructions influence the quality of LLM-generated outputs.

## Prompt Design
The following prompt structure was followed:
* Role definition
* Input context
* Task specification
* Constraints
* Formatting instructions

Role definition guides the tone and writing style. It guides the model towards marketing-oriented outputs and reduces possibility of generic outputs.

Input context was put before tasks and constraints, as this helps the model condition its outputs based on the inputs.

Explicit task specification reduces ambiguity, hence the control over the output and its reliability increases.

The guidelines mimic real world advertising constraints. They limit the search space of the model, hence the output becomes more consistent.

The constraints were based on my research into the characteristics and optimal lengths of effective marketing captions, headlines, and CTAs.

Finally, format instructions were provided intentionally at the end in order to reinforce structured output generation.

This particular structure removes ambiguity step by step, guiding the model from understanding context to constrained, structured output.

## Other Key Design Choices
* PydanticOutputParser was used as it enforces schema, data type and required field validation.
* Temperature was set to 0.8 in order to balance consistency and creativity of the LLM's outputs.
* DeepSeek V4 Flash was used in order to balance out output quality and inference costs.